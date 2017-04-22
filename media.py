
""" This module provides media classes to be instaintiated for the fresh_tomatoes.py """


class Movie():
    """This class holds all the properties relevant to a movie and
       initializes them via constructor"""

    def __init__(self, title, movie_storyline, poster_image_url, trailer_youtube_url):
        self.title = title
        self.movie_storyline = movie_storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
