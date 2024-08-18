import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
        self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'] )/ 2) )

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
        self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'] )/ 2) )


  """ ------------ Add more unit tests ------------ """
  def test_getRatio_priceA_equals_zero(self):
      prices = {}
      quote1 = {'top_ask': {'price': 0, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 0, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'}
      quote2 = {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
      stock1, bid_price1, ask_price1, price1 = getDataPoint(quote1)
      stock2, bid_price2, ask_price2, price2 = getDataPoint(quote2)
      prices[stock1] = price1
      prices[stock2] = price2
      self.assertEqual(getRatio(prices[stock1], prices[stock2]), 0)
     
  def test_getRatio_priceB_equalsZero(self):
      prices = {}
      quote1 = {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'}
      quote2 = {'top_ask': {'price': 0, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 0, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
      stock1, bid_price1, ask_price1, price1 = getDataPoint(quote1)
      stock2, bid_price2, ask_price2, price2 = getDataPoint(quote2)
      prices[stock1] = price1
      prices[stock2] = price2
      self.assertEqual(getRatio(prices[stock1], prices[stock2]), None)
      
  def test_getRatio_priceA_EqualsPriceB(self):
      prices = {}
      quote1 = {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'}
      quote2 = {'top_ask': {'price': 121.2, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
      stock1, bid_price1, ask_price1, price1 = getDataPoint(quote1)
      stock2, bid_price2, ask_price2, price2 = getDataPoint(quote2)
      prices[stock1] = price1
      prices[stock2] = price2
      self.assertEqual(getRatio(prices[stock1], prices[stock2]), 1)
      

      
  def test_getRatio_priceA_GreaterThanPriceB(self):
      prices = {}
      quote1 = {'top_ask': {'price': 122.56, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 118.6, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'}
      quote2 = {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
      stock1, bid_price1, ask_price1, price1 = getDataPoint(quote1)
      stock2, bid_price2, ask_price2, price2 = getDataPoint(quote2)
      prices[stock1] = price1
      prices[stock2] = price2
      self.assertGreater(getRatio(prices[stock1], prices[stock2]), 1)
      
  def test_getRatio_priceB_GreaterThanPriceA(self):
      prices = {}
      quote1 = {'top_ask': {'price': 122.56, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 118.6, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'}
      quote2 = {'top_ask': {'price': 123.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 124.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
      stock1, bid_price1, ask_price1, price1 = getDataPoint(quote1)
      stock2, bid_price2, ask_price2, price2 = getDataPoint(quote2)
      prices[stock1] = price1
      prices[stock2] = price2
      self.assertLess(getRatio(prices[stock1], prices[stock2]), 1)
      
      
      
      
       


if __name__ == '__main__':
    unittest.main()
