
## :pencil2: Python - Everything is object
In this project we resolve some questions about how Python works with different types of objects: Integers, strings, tuples, lists. Additional, some characteristics related with mutable and immutable values of different types of variables. Also, the use of aliasing and the use of cloning of some type variables like lists.

### Requirements:
The command were tested on Ubuntu 14.04 LTS. Although the commands might work well on other distributions, versions or operative systems. The Python linter was PEP8, and the version of Python was Python 3.4.3. 

### Usage:

Verify that the script file have execution permissions before being used! **If not, use the following command:**

    chmod u+x name_of_file ###To make the file executable

For the shell and Python scripts, the way to execute them is by putting a period and a slash before the command name. As follows:

    ./name_of_file ###To execute the file

### Executable files and text files:

Here a short description of each text file or script:
+ [0-answer.txt](https://github.com/dmhenaopa/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/0-answer.txt): What function would you use to print the type of an object?
+ [1-answer.txt](https://github.com/dmhenaopa/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/1-answer.txt): How do you get the variable identifier (which is the memory address in the CPython implementation)?
+ [2-answer.txt](https://github.com/dmhenaopa/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/2-answer.txt): Do a and b point to the same object? a = 89, b = 100
+ [3-answer.txt](https://github.com/dmhenaopa/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/3-answer.txt): Do a and b point to the same object? a = 89, b = 89
+ [4-answer.txt](https://github.com/dmhenaopa/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/4-answer.txt): Do a and b point to the same object? a = 89, b = a
+ [5-answer.txt](https://github.com/dmhenaopa/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/5-answer.txt): Do a and b point to the same object? a = 89, b = a + 1
+ [6-answer.txt](https://github.com/dmhenaopa/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/6-answer.txt): What do these 3 lines print? s1 = "Holberton", s2 = s1, print(s1 == s2)
+ [7-answer.txt](https://github.com/dmhenaopa/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/7-answer.txt): What do these 3 lines print? s1 = "Holberton", s2 = s1, print(s1 is s2)
+ [8-answer.txt](https://github.com/dmhenaopa/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/8-answer.txt): What do these 3 lines print? s1 = "Holberton", s2 = "Holberton", print(s1 == s2)
+ [9-answer.txt](https://github.com/dmhenaopa/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/9-answer.txt): What do these 3 lines print? s1 = "Holberton", s2 = "Holberton", print(s1 == s2)
+ [10-answer.txt](https://github.com/dmhenaopa/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/10-answer.txt): What do these 3 lines print? l1 = [1, 2, 3], l2 = [1, 2, 3], print(l1 == l2)
+ [11-answer.txt](https://github.com/dmhenaopa/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/11-answer.txt): What do these 3 lines print? l1 = [1, 2, 3], l2 = [1, 2, 3], print(l1 is l2)
+ [12-answer.txt](https://github.com/dmhenaopa/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/12-answer.txt): What do these 3 lines print? l1 = [1, 2, 3], l2 = l1, print(l1 == l2)
+ [13-answer.txt](https://github.com/dmhenaopa/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/13-answer.txt): What do these 3 lines print? l1 = [1, 2, 3], l2 = l1, print(l1 is l2)
+ [14-answer.txt](https://github.com/dmhenaopa/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/14-answer.txt): What does this script print? l1 = [1, 2, 3], l2 = l1, l1.append(4), print(l2)
+ [15-answer.txt](https://github.com/dmhenaopa/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/15-answer.txt): What does this script print? l1 = [1, 2, 3], l2 = l1, l1 = l1 + [4], print(l2)
+ [16-answer.txt](https://github.com/dmhenaopa/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/16-answer.txt): What does this script print? def increment(n): n += 1, a = 1, increment(a), print(a)
+ [17-answer.txt](https://github.com/dmhenaopa/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/17-answer.txt): What does this script print? def increment(n): n.append(4), l = [1, 2, 3], increment(l), print(l)
+ [18-answer.txt](https://github.com/dmhenaopa/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/18-answer.txt): What does this script print? def assign_value(n, v):  n = v, l1 = [1, 2, 3], l2 = [4, 5, 6], assign_value(l1, l2), print(l1)
+ [19-copy_list.py](https://github.com/dmhenaopa/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/19-answer.txt): A function def copy_list(l): that returns a copy of a list.
+ [20-answer.txt](https://github.com/dmhenaopa/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/20-answer.txt): Is a a tuple? a = ()
+ [21-answer.txt](https://github.com/dmhenaopa/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/21-answer.txt): Is a a tuple? a = (1, 2)
+ [22-answer.txt](https://github.com/dmhenaopa/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/22-answer.txt): Is a a tuple? a = (1)
+ [23-answer.txt](https://github.com/dmhenaopa/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/23-answer.txt): Is a a tuple? a = (1, )
+ [24-answer.txt](https://github.com/dmhenaopa/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/24-answer.txt): What does this script print? a = (1), b = (1), print(a is b)
+ [25-answer.txt](https://github.com/dmhenaopa/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/25-answer.txt): What does this script print? a = (1, 2), b = (1, 2), print(a is b)
+ [26-answer.txt](https://github.com/dmhenaopa/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/26-answer.txt): What does this script print? a = (), b = (), print(a is b)
+ [27-answer.txt](https://github.com/dmhenaopa/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/27-answer.txt): Will the last line of this script print 139926795932424? id(a), 139926795932424, a, [1, 2, 3, 4], a = a + [5], id(a)
+ [28-answer.txt](https://github.com/dmhenaopa/holbertonschool-higher_level_programming/blob/master/0x09-python-everything_is_object/28-answer.txt): Will the last line of this script print 139926795932424? a, [1, 2, 3], id (a), 139926795932424, a += [4], id(a)
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTE3MTgwMjkyMzFdfQ==
-->