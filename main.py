from flask import Flask,render_template, request
from datetime import datetime
from werkzeug import secure_filename
from werkzeug.datastructures import ImmutableMultiDict
app = Flask(__name__)
#import sub
#import numpy



@app.route('/')
def hello_world():
  return  render_template("upload.html")

@app.route('/hello', methods = ['POST','GET'])
def hello_world1():
  if request.method == 'POST':
    
    file = request.form
    
  
    return  render_template("frontpage.html","file")


if __name__ == '__main__':
  app.run()
