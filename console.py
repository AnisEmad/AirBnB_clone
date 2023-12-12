#!/usr/bin/python3
"""The entry point to interact with the AirBnB console."""
import cmd
from datetime import datetime
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


def dot_all(**kwargs):
    """<class name>.all()
    Show all instances created from specific class
    same as typing:
        show <class name> <id>
    """
    kwargs["cmd_instance"].do_all(kwargs["class_name"])


def dot_count(**kwargs):
    """<class name>.count()
    Get number of instances available for a class name
    """
    count = 0
    for key, instance in storage.all().items():
        if kwargs["class_name"] in key.lower():
            count += 1
    print(count)


def dot_show(**kwargs):
    """<class name>.show(<id>)
    Show informations about specific instance
    same as typing:
        show <class name> <id>
    """
    arg = kwargs["class_name"] + " " + kwargs["method_args"]
    kwargs["cmd_instance"].do_show(arg)


def dot_destroy(**kwargs):
    """<class name>.show(<id>)
    Show informations about specific instance
    same as typing:
        show <class name> <id>
    """
    arg = kwargs["class_name"] + " " + kwargs["method_args"]
    kwargs["cmd_instance"].do_destroy(arg)


def dot_update(**kwargs):
    """<class name>.update(<id>, {<attribute name>: <value>})
    Show informations about specific instance
    same as typing:
        update <class name> <id> <attribute name> "<value>"
    """
    arg_t = eval(f"({kwargs['method_args']})") + ("", "", "")
    if type(arg_t[1]) is dict:
        instance = get_instance(kwargs["class_name"], arg_t[0])
        if instance:
            instance.__dict__.update(arg_t[1])
            instance.updated_at = datetime.now()
            storage.save()
    else:
        arg = f"{kwargs['class_name']} {arg_t[0]} {arg_t[1]} \"{arg_t[2]}\""
        kwargs["cmd_instance"].do_update(arg)


method_list = {
        "all": dot_all,
        "show": dot_show,
        "count": dot_count,
        "destroy": dot_destroy,
        "update": dot_update
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
            instance.updated_at = datetime.now()
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

    def default(self, command):
        """Override the default error msg.
        but this is for implementing another way of typing commands.
        """
        if "." not in command:
            super().default(command)
            return False
        command = command.split(".", 1) + [""]
        method = command[1].split('(', 1) + [""]
        class_name = command[0].lower()
        method_name = method[0]
        method_args = method[1].split(')')[0]
        if class_name in class_list and method_name in method_list:
            method_list[method_name](
                    cmd_instance=self,
                    class_name=class_name,
                    method_args=method_args)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
