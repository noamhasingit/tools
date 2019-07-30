#!/usr/bin/env python3

import checkenvs
import checklibs
import diskspace
import osdetails


def main():
    osdetails.main()
    diskspace.print_usage("/")
    checklibs.main()
    checkenvs.main()


if __name__ == "__main__":
    main()
