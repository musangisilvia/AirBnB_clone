#!/usr/bin/python3
"""
    This is the entry point of the command interpreter.
"""

import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """
        HBNBCommand implements the Cmd class.
        It is a command  interpreter for the AirBnB project.
    """
    prompt = '(hbnb) '

    def do_create(self, line):
        """
            Creates a new instance of BaseModel, saves it to the JSON file
            prints the id.
            Usage: create <ClassName>
        """

        cmds = line.split()

        if len(cmds) is 0:
            print("** class name missing **")
            return

        if cmds[0] != "BaseModel":
            print("** class doesn't exist **")
            return

        newModel = BaseModel()
        newModel.save()
        print(newModel.id)

    def do_show(self, line):
        """
            Prints the string representation of an instance based
            on the class name and id.
            Usage: show <ClassName> <id>
        """

        cmds = line.split()

        if len(cmds) == 0:
            print("** class name missing **")
            return

        if len(cmds) == 1:
            print("** instance id missing **")
            return

        storage = FileStorage()
        storage.reload()
        obj = storage.all()

        try:
            cmds[0]
        except NameError:
            print("** class doesn't exist **")
            return

        key = cmds[0] + "." + cmds[1]

        try:
            value = obj[key]
            print(value)
        except KeyError:
            print("** no instance found **")

    def emptyline(self):
        """
            Called when emptyline is entered in response to the prompt.
            Overrides the superclass function.
        """
        pass

    def do_quit(self, line):
        """
            Exit
        """
        return True

    def do_EOF(self, line):
        """
            Exit
        """
        return True

# Help functions

    def help_create(self):
        print("Creates a new instance of BaseModel and saves \
it.\nUsage: create <ClassName>")

    def help_show(self):
        print("Prints the string representation of an instance \
based on the class name and id.\nUsage: show <ClassName> <id>.")

    def help_quit(self):
        print("Exit the command line.\nUsage: quit")

    def help_EOF(self):
        print("Exit the command line")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
