#!/usr/bin/python3
"""
    Contains the tests for class HBNBCommand
"""
import sys
import os
import unittest
from models import storage
from models.base_model import BaseModel
from io import StringIO
from console import HBNBCommand
from unittest.mock import patch

def setUpModule():
    """Set up resources to be used in the test module"""
    if os.path.isfile("my_file.json"):
        os.rename("my_file.json", "tmp.json")

def tearDownModule():
    """Tear down resources used in the test module"""
    if os.path.isfile("my_file.json"):
        os.remove("my_file.json")
    if os.path.isfile("tmp.json"):
        os.rename("tmp.json", "my_file.json")


class TestHBNBCommand(unittest.TestCase):
    """Tests for the HBNBCommand prompt"""

    def test_HBNBCommand_prompt(self):
        """Test the HBNBCommand prompt"""
        self.assertEqual(HBNBCommand.prompt, '(hbnb) ')

class TestHBNBCommand_create(unittest.TestCase):
    """Test the HBNBCommand create command"""

    def test_HBNBCommand_create_error_messages(self):
        """Test that the create comand prints the correct error messages"""
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd('create'))
            self.assertEqual("** class name missing **", f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd('create MyModel'))
            self.assertEqual("** class doesn't exist **", f.getvalue().strip())

    def test_HBNBCommand_create_new_instances(self):
        """Test the creation of new instances of different classes"""

        Mm = ['BaseModel', 'User', 'Place', 'City', 'State', 'Review', 'Amenity']
        for m in Mm:
            with patch('sys.stdout', new=StringIO()) as f:
                self.assertFalse(HBNBCommand().onecmd('create {}'.format(m)))
                new_key = m + "." + f.getvalue().strip()
                self.assertIn(new_key, storage.all().keys())


class TestHBNBCommand_show(unittest.TestCase):
    """Test the HBNBCommand show command"""

    def test_HBNBCommand_show_error_messages(self):
        """Test that the show comand prints the correct error messages"""

        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd('show'))
            self.assertEqual("** class name missing **", f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd('show MyModel'))
            self.assertEqual("** class doesn't exist **", f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd('show BaseModel'))
            self.assertEqual("** instance id missing **", f.getvalue().strip())

        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd('show BaseModel 12234321'))
            self.assertEqual("** no instance found **", f.getvalue().strip())

    def test_HBNBCommand_show_existing_instance(self):
        """Test the creation of new instances of different classes"""
        objs = storage.all()
        for key, value in objs.items():
            inst = key.split(".")
            value_str = str(value)
            with patch('sys.stdout', new=StringIO()) as f:
                self.assertFalse(HBNBCommand().
                                 onecmd('show {} {}'.format(inst[0], inst[1])))
                self.assertEqual(value_str, f.getvalue().strip())

class TestHBNBCommand_all(unittest.TestCase):
    """Test the HBNBCommand all command"""

    def test_HBNBCommand_all_error_messages(self):
        """Test that the all comand prints the correct error messages"""

        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(HBNBCommand().onecmd('all MyModel'))
            self.assertEqual("** class doesn't exist **", f.getvalue().strip())

    def test_HBNBCommand_all_existing_instances(self):
        """Test the creation of new instances of different classes"""
        objs = storage.all()
        for key, value in objs.items():
            inst_key = key.split(".")[1]
            with patch('sys.stdout', new=StringIO()) as f:
                self.assertFalse(HBNBCommand().onecmd('all'))
                self.assertIn(inst_key, f.getvalue().strip())

if __name__ == '__main__':
    unittest.main()
