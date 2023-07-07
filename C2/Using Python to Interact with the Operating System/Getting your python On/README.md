**Getting Famillier with operating system:~**

_Microsoft Windows isn't an Open-Source OS._

The operating system is a software that manages everything that goes on in the computer.

There are two main parts of an operating system: the kernel and the user space.

The major operating systems used in IT today are Windows, Mac OS, and Linux.

Linux is an open source operating system, which means it is free to share, modify, and distribute.

Python is a cross-platform language, which means it can be used on Windows, Mac OS, Linux, and other operating systems.

In this course, we will be using Linux and Python to interact with the operating system.

**Getting Your Computer Ready for Python**

_pip the name of the command line tool commonly used to install, update, and remove external Python modules._

The best way to learn Python is to practice by running the scripts on your computer.

To run Python locally, you need to have it installed on your computer.

You can check whether you already have Python installed by running the Python --version command .

If you don't have Python installed, you can install it from the Python website.

After installing Python, you can install additional modules that aren't part of the Python Standard Library.

These additional modules can be found on the Python Package Index (PyPI).

You can install, update, and remove external modules using the pip command line tool.

**Setting up Your Environment on Windows (Optional)**
Windows computers do not come with Python preinstalled.

To do this, we will download the executable installer for Python 3 64-bit architecture.

Once the installer has downloaded, we will run it as an administrator user.

We will need to check the "Add Python 3.7 to Path" box before clicking "Install now".

This will ensure that the Python interpreter is executed when we invoke it from the command line.

After Python has been installed, we can test to see that it worked by opening a new PowerShell and executing the command "python --version".

If Python is installed correctly, we will see the version number of the interpreter.

We can also check to see if the request module is installed by importing it into the interpreter.

If the module is not installed, we can install it using Pip.

To do this, we will run the command "pip install request" from the command line.

Once the module is installed, we can import it into the interpreter and use it to interact with web services.
_Here are some additional tips for installing Python on Windows:_

Make sure that you download the correct version of Python for your computer.

If you are not sure which version of Python to download, you can check the system requirements for your computer.

You can also install Python from the Microsoft Store. This is a convenient option, but it may not include all of the latest features and bug fixes.

If you are having trouble installing Python, you can search for help online or contact the Python community for support.

**Running Python Locally**
Interpreted languages are those that are not compiled into machine code before they are run. Instead, they are interpreted line by line by an interpreter program.

This makes interpreted languages slower than compiled languages, but it also makes them easier to develop and debug.

Python is an interpreted language, so you can write a Python script on one operating system and run it on another without making any changes.

Java and C# are compiled languages, but they are compiled into intermediate code that can be run on different platforms.

This means that you can write a Java or C# program on one operating system and run it on another without making any changes, as long as you have the Java Virtual Machine (JVM) or Common Language Runtime (CLR) installed on the target operating system.

In this video, we learned how to run Python scripts from a command prompt.

We first learned that we can run Python scripts by typing the name of the script followed by the .py extension.

We then learned that we can add a shebang line to the beginning of a Python script to tell the operating system what command to use to execute the script.

The shebang line is usually a single line that starts with a hash (#) character and then the path to the interpreter followed by a space.

For example, the shebang line for Python 3 would be:~
_#!/usr/bin/python3_

Once we have added the shebang line to our Python script, we can make the script executable using the chmod command.

To do this, we run the following command:~

_chmod +x hello_world.py_

This will make the hello_world.py script executable.

We can now run the hello*world.py script by typing the following command:
*./hello*world.py*
python3 hello_world.py

A module is a file that contains Python code.

Modules can be used to organize code and to make it easier to reuse code.

To use a module, we need to import it.

To import a module, we use the import keyword followed by the name of the module.

We can then access the functions and variables defined in the module by using dot notation.

For example, if we have a module called areas.py that contains a function called calculate_area, we can access the function by using the following code:.

import areas

area = areas.calculate_area(5, 4)
This code will calculate the area of a rectangle with a width of 5 and a height of 4 and store the result in the variable area.

We can also import multiple modules at the same time.
For example, the following code imports the areas.py and math.py modules:
import areas
import math

This code allows us to use the calculate_area function from the areas.py module and the pi constant from the math.py module.

Modules can also be nested.

This means that we can put modules inside of other modules.

For example, the following code creates a module called

my_module.py that contains a submodule called areas.py:
def calculate_area(width, height):
return width \* height

def main():
area = calculate_area(5, 4)
print(area)

if **name** == "**main**":
main()

The my_module.py module contains a function called calculate_area and a main function.

The areas.py submodule contains the calculate_area function.

To use the my_module.py module, we need to import it.

We can do this using the following code:

import my_module

This code imports the my_module.py module and makes the calculate_area function available to us.

We can then call the calculate_area function using the following code:

area = my_module.calculate_area(5, 4)

**IDE**

Integrated Development Environment (IDE) is a code editor with some handy extra capabilities that make writing scripts a lot easier.

Some of the most basic extra features in code editors are syntax highlighting and code completion.

Syntax highlighting means that the editor recognizes the language we are writing our code in, and highlights the pieces of code that make up the syntax of the language.

Code completion means that the editor suggests the names of the variables and functions as we are typing.

There are a bunch of different code editors available, so it is important to find one that you feel comfortable and productive with.

Some popular code editors include Atom, Notepad++, Sublime Text, Eclipse, and PyCharm.

It is also a good idea to learn how to use a command line editor like Vim, Emacs, or Nano.

Graphical code editors with additional capabilities can save us a lot of time, but command line editors are essential for times when you might not be able to use a graphical editor.

When you are writing a lot of code, having an editor automatically complete the names of the variables and functions can save you a lot of time.

It is a good idea to familiarize yourself with the editor's capabilities so that you can get the most out of it.

Feel free to experiment writing some scripts and executing them until you feel comfortable editing your Python scripts.

As an IT specialist, you don't want to be completely tied to just one editor. It's possible you may need to debug a problem on the computer with a different editor installed, and you don't want to waste time installing your preferred editor. So make sure you have a basic idea of how to use an editor that's installed by default on the computers you work with.
