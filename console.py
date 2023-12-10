#!/usr/bin/python3
"""The entry point to interact with the AirBnB console."""
import cmd
import functions as utils
from models             import storage
from models.base_model  import BaseModel
from models.user        import User
from models.city        import City
from models.place       import Place
from models.state       import State
from models.review      import Review
from models.amenity     import Amenity

class_list = {
        "basemodel": BaseModel,
        "user"     : User,
        "city"     : City,
        "place"    : Place,
        "state"    : State,
        "review"   : Review,
        "amenity"  : Amenity
}

def valid_class(name):
    """Check if the class is valid or print error."""
    if name == "":
        print("** class name missing **")
    elif name.lower() not in class_list:
        print("** class doesn't exist **")
    else:
        return True

def get_instance(class_name, instance_id):
    """Get an instance from the storage (if exist)"""
    key = f"{class_list[class_name.lower()].__name__}.{instance_id}"
    all = storage.all()
    if instance_id == "":
        print("** instance id missing **")
    elif key not in all:
        print("** no instance found **")
    else:
        return all[key]
    return False

class HBNBCommand(cmd.Cmd):
    """The console."""
    prompt = "(hbnb)"

    def do_create(self, arg):
        """create <class name>
        Create a new instance of the given class."""
        if valid_class(arg):
            instance = class_list[arg.lower()]()
            print(instance.id)


    def do_show(self, arg):
        """show <class name> <instance id>
        Show informations about an instance."""
        args = arg.split(" ") + [""]
        if valid_class(args[0]):
            instance = get_instance(args[0], args[1])
            if instance:
                print(instance)



    def do_destroy(self, arg):
        """destroy <instance>
        Delete the given instance."""
        args = arg.split(" ") + [""]
        if valid_class(args[0]):
            instance = get_instance(args[0], args[1])
            if instance:
                del instance

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
