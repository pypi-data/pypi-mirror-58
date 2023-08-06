import argparse
import sys
import socket

from .drivers.digitalocean_driver import DigitaloceanDriver

drivers = [DigitaloceanDriver]


def create_parser():
  parser = argparse.ArgumentParser(
    description='Get master node from a cluster'
  )

  parser.add_argument(
    '--test-port',
    default=22,
    type=int,
    help='The port to use for a connection test'
  )

  return parser


def is_server_reachable(ip: str, port: int = 22):
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  try:
    s.connect((ip, port))
    s.shutdown(socket.SHUT_WR)
    return True
  except socket.SO_ERROR:
    return False


def main():
  main_parser = argparse.ArgumentParser(
    description='Get master node from a cluster'
  )

  main_parser.add_argument(
    '-p',
    '--test-port',
    default=22,
    type=int,
    help='The port to use for a connection test'
  )

  main_parser.add_argument(
    '-a',
    '--list-all',
    action='store_true',
    help='List all reachable servers'
  )

  sub_parsers = main_parser.add_subparsers(help='drivers', dest='driver')
  driver_parsers = {}

  for driver in drivers:
    parser = driver.create_parser(sub_parsers)
    driver_parsers[driver.get_name()] = driver.init_parser(parser)

  main_args = main_parser.parse_args()

  if main_args.driver is None:
    main_parser.print_help()
  else:
    driver_class = None

    for drv in drivers:
      if drv.get_name() == main_args.driver:
        driver_class = drv

    if driver_class is None:
      raise Exception('Driver "' + main_args.driver + '" not found')

    driver = driver_class(driver_parsers[main_args.driver])
    server_ips = driver.run(main_args)
    reachable_ips = []

    for ip in server_ips:
      if (is_server_reachable(ip, main_args.test_port)):
        reachable_ips.append(ip)

        if main_args.list_all is False:
          break

    for ip in reachable_ips:
      print(ip)


if __name__ == '__main__':
  sys.exit(main() or 0)
