#!/usr/bin/python3
"""
    Contains the tests for the FileStorage class
"""
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os


class TestFileStorage(unittest.TestCase):
    """Definition of test class for class FileStorage"""
    def setUp(self):
        """Sets up the resources required to run tests"""
        if os.path.isfile('my_file.json'):
            os.rename('my_file.json', 'tmp_file.json')
        self.model1 = BaseModel()

    def tearDown(self):
        """Tears down the resources that have been used to run tests"""
        if os.path.isfile('my_file.json'):
            os.remove('my_file.json')
        if os.path.isfile('tmp_file.json'):
            os.rename('tmp_file.json', 'my_file.json')
        del self.model1

    def test_attributes_exist(self):
        """Test that FileStorage class has required attributes and methods"""
        self.assertTrue(hasattr(FileStorage, '_FileStorage__objects'))
        self.assertTrue(hasattr(FileStorage, '_FileStorage__file_path'))
        self.assertTrue(hasattr(FileStorage, 'all'))
        self.assertTrue(hasattr(FileStorage, 'new'))
        self.assertTrue(hasattr(FileStorage, 'save'))
        self.assertTrue(hasattr(FileStorage, 'reload'))

    def test_attributes(self):
        """Test whether the type of FileStorage class attributes is correct"""
        self.assertEqual(storage._FileStorage__file_path, 'my_file.json')
        self.assertIsInstance(storage._FileStorage__objects, dict)

    def test_all(self):
        """Test that the all method returns the correct dictionary"""
        my_dict = storage.all()
        my_id = 'BaseModel.' + self.model1.id
        self.assertIsInstance(my_dict, dict)
        self.assertIn(my_id, my_dict)

    def test_reload(self):
        """Test that the reload method actually reloads objects from file"""
        self.model1.save()
        self.assertTrue(os.path.isfile('my_file.json'))
        tmp_obj = BaseModel()
        tmp_id = 'BaseModel.' + tmp_obj.id
        tmp_obj.save()
        del storage._FileStorage__objects[tmp_id]
        storage.reload()
        self.assertIn(tmp_id, storage.all())
