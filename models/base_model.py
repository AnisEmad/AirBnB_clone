"""Model of the base parent class that all classes inherit from."""
from models import storage
import datetime
import uuid

class BaseModel:
    """Container of all common attributes/methods for other classes."""
    def __init__(self, *args, **kwargs):
        """Make an instance of the BaseModel."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """Represent the object in a human readable format."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def to_dict(self):
        """Get a dictionary containing all attributes of instance."""
        instance_dict = self.__dict__.copy()
        instance_dict["__class__"] = self.__class__.__name__
        instance_dict["created_at"] = instance_dict["created_at"].isoformat()
        instance_dict["updated_at"] = instance_dict["updated_at"].isoformat()
        return instance_dict

    def save(self):
        """Save the attributes at the current time."""
        self.updated_at = datetime.datetime.now()
        storage.save()
