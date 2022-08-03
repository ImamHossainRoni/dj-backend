from enum import Enum


class BaseEnum(Enum):
    """
     Let's allow using an Enum class in model Field choices and make code more simple and modular.
     Ref: https://code.djangoproject.com/ticket/27910
     Ref: https://stackoverflow.com/questions/54802616/how-to-use-enums-as-a-choice-field-in-django-model
    """

    def __init__(self, *args):
        cls = self.__class__
        if any(self.value == e.value for e in cls):
            a = self.name
            e = cls(self.value).name

            raise ValueError("aliases not allowed in DuplicateFreeEnum:  %r --> %r" % (a, e))

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

    @classmethod
    def has_value(cls, value):
        return value in cls._value2member_map_


class ImageSize(BaseEnum):
    SMALL = 256
    MEDIUM = 1024
    LARGE = 2048
