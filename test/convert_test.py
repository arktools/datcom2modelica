# Copyright 2012 Lenna X. Peterson (github.com/lennax)
# All rights reserved
# License: GPL v3
# This program comes with ABSOLUTELY NO WARRANTY. This is free software
# and you are welcome to distribute it under certain conditions.
# For details, see license.txt

import unittest
import os

from datcom2modelica import Convert


class TestConvert(unittest.TestCase):

    def setUp(self):
        self.path = os.path.abspath(os.path.dirname(__file__))
        print self.path

    def test_convert(self):

        filenames=['B-737']
        
        print "current directory: ", os.path.abspath(os.path.curdir)
        
        for filename in filenames:
            
            input_path=os.path.join(self.path, 'input', filename+'.out')
            output_path=os.path.join(self.path, 'output', filename+'.mo')
            interface_path=os.path.join(self.path, 'output')
            
                        
            print "checking file:", input_path
            
            Convert.from_argv(['', input_path, output_path, '-i'+ interface_path])
            
            expected_path=os.path.join(self.path, 'expected', filename+'.mo')
            
            with open(output_path, 'rb') as output_file:
                output = output_file.readlines()
                
            with open(expected_path, 'rb') as expected_file:
                expected = expected_file.readlines()
                
            for i in xrange(len(expected)):
                if output[i] != expected[i]:
                    raise Exception(output_path+": line " +str(i+1) +" does not match " + expected_path)

if __name__ == "__main__":
    unittest.main()
