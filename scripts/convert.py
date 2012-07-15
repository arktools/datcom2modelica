#!/usr/bin/env python

# Copyright 2012 Lenna X. Peterson (github.com/lennax)
# All rights reserved
# License: GPL v3
# This program comes with ABSOLUTELY NO WARRANTY. This is free software
# and you are welcome to distribute it under certain conditions.
# For details, see license.txt

import argparse
import logging

from datcom2modelica import Convert

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("infile",
                        help="DATCOM file to convert")
    parser.add_argument("outfile",
                        help="Path to write converted file")
    parser.add_argument("-f", "--format",
                        choices=['table', 'model'], default='model',
                        help="Format to write (table not implemented)")
    noise = parser.add_mutually_exclusive_group()
    noise.add_argument("-q", "--quiet", action="store_true",
                       help="Less output")
    noise.add_argument("-v", "--verbose", action="store_true",
                       help="More output")

    args = parser.parse_args()

    if args.quiet:
        log_level = logging.WARNING
    elif args.verbose:
        log_level = logging.DEBUG
    else:
        log_level = logging.INFO

    logging.basicConfig(format="%(message)s", level=log_level)

    # TODO add format argument to Convert
    Convert(args.infile, args.outfile)
