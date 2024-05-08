from wsgiref.simple_server import make_server
import falcon

from fh.aalen.video.VideoController import VideoController
from fh.aalen.video.VideoRessource import VideoRessource
from fh.aalen.person.PersonRessource import PersonRessource
from fh.aalen.person.PersonController import PersonController

#create the falcon app
app = application = falcon.App()

#Instantiate the Ressources
vres = VideoRessource()
pres = PersonRessource()

#Initalize the controllers
vc = VideoController(app, vres)
pc = PersonController(app, pres)

#Start a webserver on port 8080
if __name__ == '__main__':
    with make_server('', 8080, app) as httpd:
        print('Serving on port 8080...')

        # Run as server until process is killed
        httpd.serve_forever()
