# -*- coding: utf-8 -*-
# (C) 2015 Muthiah Annamalai
#  
# This file is part of 'open-tamil' package tests
# 

# setup the paths
from opentamiltests import *
import tamil

class VersionTester(unittest.TestCase):
    def test_version(self):        
        print ( dir(tamil) )
        self.assertEqual(tamil.VERSION,'0.4')

if __name__ == '__main__':    
    unittest.main()

