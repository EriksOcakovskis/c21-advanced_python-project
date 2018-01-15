# Used for Python2 to make strings unicode
from __future__ import unicode_literals
# Used for Python2 to make print() work
from __future__ import print_function
# Used for Python2 to make imports call standar library first
from __future__ import absolute_import
# Enables non-truncating division (dividing two integers results in a float.)
from __future__ import division

# makes new-style classes in Python 2.
__metaclass__ = type


class BusinessLogic(object):
  """
  Provides funcrions to find
  What was the greatest percent increase over the previous day, and what day was it?
  What was the greatest percent decrease over the previous day, and what day was it?
  What is the highest price in the the data, and what day was it?
  """

  def __greatest_change(self, btc_data, func):
    biggest_change = 0
    day_of_biggest_change = None

    for index, data_point in enumerate(btc_data[1:]):
        data_point_previous = btc_data[index]
        price_current = float(data_point[1])
        price_previous = float(data_point_previous[1])

        change = price_current - price_previous
        change = (change / price_previous) * 100

        if func(change, biggest_change):
            biggest_change = change
            day_of_biggest_change = data_point[0]

    return(day_of_biggest_change, biggest_change)

  def greatest_increase(self, btc_data):
    gi = self.__greatest_change(btc_data, lambda x, y: x > y)
    return gi

  def greatest_decrease(self, btc_data):
    gd = self.__greatest_change(btc_data, lambda x, y: x < y)
    return gd

  def highest_price(self, btc_data):
    biggest_price = 0
    day_of_biggest_price = None

    for date, price in btc_data:
        price = float(price)
        if price > biggest_price:
          biggest_price = price
          day_of_biggest_price = date

    return(day_of_biggest_price, biggest_price)
