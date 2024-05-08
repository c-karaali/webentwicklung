from fh.aalen.person.Person import Person
from fh.aalen.data.db_session import DBSession
from fh.aalen.video.Video import Video
from fh.aalen.relations.favours import Favours

class PersonService:

    #Helpermethod to create/update videos
    @classmethod
    def __json_to_video(cls, person, json_person):
        person.id = json_person['id']
        person.surename = json_person['surename']
        person.birthdate=json_person['birthdate']
        return person

    @classmethod
    def get_persons(cls):
        session = DBSession.get_session()
        personlist = session.query(Person).all()
        return personlist

    @classmethod
    def get_person(cls, id):
        session = DBSession.get_session()
        person = session.query(Person).get(id)
        return person

    @classmethod
    def create_person(cls, json_person):
        person = Person()
        persion = cls.__json_to_video(person, json_person)
        session = DBSession.get_session()
        session.add(person)
        session.commit()

    @classmethod
    def update_person(cls, id, json_person):
        session = DBSession.get_session()
        person = session.query(Person).get(int(id))
        cls.__json_to_video(person, json_person)
        session.commit()

    @classmethod
    def delete_person(cls, id):
        session = DBSession.get_session()
        person = session.query(Person).get(int(id))
        session.delete(person)
        session.commit()

    #New method to add a dependency
    @classmethod
    def add_video_to_favourites(cls, video_id, person_id):
        session = DBSession.get_session()
        fav = Favours()
        fav.video_vnr=video_id
        fav.person_id=person_id
        session.add(fav)
        session.commit()
