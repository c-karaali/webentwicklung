import json
import falcon
from fh.aalen.person.PersonService import PersonService

class PersonRessource:

    def on_get_persons(self, req, resp):
        personlist = PersonService.get_persons();
        resp.text=json.dumps([v.to_dict() for v in personlist], ensure_ascii=False, indent=2)
        resp.status = falcon.HTTP_200

    def on_get_person(self, req, resp, id):
        resp.text=None
        v = PersonService.get_person(int(id))
        resp.text = json.dumps(v.to_dict(),  ensure_ascii=False, indent=2)
        resp.status = falcon.HTTP_200

    def on_post_persons(self, req, resp):
        #Return value is an object of type dict
        person_json = json.load(req.bounded_stream)
        PersonService.create_person(person_json)
        resp.text = "Person added successfully."
        resp.status = falcon.HTTP_OK
        resp.content_type = falcon.MEDIA_TEXT

    def on_put_persons(self, req, resp, id):
        person_json = json.load(req.bounded_stream)
        # Convert the dict to an object of the class video
        PersonService.update_person(id, person_json)
        resp.text = "Person updated successfully."
        resp.status = falcon.HTTP_OK
        resp.content_type = falcon.MEDIA_TEXT

    def on_delete_persons(self, req, resp, id):
        PersonService.delete_person(id)
        resp.text = "Person deleted successfully."
        resp.status = falcon.HTTP_OK
        resp.content_type = falcon.MEDIA_TEXT

    def on_get_addvideofavourite(self, req, resp, person_id, video_id):
        resp.text = None
        PersonService.add_video_to_favourites(video_id, person_id)
        resp.text = "Favourite connected successfully"
        resp.status = falcon.HTTP_200