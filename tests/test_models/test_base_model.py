#!/usr/bin/python3
import unittest
import pep8
import os
from models.__init__ import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestModels(unittest.TestCase):

    def setUp(self):
        """ Set a variable """
        self.my_model = BaseModel()
        self.my_model.my_number = 55
        print("setUp")

    def tearDown(self):
        """ End variable """
        print("tearDown")

    @classmethod
    def setUpClass(cls):
        """ Set a Class """
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        """ Del a Class"""
        print("tearDownClass")

    def test_models_doc(self):
        """ Check the documentation """
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_models_name(self):
        """ Check if name is create"""
        self.my_model.name = 'Holberton'
        self.assertEqual(self.my_model.name, 'Holberton')

    def test_models_number(self):
        """ Check if the number is create """
        self.assertEqual(self.my_model.my_number, 55)

    def test_models_exist(self):
        """ Check if the json file and methods exists """
        self.my_model.save()
        self.assertTrue(os.path.isfile('file.json'))
        self.assertTrue(hasattr(self.my_model, "__init__"))
        self.assertTrue(hasattr(self.my_model, "__str__"))
        self.assertTrue(hasattr(self.my_model, "save"))
        self.assertTrue(hasattr(self.my_model, "to_dict"))

    def test_models_not_empty(self):
        """ Check if the json file is not empty """
        self.assertTrue('file.json')

    def test_models_save(self):
        """ Check if the save function works """
        a = self.my_model.updated_at()
        self.my_model.save()
        self.assertNotEqual(a, self.my_model.update_at)
        self.assertNotEqual(self.my_model.created_at,
                            self.my_model.updated_at)

    def test_models_instance(self):
        """ check if user_1 is instance of User """
        self.assertIsInstance(self.my_model, BaseModel)

    def test_models_to_dict(self):
        model_1 = self.my_model.to_dict()
        self.assertIsInstance(model_1["created_at"], str)
        self.assertIsInstance(model_1["updated_at"], str)
        self.assertIsInstance(model_1["my_number"], int)
        self.assertIsInstance(model_1["id"], str)

if __name__ == '__main__':
    unittest.main()
