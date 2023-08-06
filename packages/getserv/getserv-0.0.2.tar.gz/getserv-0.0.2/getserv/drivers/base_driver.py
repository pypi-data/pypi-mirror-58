import argparse


class BaseDriver:
  arg_parser: argparse.ArgumentParser

  def __init__(self, parser: argparse.ArgumentParser):
    self.arg_parser = parser

  def create_parser():
    raise Exception('No parser created')

  def init_parser(parser: argparse.ArgumentParser):
    return parser

  def get_name():
    raise Exception('Name for driver required')

  def run(self):
    return []
