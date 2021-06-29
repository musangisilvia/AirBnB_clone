#!/usr/bin/python3
"""
    This is the entry point of the command interpreter.
"""

import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.review import Review


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

        try:
            eval(cmds[0])
        except NameError:
            print("** class doesn't exist **")
            return

        newModel = eval(cmds[0])()
        print(newModel.id)
        newModel.save()

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
        try:
            eval(cmds[0])
        except NameError:
            print("** class doesn't exist **")
            return

        if len(cmds) == 1:
            print("** instance id missing **")
            return

#        storage = FileStorage()
        models.storage.reload()
        obj = models.storage.all()
        key = cmds[0] + "." + cmds[1]

        try:
            value = obj[key]
            print(value)
        except KeyError:
            print("** no instance found **")

    def do_all(self, line):
        """
            Prints all string representation of all instances based
            on or not on the class name
            Usage: all <ClassName> or all
        """
        obj_list = []
#        storage = FileStorage()
        models.storage.reload()
        objs = models.storage.all()

        try:
            if len(line) != 0:
                eval(line)
            else:
                pass
        except NameError:
            print("** class doesn't exist **")
            return

        line.strip()
        for key, val in objs.items():
            if len(line) != 0:
                if type(val) is eval(line):
                    val = str(objs[key])
                    obj_list.append(val)
            else:
                val = str(objs[key])
                obj_list.append(val)

        print(obj_list)

    def do_update(self, line):
        """
            Updates an instance based on te class name and id
            by adding or updating attribute(changes saved in json file.)
            Usage: update <class name> <id> <attribute name>
            "<attribute value>"
        """
        dq1 = line.find('\"')
        if dq1 != -1:
            dq2 = line[dq1+1:].find('\"')
            if dq2 != -1:
                dq2 = dq1 + dq2 + 1
        cmds = line.split()

        if len(cmds) == 0:
            print("** class name missing **")
            return

        try:
            eval(cmds[0])
        except NameError:
            print("** class doesn't exist **")
            return

        if len(cmds) == 1:
            print("** instance id missing **")
            return

        key = cmds[0] + "." + cmds[1]
        models.storage.reload()
        objs = models.storage.all()

        try:
            value = objs[key]
        except KeyError:
            print("** no instance found **")
            return
        if len(cmds) == 2:
            print("** attribute name missing **")
            return
        elif len(cmds) == 3:
            print("** value missing **")
            return

        try:
            if dq1 != -1:
                if dq2 != -1:
                    cmds[3] = line[dq1+1:dq2]
            attr_type = type(getattr(value, cmds[2]))
            cmds[3] = attr_type(cmds[3])

        except AttributeError:
            pass

        setattr(value, cmds[2], cmds[3])
        models.storage.save()

    def do_count(self, line):
        """
            Counts the number of intances of a class
        """
        try:
            if len(line) != 0:
                eval(line)
        except NameError:
            print("** class doesn't exist **")
            return

        models.storage.reload()
        objs = models.storage.all()
        count = 0

        for key in objs.keys():
            if line in key:
                count = count + 1

        print(count)

    def do_destroy(self, line):
        """
            Deletes an instance based on the class name and id.
            Change is saved.
            Usage: destroy <ClassName> <id>
        """
        cmds = line.split()

        if len(cmds) == 0:
            print("** class name missing **")
            return

        try:
            eval(cmds[0])
        except NameError:
            print("** class doesn't exist **")
            return

        if len(cmds) == 1:
            print("** instance id missing **")
            return

#        storage = FileStorage()
        models.storage.reload()
        obj = models.storage.all()

        key = cmds[0] + "." + cmds[1]

        try:
            del obj[key]
        except KeyError:
            print("** no instance found **")
            return

        models.storage.save()

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

    def default(self, line):
        """Called when an unknown command is received"""
        cmds = line.split(".")

        try:
            eval(cmds[0])
        except NameError:
            print("** class doesn't exist **")
            return

        if len(cmds) > 1:
            if "show" in cmds[1]:
                obj_id = cmds[1].split('"')[1]
                msg = cmds[0] + " " + obj_id
                self.do_show(msg)

            elif "destroy" in cmds[1]:
                obj_id = cmds[1].split('"')[1]
                msg = cmds[0] + " " + obj_id
                self.do_destroy(msg)

            elif "all" in cmds[1]:
                msg = cmds[0]
                self.do_all(msg)

            elif "count" in cmds[1]:
                msg = cmds[0]
                self.do_count(msg)

            elif "update" in cmds[1]:
                obj_id = cmds[1].split('"')[1]
                tt = cmds[0] + " " + obj_id
                if '{' in cmds[1]:
                    tmp = cmds[1].split('{')[1]
                    tmp = tmp.replace("})", "")
                    tmp = tmp.replace('"', "")
                    tmp = tmp.replace("'", "")
                    tmp = tmp.replace(",", "")
                    tmp = tmp.replace(":", "")
                    tmps = tmp.split()

                    key = []
                    value = []
                    for index in range(len(tmps)):
                        if index % 2 == 0:
                            key.append(tmps[index])
                        else:
                            value.append(tmps[index])

                    for index in range(len(key)):
                        msg = tt + " " + key[index] + ' "' + value[index] + '"'
                        self.do_update(msg)
                else:
                    attr_nm = cmds[1].split('"')[3]
                    attrval = cmds[1].split('"')[5]

                    self.do_update(tt + " " + attr_nm + " \"" + attrval + "\"")
# Help functions

    def help_create(self):
        print("Creates a new instance of BaseModel and saves \
it.\nUsage: create <ClassName>")

    def help_show(self):
        print("Prints the string representation of an instance \
based on the class name and id.\nUsage: show <ClassName> <id>.")

    def help_all(self):
        print("Prints all string representation of all instances.\
\nUsage: all or all <ClassName>")

    def help_update(self):
        print("Updates an instance based on the class name and id\
by adding or changing attribute values.\
\nUsage: update <class name> <id> <attribute name> \"<attribute value>\"")

    def help_count(self):
        print("Prints the number of instances of a class.\
\nUsage: <class_name>.count() ")

    def help_quit(self):
        print("Exit the command line.\nUsage: quit")

    def help_EOF(self):
        print("Exit the command line")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
