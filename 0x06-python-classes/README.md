## :pencil2: Python - Classes and objects
This folder contains some useful scripts with basic Python modules.

### Requirements:
All commands were tested on Ubuntu 14.04 LTS. Although the commands might work well on other distributions, versions or operative systems. The Python linter was PEP8, and the version of Python was Python 3.4.3. 

### Usage:
Verify that the files have execution permissions before being used! **If not, use the following command:**

    chmod u+x name_of_file ###To make the file executable

For the shell and Python scripts, the way to execute them is by putting a period and a slash before the command name. As follows:

    ./name_of_file ###To execute the file

For the C file, we need to use the compiler GCC:

    gcc -Wall -Werror -Wextra -pedantic all_the_c_files.c -o output_name

### Executable files:

Here a short description of each script:
+ 0-square.py: An empty class Square that defines a square.
+ 1-square.py: A class Square that defines a square. We have the private instance attribute: size.
+ 2-square.py: A class Square that defines a square. Private instance attribute: size. Instantiation with optional size: def __init__(self, size=0): size must be an integer, otherwise raise a TypeError exception with the message size must be an integer. If size is less than 0, raise a ValueError exception with the message size must be >= 0.
+ 3-square.py: A class Square that defines a square. Private instance attribute: size. Instantiation with optional size: def __init__(self, size=0): size must be an integer, otherwise raise a TypeError exception with the message size must be an integer. If size is less than 0, raise a ValueError exception with the message size must be >= 0. Public instance method: def area(self): that returns the current square area.
+ 4-square.py: A class Square that defines a square. Private instance attribute: size: property def size(self): to retrieve it. Property setter def size(self, value): to set it: size must be an integer, otherwise raise a TypeError exception with the message size must be an integer. If size is less than 0, raise a ValueError exception with the message size must be >= 0. 
+ 5-square.py: A class Square that defines a square. Private instance attribute: size: property def size(self): to retrieve it. Property setter def size(self, value): to set it: size must be an integer, otherwise raise a TypeError exception with the message size must be an integer. If size is less than 0, raise a ValueError exception with the message size must be >= 0. Public instance method: def my_print(self): that prints in stdout the square with the character #.
+ 6-square.py: A class Square that defines a square. Private instance attribute: size: property def size(self): to retrieve it. Property setter def size(self, value): to set it: size must be an integer, otherwise raise a TypeError exception with the message size must be an integer. If size is less than 0, raise a ValueError exception with the message size must be >= 0. Private instance attribute: position: property def position(self): to retrieve it. property setter def position(self, value): to set it:position must be a tuple of 2 positive integers, otherwise raise a TypeError exception with the message position must be a tuple of 2 positive integers. Instantiation with optional size and optional position: def __init__(self, size=0, position=(0, 0)):. Public instance method: def area(self): that returns the current square area. Public instance method: def my_print(self): that prints in stdout the square with the character #: if size is equal to 0, print an empty line. Position should be use by using space - Don’t fill lines by spaces when position[1] > 0.
<!--stackedit_data:
eyJoaXN0b3J5IjpbOTE5OTAxNzQyXX0=
-->