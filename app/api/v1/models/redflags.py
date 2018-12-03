from flask_restplus import reqparse
import datetime
REDFLAGS = []


class Helper():
    def get_all(self):
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
            "images":args["image"],
            "video": args["video"],
            "location": args["location"],
            "status": "pending",
            "description": args["description"]
        }
        REDFLAGS.append(REDFLAG)
        return {"status": 201, "data": REDFLAG, "message": "Redflag posted successfully!"}
