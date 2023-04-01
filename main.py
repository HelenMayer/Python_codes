class Counter:
    def __init__(self, value=0):
        """Create an immutable counter."""
        self.value = max(value, 0)

    def inc(self, delta=1):
        return Counter(max(self.value + delta, 0))

    def dec(self, delta=1):
        return self.inc(-delta)



class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @property
    def full_name(self):
        return self.name + ' ' + self.surname

    # сеттер для свойства full_name
    @full_name.setter
    def full_name(self, new):
        self.name, self.surname = new.split(' ')


# BEGIN
class HourClock:
    def __init__(self):
        """Create a new hour clock."""
        self.hand_position = 0

    @property
    def hours(self):
        return self.hand_position

    @hours.setter
    def hours(self, new_position):
        self.hand_position = new_position % 12
# END


class Counter(object):
    """A simple integral counter."""

    def __init__(self):
        """Initialize a new counter with zero as starting value."""
        self.value = 0

    def inc(self, amount=1):
        """Increment counter's value."""
        self.value = max(self.value + amount, 0)

    def dec(self, amount=1):
        """Decrement counter's value."""
        self.inc(-amount)


# BEGIN (write your solution here)
class LimitedCounter(Counter):
    def __init__(self, limit):
        self.limit = limit
        self.value = 0

    def inc(self, amount=1):
        super().inc(amount)
        if self.value > self.limit:
            self.value = self.limit

# END


a = [1,2,3]
b = [*a,4,5,6]
print(b) # [1,2,3,4,5,6]


def printPetNames(owner, **pets):
   print(f"Owner Name: {owner}")
   for pet,name in pets.items():
      print(f"{pet}: {name}")
printPetNames("Jonathan", dog="Brock", fish=["Larry", "Curly", "Moe"], turtle="Shelldon")
# """
# Owner Name: Jonathan
# dog: Brock
# fish: ['Larry', 'Curly', 'Moe']
# turtle: Shelldon
# """


import operator
from operator import mul


def keep_truthful(items):
    result = []
    for item in items:
        if operator.truth(item):
            result.append(item)
    return result

def abs_sum(items):
    result = 0
    for item in items:
        result += abs(item)
    return result

def walk(library, way_to_value):
    result = library
    for item in way_to_value:
        result = operator.getitem(result, item)
    return result



def partial_apply(func, first_arg):
    def  inner(second_arg):
        return func(first_arg, second_arg)
    return inner
    


def flip(func):
    def inner(first_arg, second_arg):
        return func(second_arg, first_arg)
    return inner



def memoized(function):
    memory = {}
    def inner(arg):
        if arg not in memory:
            result = function(arg)
            memory[arg] = result
            return result
        else:
            return memory.get(arg)
 
    return inner

from functools import wraps


def memoizing(max_count):
    index = 0

    def memoized(func):
        memory = {}
        @wraps(func)

        def inner(arg):
            nonlocal index
            if arg not in memory:
                if len(memory) == max_count:
                    del memory[index % max_count]
                result = func(arg)
                memory[arg] = result
                index += 1
                print(index)
                return result
            else:
                return memory.get(arg)
    
        return inner
    return memoized


from functools import wraps

def suppress(*errors, or_return=None):
    def wrapper(func):
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except:
                return or_return
        return inner
    return wrapper