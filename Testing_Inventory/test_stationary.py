# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 15:59:17 2019

@author: Ritayu_Nagpal
"""

import unittest
import LibraryManagement.Inventory.stationary as statn

class TestStationary(unittest.TestCase):
    def setUp(self):
        self.pen1 = statn.Pen("Blue", "gel","uniball",1.20,20)
        self.pen2 = statn.Pen("Red", "ball","reynolds",1.10,10)
        self.pencil1 = statn.Pencil("Green", "HB", 0.5, "Camlin", 0.25, 25)
        self.pencil2 = statn.Pencil("Black", "Click", 0.7, "BIC", 1.00, 15)
        self.notebook1 = statn.Notebook("A4", 150, "Classmate", 4.90, 10)
        self.notebook2 = statn.Notebook("A3", 100, "Artik", 3.90, 20)
        #wrong cases
        self.pen3 = statn.Pen("Blue", "gel","uniball",1.20,20.2)
        self.pen4 = statn.Pen("Red", "ball","reynolds",1.10,-11)
        self.pencil3 = statn.Pencil("Green", "HB", 0.5, "Camlin", 0.25, -5)
        self.pencil4 = statn.Pencil("Black", "Click", 0.7, "BIC", 1.00, "abc")
        self.notebook3 = statn.Notebook("A4", 150, "Classmate", 4.90, True)
        self.notebook4 = statn.Notebook("A3", 100, "Artik", 3.90, -15)
        
        
    def test_validate(self):
        self.assertIsNone(self.pen3.validate_object())
        self.assertIsNone(self.pen4.validate_object())
        self.assertIsNone(self.pencil3.validate_object())
        self.assertIsNone(self.pencil4.validate_object())
        self.assertIsNone(self.notebook3.validate_object())
        self.assertIsNone(self.notebook4.validate_object())
        
    def test_sold(self):
        self.pen1.sold(5)
        self.assertEqual(self.pen1.quantity,15)
        self.assertEqual(self.pen2.sold(40),"Not Enough Quantity Available")
        self.assertEqual(self.pen1.sold("a"),"Enter an integer value for quantity sold.")
        
        self.pencil1.sold(15)
        self.assertEqual(self.pencil1.quantity,10)
        self.assertEqual(self.pencil2.sold(40),"Not Enough Quantity Available")
        self.assertEqual(self.pencil1.sold(-2),"Enter a positive integer number for quantity sold.")
        
        self.notebook1.sold(10)
        self.assertEqual(self.notebook1.quantity,0)
        self.assertEqual(self.notebook1.sold(6),"Not Enough Quantity Available")
        self.assertEqual(self.notebook2.sold(40),"Not Enough Quantity Available")
        
    def test_purchase_cost(self):
        self.assertEqual(self.pen1.purchase_cost(5), 6)
        self.assertEqual(self.pen2.purchase_cost(10), 11)
        
        self.assertEqual(self.pencil1.purchase_cost(10), 2.5)
        self.assertEqual(self.pencil2.purchase_cost(10), 10)
        self.assertEqual(self.pencil2.purchase_cost(2.1),"Enter an integer value to check purchasing cost.")
        
        self.assertEqual(self.notebook1.purchase_cost(10), 49)
        self.assertEqual(self.notebook2.purchase_cost(20), 78)
        self.assertEqual(self.notebook2.purchase_cost(-5), "Enter a positive integer number for checking purchasing cost.")
        
        
    def test_returned(self):
        self.pen1.returned(5)
        self.pen2.returned(10)
        self.assertEqual(self.pen1.quantity, 25)
        self.assertEqual(self.pen2.quantity, 20)
        self.assertEqual(self.pen1.returned(-5), "Enter a positive integer number for returned quantity.")
        
        self.pencil1.returned(0)
        self.pencil2.returned(100)
        self.assertEqual(self.pencil1.quantity, 25)
        self.assertEqual(self.pencil2.quantity, 115)
        
        self.notebook1.returned(1)
        self.notebook2.returned(2)
        self.assertEqual(self.notebook1.quantity, 11)
        self.assertEqual(self.notebook2.quantity, 22)
        self.assertEqual(self.notebook1.returned("abc"), "Enter an integer value for returned quantity.")
        
    def test_add(self):
        self.pen1.add(15)
        self.pen2.add(5)
        self.assertEqual(self.pen1.quantity, 35)
        self.assertEqual(self.pen2.quantity, 15)
        
        self.pencil1.add(0)
        self.pencil2.add(10)
        self.assertEqual(self.pencil1.quantity, 25)
        self.assertEqual(self.pencil2.quantity, 25)
        self.assertEqual(self.pencil2.add(-10), "Enter a positive integer number for quantity added to Inventory.")
        
        self.notebook1.add(4)
        self.notebook2.add(12)
        self.assertEqual(self.notebook1.quantity, 14)
        self.assertEqual(self.notebook2.quantity, 32)
        self.assertEqual(self.notebook1.add(23.12), "Enter an integer value for quantity added to Inventory.")
        
    def test_display_details(self):
        self.assertEqual(self.pen1.display_details(), "Pen Color:Blue    Pen Type:gel    Pen Brand:uniball    Pen Price:1.2")
        self.assertEqual(self.pen2.display_details(), "Pen Color:Red    Pen Type:ball    Pen Brand:reynolds    Pen Price:1.1")
        
        self.assertEqual(self.pencil1.display_details(), "Pencil Color:Green    Pencil Type:HB    Pencil Thickness:0.5    Pencil Brand:Camlin    Pencil Price:0.25")
        self.assertEqual(self.pencil2.display_details(), "Pencil Color:Black    Pencil Type:Click    Pencil Thickness:0.7    Pencil Brand:BIC    Pencil Price:1.0")
        
        self.assertEqual(self.notebook1.display_details(), "Page SizeA4    Number of Pages:150    Notebook Brand:Classmate    Notebook Price:4.9")
        self.assertEqual(self.notebook2.display_details(), "Page SizeA3    Number of Pages:100    Notebook Brand:Artik    Notebook Price:3.9")
        
unittest.main(argv=[''], verbosity = 2, exit = False)
