## :pencil2: JavaScript - Warm up

This folder contains JavaScript basic scripts. Here we found commands to create variables and constants, how to use if, if... else statements, how to use loops, how to declare and use a function and how to import a file.  

### Requirements:
All commands were tested on Ubuntu 20.04 LTS. Although the commands might work fine on other distributions, versions or operative systems.

Additionally, node (version 14.x) was used.

If you don't have Node 14 installed, download it and install as shown (Ubuntu):

    curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
    sudo apt-get install -y nodejs

### Usage:
Verify that the files have execution permissions before being used! **If not, use the following command:**

    chmod u+x name_of_file ###To make the file executable

In all cases, all files, the way to execute them is by putting a period and a slash before the command name. As follows:

    ./name_of_file ###To execute the file

Some scripts need arguments, you can pass arguments as follows:

    ./name_of_file argument1 argument2... ###To execute the file

### Executable files:

Here a short description of each script:

+ 0-javascript_is_amazing.js: A script that prints “JavaScript is amazing”.
+ 1-multi_languages.js: A script that prints 3 lines (The first line: “C is fun”; The second line: “Python is cool”; The third line: “JavaScript is amazing”).
+ 2-arguments.js: A script that prints a message depending of the number of arguments passed (If no arguments are passed to the script, print “No argument”; If only one argument is passed to the script, print “Argument found”; Otherwise, print “Arguments found”).
+ 3-value_argument.js: A script that prints the first argument passed to it (If no arguments are passed to the script, print “No argument”).
+ 4-concat.js: A script that prints two arguments passed to it, in the following format: “ is ”.
+ 5-to_integer.js: A script that prints My number: <first argument converted in integer> if the first argument can be converted to an integer (If the argument can’t be converted to an integer, print “Not a number”).
+ 6-multi_languages_loop.js: A script that prints 3 lines: (like 1-multi_languages.js) but by using an array of string and a loop (The first line: “C is fun”; The second line: “Python is cool”; The third line: “JavaScript is amazing”).
+ 7-multi_c.js: A script that prints x times “C is fun”. If the first argument can’t be converted to an integer, print “Missing number of occurrences”.
+ 8-square.js: A script that prints a square. The first argument is the size of the square. If the first argument can’t be converted to an integer, print “Missing size”.
+ 9-add.js: A script that prints the addition of 2 integers. The first argument is the first integer. The second argument is the second integer.
+ 10-factorial.js: A script that computes and prints a factorial. The first argument is integer (argument can be cast as integer) used for computing the factorial. Factorial of NaN is 1.
+ 11-second_biggest.js: A script that searches the second biggest integer in the list of arguments. If no argument passed, print 0. If the number of arguments is 1, print 0.
+ 12-object.js: A script to replace the value 12 with 89.
+ 13-add.js: A function that returns the addition of 2 integers.
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTE5MDUxMTA4NV19
-->