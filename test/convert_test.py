'''
Created on Jul 14, 2012

@author: jgoppert
'''
import unittest

from datcom2modelica import Convert


class TestConvert(unittest.TestCase):

    infile = 'data/Citation.out'

    def test_convert(self):
        c = Convert(self.infile, "modelica_test")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
