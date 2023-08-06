import argparse
from urllib.request import Request, urlopen
from urllib.error import HTTPError
import json
import os
import sys

from .base_driver import BaseDriver


class DigitaloceanDriver(BaseDriver):
  api_base_url = 'https://api.digitalocean.com/v2/'

  def get_name():
    return 'digitalocean'

  def create_parser(sub_parsers: argparse._SubParsersAction):
    return sub_parsers.add_parser(
      DigitaloceanDriver.get_name(),
      help='Retrieves ips from DigitalOcean droplets by tags',
      description='Retrieve node ips by tags'
    )

  def init_parser(parser: argparse.ArgumentParser):
    parser.add_argument(
      '--digitalocean-access-token',
      default=os.environ.get('DIGITALOCEAN_ACCESS_TOKEN', ''),
      help='\
        If not set, the "DIGITALOCEAN_ACCESS_TOKEN" \
        environment variable will be used instead\
      '
    )

    parser.add_argument(
      'droplet_tags',
      nargs=1,
      type=str,
      help='A comma separated list of tags'
    )

    return parser

  def run(self, args):
    return self.fetch(
      ','.join(args.droplet_tags),
      args.digitalocean_access_token
    )

  def fetch(self, tagSeq: str, token: str):
    tags = [tag.strip() for tag in tagSeq.split(',')]
    droplet_ips = set()
    results = []

    for tag in tags:
      try:
        request = Request(self.api_base_url + 'droplets?tag_name=' + tag)

        request.add_header('Content-Type', 'application/json')
        request.add_header('Authorization', 'Bearer ' + token)
        results.append(json.loads(urlopen(request).read()))
      except HTTPError as e:
        if (e.code == 401):
          print(
            'Invalid access token for Digital ocean given: 401 Unauthorized'
          )
        else:
          print('Something went wrong while accessing the DigitalOcean API')

        sys.exit(1)

    for result in results:
      for droplet in result['droplets']:
        droplet_tags = droplet['tags']

        # The next lines will check if the current droplet
        # has the tags constrained by the user.
        # If so, it'll check if the droplet is attached
        # to a publice network in order to save the
        # IPv4 address
        if set(tags).issubset(droplet_tags):
          for network in droplet['networks']['v4']:
            if network['type'] == 'public':
              droplet_ips.add(network['ip_address'])

    return list(droplet_ips)
