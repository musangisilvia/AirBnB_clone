#!/usr/bin/python3
"""
    This is the entry point of the command interpreter.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
        HBNBCommand implements the Cmd class.
        It is a command  interpreter for the AirBnB project.
    """
    prompt = '(hbnb) '

    def do_quit(self, line):
        """
            Exit the program
        """
        return True

    def do_EOF(self, line):
        """
            defines action when end of file is reached
        """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
