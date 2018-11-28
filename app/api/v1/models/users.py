from flask_restful import reqparse

USERS = []

class Helper():
    def post_user():
        user ={
            "id" : len(USER)+1, 
           "firstname" : request.json["firstname"],
           "lastname" : request.json["lastname"],
           "email" : request.json["email"],
           "phoneNumber" : request.json["phoneNumber"],
           "username" : request.json["username"], 
           "registered" : datetime.datetime.now,
           "isAdmin" : False,
        }
        USERS.append(user)
        return {"status":201, "data": USERS, "message":"User successfully created"}