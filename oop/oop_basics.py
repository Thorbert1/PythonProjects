# any methods defined within the class can be called on an object of said class
class Person:
    # the __init__ method is a constructor method that initializes the object and its initial state
    def __init__(
        # the variable=None statement states that the default value of the variable is None
        self,
        name: str = None,
        age: int = None,
    ):
        # the self variable refers to the object, and the variable being initialized is placed after the "."
        self.name = name
        self.age = age

    def say_hi(self):
        return f"{self.name} is {self.age} years old"


# this method defined outside of the Person class cannot be called on a Person object
# the self parameter inside a class refers to an object of said class, while outside of the class it acts as a normal function parameter
def say_hello(obj):
    return f"Hello, {obj.name}! Is it true that you are {obj.age} years old?\n"


def demo1() -> str:
    t = Person("Thorbert", 17)
    # because of the earlier discrepancy in method calling, we need to input the object as a parameter in this case
    return say_hello(t)


def demo2() -> str:
    f = Person("Felicia", 18)
    try:
        return f.say_hi()  # prints the f-string defined in say_hi()
    except AttributeError:
        return "AttributeError: 'Person' object has no attribute 'say_hello'"


if __name__ == "__main__":
    print("Say hello:\n", demo1(), "\n", "Say hi:\n", demo2(), sep="")
