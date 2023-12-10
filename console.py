#!/usr/bin/python3
"""The entry point to interact with the AirBnB console."""
import cmd
from models             import storage
from models.base_model  import BaseModel
from models.user        import User
from models.city        import City
from models.place       import Place
from models.state       import State
from models.review      import Review
from models.amenity     import Amenity


class HBNBCommand(cmd.Cmd):
    """The console."""
    prompt = "(hbnb)"

    def do_create(self, arg):
        """create <class name>
        Create a new instance of the given class."""
        pass

    def do_show(self, arg):
        """show <class name> <instance id>
        Show informations about an instance."""
        pass

    def do_destroy(self, arg):
        """destroy <instance>
        Delete the given instance."""
        pass

    def do_all(self, arg):
        """all [class name]
        Show informations about every available instance of a specific class
        if no argument given all classes is considered.
        """
        pass

    def do_update(self, arg):
        """update <class name> <id> <attribute name> "<attribute value>"
        Update an instance attribute.
        """
        pass

    def do_EOF(self, arg):
        """exit the program"""
        print()
        return True

    def do_quit(self, arg):
        """exit the program"""
        return True

    def emptyline(self):
        """Type nothing, do nothing."""
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
