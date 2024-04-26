from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


# initializes the flask application
app = Flask(__name__)

#To be able to send request from the frontend to the backend, we need to wrap our application in CORS
#This will take care of the CORS error when trying to communicate requests between frontend & the backend 
CORS(app)

#configure our DB 
#done using the sql_alchemy library, the first line confiries the db we want to use, and we speficy we are not tracking db changes

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabse.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

#Create the db instance for the app, this will give us access tothe DB we have create above 
#This instance now will allow us to peform our CRUD operations

db = SQLAlchemy(app)





#jdbc connecter to connect already made db's 