#!/usr/bin/python3
""" a module that tests base model """

import unittest
import time
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_Initialisation(self):
        """ testing __init__ method of basemodel """
        testModel = BaseModel()
        # id
        id1 = testModel.id
        id2 = testModel.id
        self.assertEqual(id1, id2)
        # created_at
        created_at1 = testModel.created_at
        time.sleep(1)
        created_at2 = testModel.created_at
        self.assertEqual(created_at1, created_at1)
        testModel.name = 'changed'
        self.assertLess(created_at1, created_at2)
        self.assertEqual(created_at1, created_at1)
        # updated_at
        updated_at1 = testModel.updated_at
        time.sleep(1)
        updated_at2 = testModel.updated_at
        self.assertEqual(updated_at1, updated_at1)
        testModel.name = 'changed'
        self.assertLess(updated_at1, updated_at2)
        self.assertEqual(updated_at1, updated_at1)
