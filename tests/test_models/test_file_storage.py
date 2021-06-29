#!/usr/bin/python3
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        if os.path.isfile('my_file.json'):
            os.rename('my_file.json', 'tmp_file.json')
        self.storage1 = FileStorage()
        self.model1 = BaseModel()

    def tearDown(self):
        if os.path.isfile('my_file.json'):
            os.remove('my_file.json')
        if os.path.isfile('tmp_file.json'):
            os.rename('tmp_file.json', 'my_file.json')
        del self.storage1
        del self.model1

    def test_attributes(self):
        self.assertEqual(self.storage1._FileStorage__file_path, 'my_file.json')
        self.assertIsInstance(self.storage1._FileStorage__objects, dict)

    def test_all(self):
        """ tests both all and new """
        my_dict = self.storage1.all()
        my_id = 'BaseModel.' + self.model1.id
        self.assertIsInstance(my_dict, dict)
        self.assertIn(my_id, my_dict)

    def test_reload(self):
        self.model1.save()
        self.assertTrue(os.path.isfile('my_file.json'))
        tmp_obj = BaseModel()
        tmp_id = 'BaseModel.' + tmp_obj.id
        tmp_obj.save()
        del self.storage1._FileStorage__objects[tmp_id]
        self.storage1.reload()
        self.assertIn(tmp_id, self.storage1.all())
