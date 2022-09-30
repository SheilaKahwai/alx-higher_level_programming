#!/usr/bin/python3
"""Module Test_Rectangle
Unittests to perform on the Rectangle class
"""


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('Rectangle setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('Rectangle tearDownClass')

    def setUp(self):
        print('setUp')

    def tearDown(self):
        print('tearDown')

    def test_instance_id(self):
        self.assertEqual(Rectangle(10, 2).id, 1)
        self.assertEqual(Rectangle(10, 2, 0, 0, 12).id, 12)

    def test_width_height_setters(self):
        x = Rectangle()
        self.assertRaises()
        x = Rectangle(10)
        self.assertRaises()
        x = Rectangle([9, 2])
        self.assertRaises(TypeError)
        x = Rectangle('2', 8)
        self.assertRaises(TypeError)
        x = Rectangle(-9, 2)
        self.assertRaises(ValueError)
        x = Rectangle(8, -8)
        self.assertRaises(ValueError)
        x = Rectangle(78, None)
        self.assertRaises()
        x = Rectangle(8, '3')
        self.assertRaises(TypeError)
        x = Rectangle(7, 9)
        self.assertTrue(isinstance(x, Rectangle))
        x = Rectangle(None, 89)
        self.assertRaises()
        x = Rectangle(8.9, 9)
        self.assertRaises(TypeError)
        x = Rectangle(8, 9.2)
        self.assertRaises(TypeError)
        x = Rectangle(0, 9)
        self.assertRaises(ValueError)

    def test_x_y(self):
        obj = Rectangle(10, 9, '8', 0)
        self.assertRaises(TypeError)
        obj = Rectangle(10, 9, [8, 7])
        self.assertRaises(TypeError)
        obj = Rectangle(10, 9, -9)
        self.assertRaises(ValueError)
        obj = Rectangle(10, 9, 8.9, 0)
        self.assertRaises(TypeError)
        obj = Rectangle(10, 9, 7, 7.3)
        self.assertRaises(TypeError)
        obj = Rectangle(10, 9, 0, -7)
        self.assertRaises(ValueError)
        obj = Rectangle(10, 9, 7, '7')
        self.assertRaises(TypeError)
        obj = Rectangle(10, 9,  , 6)
        self.assertRaises()
        obj = Rectangle(10, 9, None)
        self.assertRaises()
        obj = Rectangle(10, 9, 7, None)
        self.assertRaises()
        obj = Rectangle(10, 9, 7, 2)
        self.assertTrue(isinstance(obj, Rectangle))

    def test_area(self):
        self.assertEqual(Rectangle(3, 2).area(), 6)
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)
    
    def test_display(self):
        self.assertEqual(Rectangle(4, 6).display(), ####
                                                    ####
                                                    ####
                                                    ####
                                                    ####
                                                    ####
                                                    )
        self.assertEqual(Rectangle(2, 3, 1, 2).display(), 
                                                          
                                                           ##
                                                           ##
                                                           ##
                                                           )
    def test_str(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(print(r1), "[Rectangle] (12) 2/1 - 4/6")
        r1 = Rectangle(5, 5, 1)
        self.assertEqual(print(r1), "[Rectangle] (1) 1/0 - 5/5")
        r1 = Rectangle(9, 8)
        self.assertEqual(print(r1), "[Rectangle] (1) 0/0 - 9/8")

    def test_update(self):
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(print(r1.update(89)), "[Rectangle] (89) 10/10 - 10/10")
        self.assertEqual(print(r1.update(89, 2)), "[Rectangle] (89) 10/10 - 2/10")
        self.assertEqual(print(r1.update(89, 2, 3)), "[Rectangle] (89) 10/10 - 2/3")
        self.assertEqual(print(r1.update(89, 2, 3, 4)), "[Rectangle] (89) 4/10 - 2/3")
        self.assertEqual(print(r1.update(89, 2, 3, 4, 5)), "[Rectangle] (89) 4/5 - 2/3")
        self.assertEqual(print(r1.update(height=1)), "[Rectangle] (1) 10/10 - 10/1")
        self.assertEqual(print(r1.update(width=1, x=2)), "[Rectangle] (1) 2/10 - 1/1")
        self.assertEqual(print(r1.update(y=1, width=2, x=3, id=89)), "[Rectangle] (89) 3/1 - 2/1")
        self.assertEqual(print(r1.update(x=1, height=2, y=3, width=4)), "[Rectangle] (89) 1/3 - 4/2")
        self.assertEqual(print(r1.update(23, 3, 4, y=1, width=2, x=3, id=89)), "[Rectangle] (23) 10/10 - 3/4")
