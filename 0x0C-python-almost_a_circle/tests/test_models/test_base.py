#!/usr/bin/python3
"""Test_Base Module
Perform unittests on our Base class.
"""


import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Base setUpClass")

    @classmethod
    def tearDownClass(cls):
        print("Base tearDownClass")

    def setUp(self):
        self.obj1 = Base()
        self.obj2 = Base()
        self.obj3 = Base(9)
        self.obj4 = Base()
        print("Base setUp")

    def tearDown(self):
        del self.obj1
        del self.obj2
        del self.obj3
        del self.obj4
        print("Base tearDown")

    def test_instance_id(self):
        self.assertEqual(self.obj1.id, 1)
        self.assertEqual(self.obj2.id, 2)
        self.assertEqual(self.obj3.id, 9)
        self.assertEqual(self.obj4.id, 3)
        self.assertEqual(Base("Betty").id, "Betty")
        self.assertEqual(Base([1, 2, 3]).id, [1, 2, 3])
        self.assertEqual(Base({"id": 89}).id, {"id": 89})
        self.assertEqual(Base((7,)).id, (7,))
