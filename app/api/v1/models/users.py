from flask_restful import reqparse

USERS = []

class Helper():
    def signup_user(self):
        user ={
            "id" : len(USER)+1, 
           "firstname" : request.json["firstname"],
           "lastname" : request.json["lastname"],
           "email" : request.json["email"],
           "phoneNumber" : request.json["phoneNumber"],
           "username" : request.json["username"], 
           "password": request.json["password"],
           "registered" : datetime.datetime.now,
           "isAdmin" : False,
        }
        USERS.append(user)
        return {"status":201, "data": USERS, "message":"User successfully created"}

    def login_user(self, user_id):
        for user in USERS:
            if user["id"]= user_id:
                if user["password"]== request.json["password"]:
                    return {"status": 200, "message":"successful"}
                else:
                    return {"status": 401, "message": "wrong credntials!"}
            else:
                return {"status":404, "message": "user not found"}
