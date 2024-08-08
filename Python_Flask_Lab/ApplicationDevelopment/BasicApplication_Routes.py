"""
Steps to create the basic Flask Application with basic routing

1. Install Flask 
2. Create a Main Server File : app.py
3. Write the Code 
   from flask import Flask 
   # instentiate a object on flask class as your app 
   app= Flask(__name__)
   # constructor takes a single argument of class scaffold
   # you set the name in scaffold class by passing the name of the app module in built-in name variable 
   # this name is used to find resources on the file system and buy extensions to provide debuuging information 
4. Defined above server 
   lets Add first  routes 
   to return the message to client when they call your server without adding a path .
   Use @app decorator to define the method .
   Decorator takes the path as an argument : Pass the URL path 
   Now you can return the html or text  from the method 

   **** the complete code 
   from flask import Flask
   app=Flask(__name__)
   @app.route('/')
   def hello_world():
       return "<b>Hello_world Application is live! </b>"
"""