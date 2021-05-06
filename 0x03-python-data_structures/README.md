## :pencil2: Python - Data structures: lists and tuples

This folder contains some useful scripts with basic Python  about the basic use of these data structures. The use of the index in the lists, some functions like len, del instead of pop(), how to switch variable values without the use of an auxiliar variable, reverse(). Also here we have some examples of how to copy an modify a list without modify the original, using cop

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


This is a short description of each script:
+ 0-print_list_integer.py: A function that prints all integers of a list, one integer per line.
+ 1-element_at.py: A function that retrieves an element from a list. If the index is negative or is greater than the number of elements in the list, the function return None. 
+ 2-replace_in_list.py: A function that replaces an element of a list at a specific position.
+ 3-print_reversed_list_integer.py: A function that prints all integers of a list, in reverse order.
+ 4-new_in_list.py: A function that replaces an element in a list at a specific position without modifying the original list.
+ 5-no_c.py: A function that removes all characters c and C from a string.
+ 6-print_matrix_integer.py: A function that prints a matrix of integers.
+ 7-add_tuple.py: A function that adds 2 tuples. Returns a tuple with 2 integers: The first element will be the addition of the first element of each argument. The second element will be the addition of the second element of each argument.
+ 8-multiple_returns.py: A function that returns a tuple with the length of a string and its first character.
+ 9-max_integer.py: A function that finds the biggest integer of a list.
+ 10-divisible_by_2.py: A function that finds all multiples of 2 in a list. Return a new list with True of False, depending on whether the integer at the same position in the original list is a multiple of 2.
+ 11-delete_at.py: A function that deletes the item at a specific position in a list. If idx is negative or out of range, nothing change (returns the same list).
+ 12-switch.py: A function to switch value of a and b.
 12-switch.py: A function to switch value of a and b.
+
<!--stackedit_data:
eyJoaXN0b3J5IjpbNzI1NDQxNDIxXX0=
-->