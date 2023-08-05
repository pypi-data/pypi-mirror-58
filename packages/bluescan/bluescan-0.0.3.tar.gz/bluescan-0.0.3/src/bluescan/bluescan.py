#!/usr/bin/env python3

from bluescan.br_scan import BRScanner
from bluescan.le_scan import LEScanner
from bluescan.ui import parse_cmdline
from bluepy.btle import BTLEException

import subprocess
import time


def main():
    try:
        args = parse_cmdline()

        subprocess.getoutput('hciconfig hci%d reset' % args['-i'])
        subprocess.getoutput('hciconfig hci%d noscan' % args['-i'])

        if args['-m'] == 'br':
            br_scanner = BRScanner(args['-i'])
            if args['--async']:
                br_scanner.async_scan(args['--inquiry-len'])
            else:
                br_scanner.scan(args['--inquiry-len'], sort=args['--sort'])
        elif args['-m'] == 'le':
            LEScanner(args['-i']).scan(args['--timeout'], 
                args['--le-scan-type'], args['--sort']
            )
        else:
            print("[Error] invalid scan mode")
    except (BTLEException, ValueError) as e:
        print(e)
    except KeyboardInterrupt:
        print("\n[i] " + args['-m'].upper() + " scan canceled\n")


if __name__ == "__main__":
    main()
