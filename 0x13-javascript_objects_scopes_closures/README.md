## :pencil2: JavaScript - Objects, scopes and closures
This folder contains JavaScript basic scripts. Here we found commands to create classes, create a constructor, create an empty object, create and use an instance method, inherits from a parent class, define and use a prototype.  

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
+ [0-rectangle.js](https://github.com/dmhenaopa/holbertonschool-higher_level_programming/blob/master/0x13-javascript_objects_scopes_closures/0-rectangle.js): A script with an empty class Rectangle that defines a rectangle. Associated with the 0-main.js file.
+ [1-rectangle.js](https://github.com/dmhenaopa/holbertonschool-higher_level_programming/blob/master/0x13-javascript_objects_scopes_closures/1-rectangle.js): A script with a class Rectangle that defines a rectangle. The constructor take 2 arguments w (width) and h (height). Associated with the 1-main.js file.
+ [2-rectangle.js](https://github.com/dmhenaopa/holbertonschool-higher_level_programming/blob/master/0x13-javascript_objects_scopes_closures/2-rectangle.js): A script with a class Rectangle that defines a rectangle. The constructor take 2 arguments w (width) and h (height). If w or h is equal to 0 or not a positive integer, create an empty object. Associated with the 2-main.js file.
+ [3-rectangle.js](https://github.com/dmhenaopa/holbertonschool-higher_level_programming/blob/master/0x13-javascript_objects_scopes_closures/3-rectangle.js): A script with a class Rectangle that defines a rectangle. The constructor take 2 arguments w (width) and h (height). I
f w or h is equal to 0 or not a positive integer, create an empty object. With an instance method called print() that prints the rectangle using the character X. Associated with the 3-main.js file.
+ [4-rectangle.js](https://github.com/dmhenaopa/holbertonschool-higher_level_programming/blob/master/0x13-javascript_objects_scopes_closures/4-rectangle.js): A script with a class Rectangle that defines a rectangle. The constructor take 2 arguments w (width) and h (height). I
f w or h is equal to 0 or not a positive integer, create an empty object. With an instance method called print() that prints the rectang
le using the character X, an instance method called rotate() that exchanges the width and the height of the rectangle and an instance method called double() that multiples the width and the height of the rectangle by 2. Associated with the 4-main.js file.
+ [5-square.js](https://github.com/dmhenaopa/holbertonschool-higher_level_programming/blob/master/0x13-javascript_objects_scopes_closures/5-square.js): A script with a class Square that defines a square and inherits from Rectangle of 4-rectangle.js. The constructor takes 1 argument: size. Associated with the 5-main.js file.
+ [6-square.js](https://github.com/dmhenaopa/holbertonschool-higher_level_programming/blob/master/0x13-javascript_objects_scopes_closures/6-square.js): A script with a class Square that defines a square and inherits from Square of 5-square.js. With an instance method called charPrint(c) that prints the rectangle using the character c. If c is undefined, use the character X. Associated with the 6-main.js file.
+ [7-occurrences.js](https://github.com/dmhenaopa/holbertonschool-higher_level_programming/blob/master/0x13-javascript_objects_scopes_closures/7-occurrences.js): A function a function that returns the number of occurrences in a list. Associated with the 7-main.js file.
+ [8-esrever.js](https://github.com/dmhenaopa/holbertonschool-higher_level_programming/blob/master/0x13-javascript_objects_scopes_closures/8-esrever.js): A function that returns the reversed version of a list. Associated with the 8-main.js file.
+ [9-logme.js](https://github.com/dmhenaopa/holbertonschool-higher_level_programming/blob/master/0x13-javascript_objects_scopes_closures/9-logme.js): A function that prints the number of arguments already printed and the new argument value. Output format: `<number arguments already printed>: <current argument value>`. Associated with the 9-main.js file.
+ [10-converter.js](https://github.com/dmhenaopa/holbertonschool-higher_level_programming/blob/master/0x13-javascript_objects_scopes_closures/10-converter.js): A function that converts a number from base 10 to another base passed as argument. Associated with the 10-main.js file.
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTM2NDk4MjI4MF19
-->