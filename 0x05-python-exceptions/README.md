## :pencil2: Python - Exceptions
This folder contains some useful scripts with basic Python commands to run python scripts or code handling errors and exceptions

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
+ 0-safe_print_list.py: A  function that prints x elements of a list. Returns the real number of elements printed. Otherwise, if the number of elements is out of index, it breaks.
+ 1-safe_print_integer.py: A function that prints an integer. Return True if the value is an integer and has been correctly printed. Otherwise, returns False.
+ 2-safe_print_list_integers.py: A function that prints the first x elements of a list and only integers. Returns the number of integers printed.
+ 3-safe_print_division.py: A function that divides 2 integers and prints the result. Return the value of the division. Otherwise, returns None.
+ 4-list_division.py: A function that divides element by element 2 lists. The list can contain any type (integer, string...). Returns a new list with all divisions.
+ 5-raise_exception.py: A function that raises a type exception.
+ 6-raise_exception_msg.py: A function that raises a name exception with a message.
+ 100-safe_print_integer_err.py: A function that prints an integer. Returns True if value has been correctly printed (it means the value is an integer). Otherwise, returns False and prints in stderr the error precede by Exception:.
+ 101-safe_function.py: A function that executes a function safely. Returns the result of the function, otherwise, returns None if something happens during the function and prints in stderr the error precede by Exception:.
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE5MzY2MjQ3OTFdfQ==
-->