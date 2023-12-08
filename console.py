#!/usr/bin/python3
"""The entry point to interact with the AirBnB console."""
import cmd


class HBNBCommand(cmd.Cmd):
    """The console."""
    prompt = "(hbnb)"

    def do_create(self, arg):
        """create <ClassName>
        create a new instance of BaseModel."""
        pass

    def do_show(self, arg):
        """show <instance> <id>
        Print __str__ of an instance."""
        pass

    def do_destroy(self, arg):
        """destroy <instance>
        Delete the given instance."""
        pass

    def do_all(self, arg):
        """ all <ClassName> or all 
        Prints all str representation
        """
        pass

    def do_update(self, arg):
        """ update <class name> <id> <attribute name> "<attribute value>"
        update instance attributes 
        """
        pass
    def do_EOF(self, arg):
        """exit the program"""
        print()
        return True

    def do_quit(self, arg):
        """exit the program"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
