"""
python libraries are like toolkits 
they have expedites programming 


For Web development Some libraries are important as follows:
1.Requests : sends http requests 
2.BeautifulSoup : Scrap web page informations by itterating, modifiying , and searching the parse tree 
3.SQLAlchemy : is a SQL toolkit an object relational mapping { ORM tool }
4.Pytest : is the Testing Framework 


Frameworks are predifned structures for application development
Provides set of guidelines for application development 

Ex : Django , Flask , Web2Py

benefits of using a frameworks 
1. Eases the development process 
2. simplifies debugguing process 
3. Enable more functionaliyt with less code 
4. Improve DB management efficiently
5. Helps Security by Enforce 


Code Calls Libraries 

Framework Calls Code 
  Frameworks can contian libraries 
  
"""

"""
Flask is the micro framework that helps in creating web app
Flask 2.2.2 which requires minimum python 3.7
comes with minimal set of depenedencies 
Community-maintained Extension


*** main features of flask
1. Built in web server : run application in development mode 
2. Has a debugger 
3. Uses standard python logging 
4. Has a built-in unit testing 
5. Enables request and response  classes 

**** Additional features 
Provides static asset support : like css ,js files ,images 
Flask provides tags to load static files in the templates 
Provides Dynamic templates : using jinja plugging framework 
Supports routing and Dynamic URL's , HTTP methods , Redirection 
Enables Error Handling : global 
Supports user Session 


**** popular Extensions 
Flask-SQLAlchemy : support for orm 
Flask-Mail : provides ability to setup an SMTP mail server 
Flask-Admin : lets you add admin interfaces to Flask applications 
Flask-Uploads : allow you to customize file uploading to your web application 

**** other extensions 
Flask-CORS : allows your application to Cross origin resource sharing making CORS js request is possible 
Flask-Migrate : adds DB migration to SQL-Alchemy 
Flask-User : adds user Authentication , Authorization and other user management activities 
MarshMellow : adds Extensive object Serialization and Deserialization support to your code 
Celery : is the powerful task queue that can be used to simple background task and complex multistorage programs and schedules 


**** Installation Flask 
Using PIP 
1. Create a virtual environment :
   python -m venv venv
   source ./venv/bin/activate 
   , this is the virtual env module 

2. Install Flask :
   pip install Flask==2.2.2 -> important to pin version number of the dependencies in your application this ensures the failure , and reproduced from scratch 


**** Built-in Dependencies 
Werkzeug : Implements Server : WSGI (web server gateway interface)
           standard python interface between application and server 

Jinja : Template Language that renders the pages in your application 

MarkupSafe : Comes with jinja . Provides security features in Templates 
             it secapes from rendering pages to avoid injection attacks 

             
ItsDangerous : used to Signing libraries for Session cookies {Data Security} helps to determine data has been tempered with 

Click : is a Framework for writing command line application  , it provides flask commands allows adding custom managment commands 

                 
"""