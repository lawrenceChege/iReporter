from flask_restplus import reqparse
import datetime
REDFLAGS = []


class Helper():
    def get_all_redflags(self):
        return {"status": 200, "data": REDFLAGS, "message": "All redflags found successfully"}

    def post_redflag(self):
        self.parser = reqparse.RequestParser()
        args = self.parser.parse_args()

        REDFLAG = {
            "id": len(REDFLAGS)+1,
            "createdOn": datetime,
            "createdBy": args["user"],
            "type": "RedFlag",
            "title": args["title"],
            "images":args["images"],
            "video": args["video"],
            "location": args["location"],
            "status": "pending",
            "description": args["description"]
        }
        REDFLAGS.append(REDFLAG)
        return {"status": 201, "data": REDFLAG, "message": "Redflag posted successfully!"}

    def get_redflag(self, redflag_id):
        for REDFLAG in REDFLAGS:
            if REDFLAG["id"] == redflag_id:
                return {"status": 200, "data": REDFLAG}
            else:
                return {"status": 404, "message": "Redflag not found"}

    def edit_redflag(self, redflag_id):
        for REDFLAG in REDFLAGS:
            if REDFLAG["id"] == redflag_id:
                REDFLAG["title"] = request.json["title"]
                REDFLAG["type"] = request.json["type"]
                REDFLAG["images"] = request.json["images"]
                REDFLAG["video"] = request.json["video"]
                REDFLAG["location"] = request.json["location"]
                REDFLAG["description"] = request.json["description"]
                return {"status":204, "data": REDFLAG ,"message": "Redflag updated successfully!"}

    def delete_redflag(self, redflag_id):
        for REDFLAG in REDFLAGS:
            if REDFLAG["id"] == redflag_id:
                REDFLAGS.remove(REDFLAG[0])
                return {"status":204, "message":"Redflag successfuly deleted"}


        