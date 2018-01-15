from business_logic import BusinessLogic

test_values = [['2017-01-11 00:00:00', '9.0'], ['2017-01-12 00:00:00', '13.5'],
               ['2017-01-13 00:00:00', '13.0'], ['2017-01-14 00:00:00', '14.0'],
               ['2017-01-15 00:00:00', '15.0'], ['2017-01-16 00:00:00', '7.5']]

bl = BusinessLogic()


def test_greatest_increase():
  r = bl.greatest_increase(test_values)
  assert r[1] == 50
  assert r[0] == '2017-01-12 00:00:00'


def test_greatest_decrease():
  r = bl.greatest_decrease(test_values)
  assert r[1] == -50
  assert r[0] == '2017-01-16 00:00:00'


def test_highest_price():
  r = bl.highest_price(test_values)
  assert r[1] == 15
  assert r[0] == '2017-01-15 00:00:00'
