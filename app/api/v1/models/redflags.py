from flask import request, jsonify
import datetime
REDFLAGS = []


class RedflagsModel():
    def get_all_redflags(self):
        return REDFLAGS

    def post_redflag(self):
        args = request.get_json()
        RED-FLAG = [REDFLAG for REDFLAG in REDFLAGS if REDFLAG['description'] == args["description"]]
        if len(RED-FLAG) != 0:
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
            return REDFLAG
        return None

    def get_redflag(self, id):
        REDFLAG = [REDFLAG for REDFLAG in REDFLAGS if REDFLAG['redflag_id'] == id]
        if len(REDFLAG) == 0:
            return None
        else:
            return REDFLAG

    def edit_redflag(self, id):
        REDFLAG = self.get_redflag(id)
        if REDFLAG:
            REDFLAG[0]["title"] = request.json["title"]
            REDFLAG[0]["type"] = request.json["type"]
            REDFLAG[0]["modifiedOn"] = str(datetime.datetime.now())
            REDFLAG[0]["images"] = request.json["images"]
            REDFLAG[0]["video"] = request.json["video"]
            REDFLAG[0]["location"] = request.json["location"]
            REDFLAG[0]["description"] = request.json["description"]
            return REDFLAG 
        else:
             return None

    def delete_redflag(self, id):
        REDFLAG = self.get_redflag(id)
        if REDFLAG:
            REDFLAGS.remove(REDFLAG[0])
            return REDFLAGS
        else:
            return None         


    def edit_comment(self, id):
        REDFLAG = self.get_redflag(id)
        if len(REDFLAG) != 0:
            REDFLAG[0]["description"] = request.json["description"]
            return REDFLAG          
        return None
        

    def edit_location(self, id):
        REDFLAG = self.get_redflag(id)
        if len(REDFLAG) != 0:
            REDFLAG[0]["location"] = request.json["location"]
            return REDFLAG          
        return None
        
    def upload_image(self, id):
        pass

    def upload_video(self,id):
        pass
            

        