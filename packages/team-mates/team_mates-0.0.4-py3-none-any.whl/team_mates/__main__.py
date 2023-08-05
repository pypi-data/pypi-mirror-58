import sys
import argparse
import subprocess


def parse_args():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers()

    # define run parser
    run_parser = subparsers.add_parser('run')
    run_parser.set_defaults(action='run')
    run_parser.add_argument(
        '--host', type=str, default='localhost', help='Server address')
    run_parser.add_argument(
        '-p', '--port', type=int, default=5000, help='Server port')
    run_parser.add_argument(
        '-b', '--bind', help='Server binding to format <HOST>:<PORT> (e.g 0.0.0.0:80)')

    args = parser.parse_args()
    if not hasattr(args, 'action'):
        parser.print_help()
        sys.exit(1)

    return args


def main():
    args = parse_args()

    if args.action == 'run':
        if args.bind is None:
            address = '%s:%s' % (args.host, args.port)
        else:
            address = args.bind

        subprocess.call(['gunicorn', '-b', address, 'team_mates.server:app'])


if __name__ == '__main__':
    main()
