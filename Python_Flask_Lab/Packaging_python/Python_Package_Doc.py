"""
int this video lecture we have to create , differentiate and verify python package

diff between python module , package , lib 

python module is nothing but the python code file with .py extension  \
you can import a module from other scripts and notebooks 

python Package is the collection of python modules into a dictionary with __init__.py file 
which makes this distinguish as just a file/dictionaries into a file 

when you import a module and create the object is always of type module 

this distinguish is only at file system level 

a library is the collection of packages or a single package 

creating the package in python 

create two python code srcipts with functions init 

to make project folder a package you must have __init__.py file 

the content of the file must be as follows 

from . import module1.py

from . import module2.py
*****

to create the package follow below steps 

1. create project folder\
2. create __init__.py file 
3. create the required modules


after creating the package you need to verify the package 
follow steps 
1. open terminal (bash)
2. open python interpreter run : python 
3. type import project_name
-- if the command runs without  then package is successfully loaded 
4. to check the functionality type the command by syntax as follows 
   package_name.module_name. function_name(parameters)

   if it returns expected results then package is created successfully 

you can use this package in other scripts if package folder is in same directory 
this can be done as 
from  myproject.module1 import square , dubler 
from  myproject.module2 import mean 


"""