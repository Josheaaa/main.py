import unittest
from main import CountryStatistics


class AsiaTest(unittest.TestCase):

    def testMYVisitors(self):
        visitors = CountryStatistics()
        result = CountryStatistics.getChina2002Visitors(visitors)
        self.assertEqual(result, 600595)
