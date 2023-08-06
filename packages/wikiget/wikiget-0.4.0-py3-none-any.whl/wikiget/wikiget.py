# wikiget - CLI tool for downloading files from Wikimedia sites
# Copyright (C) 2018, 2019, 2020 Cody Logan
# SPDX-License-Identifier: GPL-3.0-or-later
#
# Wikiget is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Wikiget is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Wikiget. If not, see <https://www.gnu.org/licenses/>.

"""Main wikiget functions."""

import argparse
import hashlib
import logging
import os
import re
import sys
from urllib.parse import unquote, urlparse

from mwclient import InvalidResponse, Site, __version__ as mwclient_version
from requests import ConnectionError
from tqdm import tqdm

from wikiget.version import __version__

BLOCKSIZE = 65536
DEFAULT_SITE = 'commons.wikimedia.org'
USER_AGENT = 'wikiget/{} (https://github.com/clpo13/wikiget) ' \
             'mwclient/{}'.format(__version__, mwclient_version)


def main():
    """
    Main entry point for console script. Automatically compiled by setuptools
    when installed with `pip install` or `python setup.py install`.
    """

    parser = argparse.ArgumentParser(description="""
                                     A tool for downloading files from
                                     MediaWiki sites using the file name or
                                     description page URL
                                     """,
                                     epilog="""
                                     Copyright (C) 2018, 2019, 2020 Cody Logan.
                                     License GPLv3+: GNU GPL version 3 or later
                                     <http://www.gnu.org/licenses/gpl.html>.
                                     This is free software; you are free to
                                     change and redistribute it under certain
                                     conditions. There is NO WARRANTY, to the
                                     extent permitted by law.
                                     """)
    parser.add_argument('FILE', help="""
                        name of the file to download with the File: or Image:
                        prefix, or the URL of its file description page
                        """)
    parser.add_argument('-V', '--version', action='version',
                        version='%(prog)s {}'.format(__version__))
    output_options = parser.add_mutually_exclusive_group()
    output_options.add_argument('-q', '--quiet',
                                help='suppress warning messages',
                                action='store_true')
    output_options.add_argument('-v', '--verbose',
                                help='print detailed information; '
                                'use -vv for even more detail',
                                action='count', default=0)
    parser.add_argument('-f', '--force',
                        help='force overwriting existing files',
                        action='store_true')
    parser.add_argument('-s', '--site', default=DEFAULT_SITE,
                        help='MediaWiki site to download from '
                        '(default: %(default)s)')
    parser.add_argument('-o', '--output', help='write download to OUTPUT')
    parser.add_argument('-a', '--batch',
                        help='treat FILE as a textfile containing multiple '
                        'files to download, one URL or filename per line',
                        action='store_true')

    args = parser.parse_args()

    # print API and debug messages in verbose mode
    if args.verbose >= 2:
        logging.basicConfig(level=logging.DEBUG)
    elif args.verbose >= 1:
        logging.basicConfig(level=logging.WARNING)

    if args.batch:
        # batch download mode
        input_file = args.FILE
        if args.verbose >= 1:
            print("Info: using batch file '{}'".format(input_file))
        try:
            fd = open(input_file, 'r')
        except IOError as e:
            print('File could not be read. '
                  'The following error was encountered:')
            print(e)
            sys.exit(1)
        else:
            with fd:
                for _, line in enumerate(fd):
                    line = line.strip()
                    download(line, args)
    else:
        # single download mode
        dl = args.FILE
        download(dl, args)


