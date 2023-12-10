"""Model of the base parent class that all classes inherit from."""
from datetime import datetime
from models import storage
import uuid

class BaseModel:
    """Container of all common attributes/methods for other classes."""
    def __init__(self, **kwargs):
        """Make an instance of the BaseModel."""
        if not self.__from_dict(kwargs):
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

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

    def __from_dict(self, src):
        """Initialize a new instance from give dictionary."""
        self.__dict__.update(src)
        if 'id' in src:
            self.created_at = datetime.fromisoformat(self.created_at)
            self.updated_at = datetime.fromisoformat(self.updated_at)
            del self.__dict__["__class__"]
            return True
        else:
            return False

    def save(self):
        """Save the attributes at the current time."""
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()
