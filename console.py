#!/usr/bin/python3
"""The entry point to interact with the AirBnB console."""
import cmd


class HBNBCommand(cmd.Cmd):
    """The console."""
    prompt = "(hbnb)"

    def do_create(self, arg):
        """create a new instance of BaseModel."""
        pass

    def do_show(self, arg):
        """Print __str__ of an instance."""
        pass

    def do_destroy(self, arg):
        """destroy <instance>
        Delete the given instance."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
