'''
Created on Jul 14, 2012

@author: jgoppert
'''
import unittest

from datcom2modelica import Convert


class TestConvert(unittest.TestCase):

    infile = 'test/data/Citation.out'

    def test_convert(self):
        c = Convert(self.infile, "test/data/modelica_test")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
