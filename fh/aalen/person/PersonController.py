class PersonController:

    def __init__(self, app, res):
        self.app=app
        self.res=res

        #Create the routes
        self.app.add_route('/persons', self.res, suffix='persons')
        self.app.add_route('/person', self.res, suffix='person')
        self.app.add_route('/person/{id}', self.res, suffix='persons')
        self.app.add_route('/personfavourite/{person_id}/{video_id}', self.res, suffix='addvideofavourite')