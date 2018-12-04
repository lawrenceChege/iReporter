# """
#     This tests the intergration of redflags
# """
# from app.tests.v1.base import BaseTestCase
# from app.api.v1.models.redflags import RedflagsModel

# class TESTREDFLAG(BaseTestCase):
#     """
#         Tet for redflag intergration
#     """
#     incident = {
#         "title": "land grabbing",
#         "type":"redflag",
#         "status":"pending",
#         "description":" public school grounds grabbed",
#         "images":"updlods/land.jpg",
#         "videos":"upluads/land.mp4",
#         "location":"23.4E, 34.9N"
#     }

#     def test_crud(self):
#         """
#             This method tests for CRUD functionality of the class
#         """

#         redflag = RedflagsModel(**TESTREDFLAG.incident) 

#         self.assertIsNone( RedflagsModel().get_redflag(1)),
#         "Get a redflag with id '1' before saving"

#         redflag.post_redflag()

#         # self.assertEqual(redflag.get_redflag.type, 'redlag')
#         self.assertIsNotNone(RedflagsModel().get_redflag(1)),
#         "Did not find a redflag with"
#         "id '1' after post"
        
   