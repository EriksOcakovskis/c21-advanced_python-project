# Used for Python2 to make strings unicode
from __future__ import unicode_literals
# Used for Python2 to make print() work
from __future__ import print_function
# Used for Python2 to make imports call standar library first
from __future__ import absolute_import
# Enables non-truncating division (dividing two integers results in a float.)
from __future__ import division

# Imports
import argparse
import csv
import requests

# makes new-style classes in Python 2.
__metaclass__ = type


class MyParsers(object):
  """Parsers for BTC csv info app"""

  def parse_args(self):
    ap = argparse.ArgumentParser(
        description='Given csv file provides Bitcoin data')

    ap.add_argument('--url', '-u', help='Provide url to csv file', type=str)
    ap.add_argument('--path', '-p', help='Provide path to csv file', type=str)

    args = ap.parse_args()

    if not (args.path or args.url):
      ap.error('Command line argument is missing')

    return args

  def parse_url(self, url):
    data = []
    r = requests.get(url)
    c = r.text
    reader = csv.reader(c.splitlines(), delimiter=str(','))
    try:
      for row in reader:
        data.append(row)
    except csv.Error as e:
      raise Exception('line {}: {}'.format(reader.line_num, e))

    return data

  def parse_path(self, filename):
    data = []
    with open(filename) as f:
      reader = csv.reader(f, lineterminator='\n')
      try:
        for row in reader:
          data.append(row)
      except csv.Error as e:
        raise Exception(
            'file {}, line {}: {}'.format(filename, reader.line_num, e))

    return data
