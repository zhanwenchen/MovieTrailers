class Movie():
    """ ... this is the class documentation docstring ...
        class Movie has a title, a sotryline, a poster image and a trailer
        """
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        """ ... this is the constructor method docstring ...
            the constructor takes a title, a storyline, a poster image and a trailer
            and sets the respective fields
            """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
