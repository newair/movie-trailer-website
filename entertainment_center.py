""" entertainment_center creates instances of movie classes from media file and list them.
 Then pass that array to fesh_tomatoes open_movies_page"""

import media
import fresh_tomatoes


def init_movies():
    """initializes movie objects"""

    avatar = media.Movie("Avatar",
                         "Avatar",
                         "http://t0.gstatic.com/images?q=tbn:ANd9GcQCfmvrE4fMo2cd8esc7mDZPtFSJThAujddMPkRtti1_ij6u-jp",  # pylint: disable=C0301
                         "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

    batman = media.Movie("Batman",
                         "Batman",
                         "https://upload.wikimedia.org/wikipedia/en/1/17/Batman-BenAffleck.jpg",
                         "https://www.youtube.com/watch?v=PIGCKbrCVc4")

    superman = media.Movie("Super Man",
                           "Super Man",
                           "https://upload.wikimedia.org/wikipedia/en/thumb/8/85/ManofSteelFinalPoster.jpg/220px-ManofSteelFinalPoster.jpg",  # pylint: disable=C0301
                           "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

    movies = [avatar, batman, superman]
    open_browser(movies)


def open_browser(movies):
    """open the browser and load the movies in given movies array"""
    fresh_tomatoes.open_movies_page(
        movies)  # call the fresh_tomatoes public open_movies_page


init_movies()
