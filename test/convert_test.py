'''
Created on Jul 14, 2012

@author: jgoppert
'''
import unittest

from datcom2modelica import Convert


class TestConvert(unittest.TestCase):

    infile = 'test/data/Citation.out'

    def test_convert(self):
        # XXX this test should be alphabetically first XXX
        Convert(self.infile, "test/data/modelica_test")

    def test_integrity(self):
        # XXX this test will fail if it's alphabetically before convert XXX
        expected = open("test/data/modelica_expected.mo", 'rb').readlines()
        test = open("test/data/modelica_test.mo", 'rb').readlines()
        for e_line, t_line in zip(expected, test):
            self.assertEqual(e_line, t_line)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
