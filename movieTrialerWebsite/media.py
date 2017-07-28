
class Media():
    ''' Media basic inforamtion. '''

    def __init__(self, title, storyline, posterImage, trailerYoutube):
        self.title = title
        self.storyline = storyline
        self.posterImage = posterImage
        self.trailerYoutube = trailerYoutube


class Movie(Media):
    ''' This is class provides a way to store movie related information. '''

    def __init__(self, title, storyline, posterImage, trailerYoutube, castYear):
        Media.__init__(self, title, storyline, posterImage, trailerYoutube)
        self.castYear = castYear


class TVShow(Media):
    ''' This is class provides a way to store TV show related information. '''

    def __init__(self, title, storyline, posterImage, trailerYoutube, seasonNumber):
        Media.__init__(self, title, storyline, posterImage, trailerYoutube)
        self.seasonNumber = seasonNumber
