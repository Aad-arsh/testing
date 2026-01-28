from enum import Enum
class TaskStatusEnum(Enum):
    PENDING = "pending"
    DONE = "done"

    @classmethod 
    def choices(cls):
        return [(key.value, key.name) for key in cls]  