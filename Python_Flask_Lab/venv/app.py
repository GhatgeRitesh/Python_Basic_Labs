from flask import Flask ,jsonify
import requests
app=Flask(__name__)
@app.route("/")
def getauthor():
  res=requests.get("https://openlibrary.org/search/authors.json?q=twain")
  
  if res.status_code == 200:
         # Raises an HTTPError for bad responses (4xx or 5xx)
        data = res.json()  # Convert the response to JSON
        return jsonify(data) 
  elif res.status_code == 404:
    return {"Message":"content not found!"},404
  else:
    return {"Message":"Server Error!"},500
