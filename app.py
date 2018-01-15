# Used for Python2 to make strings unicode
from __future__ import unicode_literals
# Used for Python2 to make print() work
from __future__ import print_function
# Used for Python2 to make imports call standar library first
from __future__ import absolute_import
# Enables non-truncating division (dividing two integers results in a float.)
from __future__ import division

# Imports
import sys
from my_parsers import MyParsers
from business_logic import BusinessLogic
from datetime import datetime


def main():
  try:
    mp = MyParsers()
    args = mp.parse_args()

    if args.url:
      btc_data = mp.parse_url(args.url)
    else:
      btc_data = mp.parse_path(args.path)

    bl = BusinessLogic()
    gi = bl.greatest_increase(btc_data)
    gd = bl.greatest_decrease(btc_data)
    hp = bl.highest_price(btc_data)

    print('Greatest percent increase over the previous day was {0:.1f}% on {1:.10}'
          .format(gi[1], gi[0]))
    print('Greatest percent decrease over the previous day was {0:.1f}% on {1:.10}'
          .format(gd[1], gd[0]))
    print('Highest price was {0:.3f} on {1:.10}'.format(hp[1], gd[0]))

  except Exception as e:
    sys.exit('{0}: {1}'.format(datetime.today(), e))


if __name__ == '__main__':
  main()
