class VideoController:

    def __init__(self, app, res):
        self.app=app
        self.res=res

        #Create the routes
        self.app.add_route('/videos', self.res, suffix='videos') #Calls method on_get_videos
        self.app.add_route('/video/{vnr}', self.res, suffix='video')  # Calls method on_get_video to get a single video by title and on_delete to delete a video
        self.app.add_route('/video', self.res, suffix='video')  # Calls method on_post_video


        self.app.add_route('/videosbygenre/{genre}', self.res, suffix='videosbygenre')
        self.app.add_route('/videosbyagerating/{agerating}', self.res, suffix='videosbyagerating')
        self.app.add_route('/videogenres', self.res, suffix='videogenres')

        # A route to a static content directory, e.g. html files
        self.app.add_static_route('/', '/Users/marcfernandes/PycharmProjects/VideoArchive3/')