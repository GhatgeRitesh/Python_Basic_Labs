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


5. Running the application 
   1. create few system env variables :Export Settings 
     * variable FLASK_APP : contiaing the name of main server file 
     * variable FLASK_ENV : Define development/Production ENV {this will be deprecated in flask 2.3}

    ** how to define these variables 
    export FLASK_APP=app.py
    export FLASK_ENV=development 

6.  Run The Flask Application 
    flask run in cmd
    defualt port localhost:5000 

    you can see your msg into the console for http://localhost:5000/


Stated Application Running 

**** Run Flask Application with Arguments 
Instead of setting environmental variables , you can pass in arguments to Flask Executable 
 * --app : identifies the python file to run 
 * debug : Starts Debug Mode
           Automatic Restart on file change

 **** Rturning JSON form your flask application 

 1. Return a serializable type/object like dictionary/list
    ex: return {"Name":"Ritesh"}
    curl -X GET -i  localhost:5000 -> this linux command is used to Get the reponse form the link

 2. Use the jsonify() method :
    this method takes in Key Value Pairs add input returns the appropriate JSON 
    ex: from flask import Flask ,jsonify 
        ....
        ....
        return jsonify(message="Hello World")      

    you will get the same result as before in key value pair 


**** Application configuration 
There are many configurations that you can use in your application 
ENV , Debug , Testing:Enables Testing Mode, SECRET_KEY: used to sign a session key , SESSION_COOKIE_NAME: name of session cookie
SERVER_NAME: finds the host and port , JSONIFY_MIMETYPE : Defaults to application/JSON


**** Loading Application Configuration 
other ways to provide configuration to flask 

Flask provides a config Object that acts like a dictionary 
ex: 
   app.config['SECRET_KEY'] = "random-secret-key"

if you have already Variables you can load them into config object
*Configuration from an environment variable 
app.config["VARIABLE_NAME"]
app.config.from_prefixed_env()

** you can store the complete configuration into seperate Json file and load them from file method provided by config object as :
app.config.from_file("pathtoconfigfile")

** Application Structure
should have Directory structure 

Example Structure 

-Config.json
-requirements.txt
-setup.py
-src
   -__init__.py
    -static
      -css
       -main.css
      -img
       -header.png
      -js
       -site.js
    -templates
      -about.html
      -index.html
-tests
  -test_auth.py
  -test_site.py
-venv 

** venv is to install right dependencies with version 

*** Request and Response Objects 

1. Flask Request object 
2. Flask Response Object

**** Custome Routes
we define the route with flasks route decorator 
* default route decorator is set to GET method 
ex : @app.route("/home") : clients can only send to get request 
Use methods argument to only allow specific HTTP methods

ex: @app.route("/Home") : default
    @app.route("/Home" , methods=["GET"]) : custome route method 


the methods usage into custome routes and behaviour 
ex: 
  @app.route("/health" , methods=["GET" , "POST"])
  def health():
    if request.method == "GET" : return jsonify(status="OK" ,method="GET"),200

    if request.method == "POST" : return jsonify(status="(OK)" , method="POST"),200

Request Object Attributes 
* ALL HTTP calls to Flask contain the request object created from Flask.Request class
all the objects and requests are handled by the @app.route() method 

* some common request attributes are: 
  1. addr of server in form of tuple of port 
  2. headers sent with the request 
  3. URL i.e resource asked by the client 
  4. access_route : lists all the ip addresses for the requests that are forwarded multiple times 
  5. full_path : that represents complete paths of request that including any queries string 
  6. is_secure : is true of the client makes the request using https or wss protocol 
  7. is_json : is true if request contains json data 
  8. cookies : cookies dictionry contains any cookie that sent with the request 

  * header contains the following data :
   1. Cache-Control : holds infomation on how to cache browsers 
   2. Accept : informs the browser what kind of content is understood by the client 
   3. Accept-Encoding : indicates the code content 
   4. User-Agent : identifies the client , application , Operating system  or version 
   5. Accept-Language : for specific language and local 
   6. Host : Specifies the host and requested server 

 you can replace the request object with custome request Object 
 which is usally optional  

 some common methods are:
 1. get_data: Get POST data from the request as bytes , then your are responsible for parsing this data 
 2. get_JSON : Parses POST data from the request as JSON data 

 Parse Request Data 
 * there are multiple ways to get parsed data depending on what is comming in with a request 
  * args: MultiDict[str,str] : give you query parameters as a dictionary 
  JSON : Optional[Any] ,will parse the dict in JSON 
  files : ImmutableMultiDict[str,FileStorage]   
  form : ImmutableMultiDict[str, str] , all values submmitted in form 
  values : ComninedMultiDict[str,str] , combines the args data with the form data 

  Access Values 
  * how to extract specific values from that data 
  you can do this using INDEXING or the GET method as all the above DS are like dictionary 

  ex :
   http://localhost:5000?course=capstone&rating=10 : from this url we have to extract information
   
   from flask import Flask , request 
   app=Flask(__name__)

   @app.route("/")
   def hello():
     course= request.args["course"]
     rating= request.args.get("rating")
     return {"message":f"{course} with rating {rating}"}


 ***Response Object is similar to Request Object and works same you can leverage 

 some common attribute are:
 1.status code: indicates success or failure of the request 
 2.headers : give more information about the response 
 3.content_type : shows the content type of the requested resource 
 4.content_length : is the size of the content response body 
 5.content_encoding : any encoding applied to the response so the client knows how to decode the data 
 6. mimetype : sets the media type of the response 
 7. expires : data and time after which the response is considered expire 

 * some standard methods on response objects 
 1. set_cookie : sets a browser cookie on the client 
 2. delete_cookie : deletes the cookie on the client 

 *** usage of flask on response object 
 Success  response  from @app.route method 

 1.JSONify method :also creates response object automatically 
 2.make_response: to create custome response 
 3.redirect : to return specifi 300 status code and redirect client to another url 
 4.abort : return a response with a error condition 


 *** DYNAMIC ROUTES 
 how to call an external api in flask 
 how to pass parameter to routes in flask


 *** Calling an External API's 
 can call external apis using the python request library  
 1. Return JSON as a dictionary to the caller   
"""
#http://localhost:5000?course=capstone&rating=10 : from this url we have to extract information
   
from flask import Flask , request 
app=Flask(__name__)
@app.route("/")
def hello():
  course= request.args["course"]
  rating= request.args.get("rating") # here if using the indexing it returns null if not present & with get method it stops the execution and throws 400 status code with bad request
  return {"message":f"{course} with rating {rating}"}


from flask import Flask , escape
import requests
app=Flask(__name__)
@app.route("/")
def getauthor():
  res=requests.get("http://openlibrary.org/search/authors.JSON?q=Michael Crichton")
  if res.status_code == 200:
    return {"Message":res.JSON()}
  elif res.status_code == 404:
    return {"Message":"something went wrong"},404
  else:
    return {"Message":"Server Error!"},500