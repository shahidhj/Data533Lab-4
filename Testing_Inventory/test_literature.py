# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 13:27:15 2019

@author: Ritayu_Nagpal
"""

import unittest
import LibraryManagement.Inventory.literature as lit

class TestLiterature(unittest.TestCase):
    def setUp(self):
        self.book1 = lit.Book("Data Science Book", "Alex", "Science", 99.99, 181, 1100110101, 2016, 8)
        self.book2 = lit.Book("Ultimate CheatBook", "Zach", "Technology", 59.99, 100, 1010110101, 2019, 2)
        self.periodical1 = lit.Periodical("Athlon Sports", "John Coon", "Sports", 14.99, 10110110, 2019_04, 5)
        self.periodical2 = lit.Periodical("Chop Chop", "Sally Sampson", "Cookery", 10.99, 10111110, 2019_11, 1)
        # wrongly created instances
        self.book3 = lit.Book("Data Science Book", "Alex", "Science", 99.99, 181, 1100110101, 2016, -8)
        self.book4 = lit.Book("Ultimate CheatBook", "Zach", "Technology", 59.99, 100, 1010110101, 2019, "a")
        self.periodical3 = lit.Periodical("Athlon Sports", "John Coon", "Sports", 14.99, 10110110, 2019_04, 0)
        self.periodical4 = lit.Periodical("Chop Chop", "Sally Sampson", "Cookery", 10.99, 10111110, 2019_11, 3.2)
        
        
    def test_validate(self):
        self.assertIsNone(self.book3.validate_object())
        self.assertIsNone(self.book4.validate_object())
        self.assertIsNone(self.periodical3.validate_object())
        self.assertIsNone(self.periodical4.validate_object())
        
        
    def test_issued(self):
        self.book1.issued()
        self.book2.issued()
        self.assertEqual(self.book1.copies,7)
        self.assertEqual(self.book2.copies,1)
        self.book2.issued()
        self.assertEqual(self.book2.issued(),"Book not available in library")
        self.book1.update_status("Discontinued")
        self.assertEqual(self.book1.issued(),"Book is discontinued")
        
        self.periodical1.issued()
        self.periodical2.issued()
        self.assertEqual(self.periodical1.copies,4)
        self.assertEqual(self.periodical2.copies,0)
        self.assertEqual(self.periodical2.issued(),"Periodical not available in Library")
        self.periodical1.update_status("Discontinued")
        self.assertEqual(self.periodical1.issued(),"Periodical is discontinued")
        
    def test_returned(self):
        self.book1.returned()
        self.book2.issued()
        self.book2.issued()
        self.assertEqual(self.book2.availability,"No")
        self.book2.returned()
        self.assertEqual(self.book1.copies,9)
        self.assertEqual(self.book2.copies,1)
        self.assertEqual(self.book1.availability,"Yes")
        self.assertEqual(self.book2.availability,"Yes")
        
        self.periodical1.returned()
        self.periodical2.issued()
        self.assertEqual(self.periodical2.availability,"No")
        self.periodical2.returned()
        self.assertEqual(self.periodical1.copies,6)
        self.assertEqual(self.periodical2.copies,1)
        self.assertEqual(self.periodical1.availability,"Yes")
        self.assertEqual(self.periodical2.availability,"Yes")
        
    def test_get_status(self):
        self.assertEqual(self.book1.get_status(),"Available")
        self.book2.issued()
        self.book2.issued()
        self.assertEqual(self.book2.get_status(),"Not Available")
        self.book1.update_status("Discontinued")
        self.assertEqual(self.book1.get_status(),"Discontinued")
        
        self.assertEqual(self.periodical1.get_status(),"Available")
        self.periodical2.issued()
        self.assertEqual(self.periodical2.get_status(),"Not Available")
        self.periodical1.update_status("Discontinued")
        self.assertEqual(self.periodical1.get_status(),"Discontinued")
        
    def test_update_status(self):
        self.book1.update_status("Yes")
        self.assertEqual(self.book1.availability,"Yes")
        self.assertEqual(self.book1.update_status("discontinue"),"Book Status Not Updated")
        
        self.periodical1.update_status("Yes")
        self.assertEqual(self.periodical2.availability,"Yes")
        self.assertEqual(self.periodical2.update_status("discontinue"),"Periodical Status Not Updated")
        
    def test_display_details(self):
        self.assertEqual(self.book1.display_details(), "Title:Data Science Book    Author:Alex    Book Title:Data Science Book    Book Author:Alex    Book Genre:Science    Book Year:2016    Number of Pages:181    Copies Available:8")
        self.assertEqual(self.periodical2.display_details(), "Title:Chop Chop    Author:Sally Sampson    Category:Cookery    Edition:201911    Copies Available:1")
                
        
unittest.main(argv=[''], verbosity = 2, exit = False)