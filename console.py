#!/usr/bin/python3
"""The entry point to interact with the AirBnB console."""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity

class_list = {
        "basemodel": BaseModel,
        "user": User,
        "city": City,
        "place": Place,
        "state": State,
        "review": Review,
        "amenity": Amenity
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


def get_value(string):
    """Get the first meaningful value from a string."""
    first_char = string[0]
    if first_char == '"':
        return string.split('"')[1]
    else:
        return string.split(' ')[0]


class HBNBCommand(cmd.Cmd):
    """The console of the AirBnB project."""
    prompt = "(hbnb) "

    def do_create(self, arg):
        """create <class name>
        Create a new instance of the given class."""
        if valid_class(arg):
            instance = class_list[arg.lower()]()
            print(instance.id)
            storage.save()

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
                key = f"{instance.__class__.__name__}.{instance.id}"
                del storage.all()[key]
                del instance
                storage.save()

    def do_all(self, arg):
        """all [class name]
        Show informations about every available instance of a specific class
        if no argument given all classes is considered.
        """
        needed = dict()
        if arg != "" and valid_class(arg):
            for key, instance in storage.all().items():
                if arg.lower() in key.lower():
                    needed[key] = instance
        elif arg == "":
            needed = storage.all()

        for key, instance in needed.items():
            print(instance)

    def do_update(self, arg):
        """update <class name> <id> <attribute name> "<attribute value>"
        Update an instance attribute.
        """
        args = arg.split(" ", 3) + ["", "", ""]
        if not valid_class(args[0]):
            return False
        instance = get_instance(args[0], args[1])
        if not instance:
            return False
        if args[2] == "":
            print("** attribute name missing **")
            return False
        if args[3] == "":
            print("** value missing **")
        else:
            value = get_value(args[3])
            instance.__dict__[args[2]] = value
            storage.save()

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
