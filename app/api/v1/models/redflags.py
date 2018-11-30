from flask import request, jsonify
import datetime
REDFLAGS = []


class Helper():
    def get_all_redflags(self):
        return jsonify({"status": 200, "data": REDFLAGS, "message": "All redflags found successfully"})

    def post_redflag(self):
        args = request.get_json()

        REDFLAG = {
            "redflag_id": len(REDFLAGS)+1,
            "createdOn": str(datetime.datetime.now()),
            "modifiedOn": str(datetime.datetime.now()),
            "createdBy": args["createdBy"],
            "type": args["type"],
            "title": args["title"],
            "images": args["images"],
            "video": args["video"],
            "location": args["location"],
            "status": args["status"],
            "description": args["description"]
        }
        REDFLAGS.append(REDFLAG)
        return jsonify({"status": 201, "data": REDFLAG, "message": "Redflag posted successfully!"})

    def get_redflag(self, id):
        REDFLAG = [REDFLAG for REDFLAG in REDFLAGS if REDFLAG['redflag_id'] == id]
        if len(REDFLAG) == 0:
            return jsonify({"status": 404, "message": "Redflag not found"})
        else:
            return jsonify({"status": 200, "data": REDFLAG, "message": "Redflag successfully retrieved!"})

    def edit_redflag(self, id):
        REDFLAG = [REDFLAG for REDFLAG in REDFLAGS if REDFLAG['redflag_id'] == id]
        if len(REDFLAG) == 0:
            return jsonify({"status": 404, "message": "Redflag not found"})
        else:
            REDFLAG["title"] = request.json["title"]
            REDFLAG["type"] = request.json["type"]
            REDFLAG["modifiedOn"] = str(datetime.datetime.now())
            REDFLAG["images"] = request.json["images"]
            REDFLAG["video"] = request.json["video"]
            REDFLAG["location"] = request.json["location"]
            REDFLAG["description"] = request.json["description"]
            return jsonify( {"status":204, "data": REDFLAG ,"message": "Redflag updated successfully!"})

    def delete_redflag(self, id):
        REDFLAG = [REDFLAG for REDFLAG in REDFLAGS if REDFLAG['redflag_id'] == id]
        if len(REDFLAG) == 0:
            REDFLAGS.remove(REDFLAG[0])
            return jsonify({"status":204, "message":"Redflag successfuly deleted"})
        else:
            return jsonify({"status": 404, "message": "Redflag not found"})


    def edit_comment(self, id):
        REDFLAG = [REDFLAG for REDFLAG in REDFLAGS if REDFLAG['redflag_id'] == id]
        if len(REDFLAG) == 0:
            [{ "op": "replace", "path": "/comment", "value": request.json["description"] }]
            # REDFLAG["description"] = request.json["description"]
            return {"status": 204, "message": "comment successfully updated"}
        else:
            return {"status": 404, "message": "Redflag not found"}

        