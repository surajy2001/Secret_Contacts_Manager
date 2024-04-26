#started with making config environment/infastructure
#Here will be our databse models 

#Below is how we want our db to look, the fields and data types of how I want it to look

from  config import db


#All DB's will have an ID
#creating our columns for how our db will look and what it will hold
#parameters of our DB
# ID   F_N    L_N     Email
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(60), unique = False, nullable = False)
    last_name = db.Column(db.String(80), unique = False, nullable = False)
    email = db.Column(db.String(100), unique = True, nullable = False)
    

    #We now convert the contact fields into an json object so itll be easy o tak that contact and give it to the front end, or whoever is requesting to get our diff contacts
    #we need to convert these firlds to json so rewuests can be sent to api and back from frontend
    # This is how the users inuts will be read
    #converting db to json format, (looks like a python dictionary )
    
    #create a python dictioanry holding our db
    
    def to_json(self):
        return {
            "id" : self.id, 
            "firstName" : self.first_name,
            "lastName" : self.last_name, 
            "email" : self.email
        }
        
        
        
        