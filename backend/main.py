#CRUD APP
#we ill be building our api here

from flask import request, jsonify
from config import app, db
from models import Contact

#gets all all our contacts 
#W need a decorator on top of any function call for routes
#This ia decorator, "/contacts" is the root url we want to go to, and method of GET will be used to access a resource
@app.route("/contacts", methods = ["GET"])
def get_contacts():
    #This will query all our contacts, will give us a list of all our contacts
    #These contacts are python objects, cannot output this so we need to conver them into json
    contacts = Contact.query.all()
    #This converts each of our python obbject contacts to json format - The function we made in models.py
    #This puts the contacts now in a new list, but it still actually returns a map even though its in right format now so we convert to a lsit
    #Essntially a list of all the contacts in a new list
    json_converted_contacts = map(lambda each_contact : each_contact.to_json(), contacts)
    json_contacts = list(json_converted_contacts)
    #convert these into json , and return a json object - we have our python dictionary object that we convert to json data 
    return jsonify({"contacts" : json_contacts})

    
    
 #create a new contact 
@app.route("/create_contact", methods = ["POST"])
def create_contact():
    #checks to see value that user had put in from the front end, and assigns the value to the variable
    first_name = request.json.get("firstName")
    last_name = request.json.get("lastName")
    email = request.json.get("email")
    
    if not first_name or not last_name or not email:
        return (
            jsonify({"message" : "Fields are incomplete"}), 400,
        )
    
    #if all fields are completed, make a new contactwith the paramets of contact class
    new_contact = Contact(first_name = first_name, last_name = last_name, email = email)
    
    #add the contact to the db and commit the addition
    try:
        db.session.add(new_contact)
        db.session.commit()
    except Exception as e:
        return jsonify({"message" : str(e)}), 400 #Bad request or can use 404
    
    
    #message of success
    return jsonify({"message" : "User Created"}), 201 #use for success in creation



#update
@app.route("/update_contact/<int:user_id>", methods = ["PATCH"])
def update_contact(user_id):
    
    contact = Contact.query.get(user_id)
    
    if not contact:
        return jsonify({"message" : "Contact not found"}), 404
    
    #what the user sends in the request, we are parsing through it
    data = request.json
    
    contact.first_name = data.get("firstName", contact.first_name)
    contact.last_name = data.get("lastName", contact.last_name)
    contact.email = data.get("email", contact.email)
    
    
    db.session.commit()
    
    
    return jsonify({"message" : "User information has been updated"}), 200 #success for  retreive (read, get) or update


#Delete
@app.route("/delete_contact/<int:user_id>", methods = ["DELETE"])
def delete_contact(user_id):
    
    contact = Contact.query.get(user_id)
    
    if not contact:
        return jsonify({"message" : "Contact not found"}), 401 #bad request
    
    db.session.delete(contact)
    db.session.commit()
    
    return jsonify({"message" : "User deleted"}), 200




# THIS IS MY CUSTOM BACKEND API CONNECTED TO OUR DB


    
    
    




#If we are in the main.py file, then run this indented code

#if statement is used for: incase main.py is called into another file, app.run() will not execute
if __name__ == "__main__":
    #we need to initalize our Db models that we want our sb to have
    #Overall its do we nave a database, if not lets go and create it for our application
    #This will get the context of our application 
    with app.app_context():
        #This will create our db with the models we made from models.py which db contains
        db.create_all()
    
    #This will run our code
    app.run(debug=True)