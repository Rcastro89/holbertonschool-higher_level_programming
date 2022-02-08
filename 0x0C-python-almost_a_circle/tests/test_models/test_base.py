#!/usr/bin/python3
"""test"""
import unittest
import os

from models.base import Base
from models.rectangle import Rectangle


class TestBaseClass(unittest.TestCase):
    """ ok"""
    def setUp(self):
        """ Hook that runs before each unit test"""
        Base._Base__nb_objects = 0

    # def test_module_docstring(self):

    def test_class_docstring(self):
        """ ok"""
        self.assertIsNotNone(Base.__doc__)

    # def test_methods_docstring(self):

    def test_initialization_with_empty_id(self):
        """ ok"""
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)


    def test_initialization_with_non_empty_id(self):
        """ ok"""
        self.assertTrue(Base(42), 42)


    def test_init_of_two_instances(self):
        """ ok"""
        b1 = Base(42)
        b2 = Base()
        self.assertTrue(b1.id == 42)
        self.assertTrue(b2.id == 1)


    def test_init_of_tree_instances(self):
        """ ok"""
        b1 = Base()
        b2 = Base(42)
        b3 = Base()
        self.assertTrue(b1.id == 1)
        self.assertTrue(b2.id == 42)
        self.assertTrue(b3.id == 2)

if __name__ == '__main__':
    unittest.main()