def download(dl, args):
    url = urlparse(dl)

    if url.netloc:
        filename = url.path
        site_name = url.netloc
        if args.site is not DEFAULT_SITE and not args.quiet:
            # this will work even if the user specifies 'commons.wikimedia.org'
            print('Warning: target is a URL, '
                  'ignoring site specified with --site')
    else:
        filename = dl
        site_name = args.site

    file_match = valid_file(filename)
    site_match = valid_site(site_name)

    # check for valid site parameter
    if not site_match:
        print('Only Wikimedia sites (wikipedia.org and wikimedia.org) '
              'are currently supported.')
        sys.exit(1)

    # check if this is a valid file
    if file_match and file_match.group(1):
        # has File:/Image: prefix and extension
        filename = file_match.group(2)
    else:
        # no file extension and/or prefix, probably an article
        print('Downloading Wikipedia articles is not currently supported.',
              end='')
        if file_match and not file_match.group(1):
            # file extension detected, but no prefix
            # TODO: no longer possible to get to this point since
            # file_match is None with no prefix
            print(" If this is a file, please add the 'File:' prefix.")
        else:
            print('\n', end='')
        sys.exit(1)

    filename = unquote(filename)  # remove URL encoding for special characters

    dest = args.output or filename

    if args.verbose >= 2:
        print('User agent: {}'.format(USER_AGENT))

    # connect to site and identify ourselves
    try:
        site = Site(site_name, clients_useragent=USER_AGENT)
    except ConnectionError:
        # usually this means there is no such site,
        # or there's no network connection
        print("Error: couldn't connect to specified site.")
        sys.exit(1)
    except InvalidResponse as e:
        # site exists, but we couldn't communicate with the API endpoint
        print(e)
        sys.exit(1)

    # get info about the target file
    file = site.images[filename]

    if file.imageinfo != {}:
        # file exists either locally or at Wikimedia Commons
        file_url = file.imageinfo['url']
        file_size = file.imageinfo['size']
        file_sha1 = file.imageinfo['sha1']

        if args.verbose >= 1:
            print("Info: downloading '{}' "
                  '({} bytes) from {}'.format(filename, file_size, site.host),
                  end='')
            if args.output:
                print(" to '{}'".format(dest))
            else:
                print('\n', end='')
            print('Info: {}'.format(file_url))

        if os.path.isfile(dest) and not args.force:
            print("File '{}' already exists, skipping download "
                  '(use -f to ignore)'.format(dest))
        else:
            try:
                fd = open(dest, 'wb')
            except IOError as e:
                print('File could not be written. '
                      'The following error was encountered:')
                print(e)
                sys.exit(1)
            else:
                # download the file
                with tqdm(total=file_size, unit='B',
                          unit_scale=True, unit_divisor=1024) as progress_bar:
                    with fd:
                        res = site.connection.get(file_url, stream=True)
                        progress_bar.set_postfix(file=dest, refresh=False)
                        for chunk in res.iter_content(1024):
                            fd.write(chunk)
                            progress_bar.update(len(chunk))

            # verify file integrity and optionally print details
            dl_sha1 = verify_hash(dest)

            if args.verbose >= 1:
                print('Info: downloaded file SHA1 is {}'.format(dl_sha1))
                print('Info: server file SHA1 is {}'.format(file_sha1))
            if dl_sha1 == file_sha1:
                if args.verbose >= 1:
                    print('Info: hashes match!')
                # at this point, we've successfully downloaded the file
            else:
                print('Error: hash mismatch! Downloaded file may be corrupt.')
                sys.exit(1)

    else:
        # no file information returned
        print("Target '{}' does not appear to be a valid file."
              .format(filename))
        sys.exit(1)


def valid_file(search_string):
    """
    Determines if the given string contains a valid file name, defined as a
    string ending with a '.' and at least one character, beginning with 'File:'
    or 'Image:', the standard file prefixes in MediaWiki.
    :param search_string: string to validate
    :returns: a regex Match object if there's a match or None otherwise
    """
    # second group could also restrict to file extensions with three or more
    # letters with ([^/\r\n\t\f\v]+\.\w{3,})
    file_regex = re.compile(r'(File:|Image:)([^/\r\n\t\f\v]+\.\w+)$', re.I)
    return file_regex.search(search_string)


def valid_site(search_string):
    """
    Determines if the given string contains a valid site name, defined as a
    string ending with 'wikipedia.org' or 'wikimedia.org'. This covers all
    subdomains of those domains. Eventually, it should be possible to support
    any MediaWiki site, regardless of domain name.
    :param search_string: string to validate
    :returns: a regex Match object if there's a match or None otherwise
    """
    site_regex = re.compile(r'wiki[mp]edia\.org$', re.I)
    return site_regex.search(search_string)


def verify_hash(filename):
    """
    Calculates the SHA1 hash of the given file for comparison with a known
    value.
    :param filename: name of the file to calculate a hash for
    :return: hash digest
    """
    hasher = hashlib.sha1()
    with open(filename, 'rb') as dl:
        buf = dl.read(BLOCKSIZE)
        while len(buf) > 0:
            hasher.update(buf)
            buf = dl.read(BLOCKSIZE)
    return hasher.hexdigest()
