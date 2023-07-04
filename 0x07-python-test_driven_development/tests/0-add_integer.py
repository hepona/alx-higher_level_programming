import doctest

def add_integer(a, b):
    """
    >>> add_integer(2, 3)
    5
    >>> add_integer(2, -3)
    -1
    >>> add_integer(-2, -3)
    -5
    >>> add_integer(-2, 3)
    1
    >>> add_integer("2", 3)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "/root/alx-higher_level_programming/0x07-python-test_driven_development/0-add_integer.py", line 4, in add_integer
        raise TypeError("a must be an integer")
    TypeError: a must be an integer
    >>> add_integer(2," 3")
    Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
     File "/root/alx-higher_level_programming/0x07-python-test_driven_development/0-add_integer.py", line 9, in add_integer
        raise TypeError("b must be an integer")
    TypeError: b must be an integer
    >>> add_integer("2","3")
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "/root/alx-higher_level_programming/0x07-python-test_driven_development/0-add_integer.py", line 4, in add_integer
      raise TypeError("a must be an integer")
    TypeError: a must be an integer
    >>> add_integer(0, 0)
    0
    >>> add_integer(True, 2)
    3
    >>> add_integer(4, True)
    5
    """
    return a + b

if __name__ == "__main__":
    doctest.testmod()
