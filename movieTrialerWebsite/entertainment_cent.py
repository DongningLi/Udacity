import media
import fresh_tomatoes

'''create threee medium'''
toy_story = media.Movie("Toy Story",
                        "A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him "
                        "as top toy in a boy's room.",
                        "https://images-na.ssl-images-amazon.com/images/M"
                        "/MV5BMDU2ZWJlMjktMTRhMy00ZTA5LWEzNDgtYmNmZTEwZTViZWJkXkEyXkFqcGdeQXVyNDQ2OTk4MzI@"
                        "._V1_SY1000_SX670_AL.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                        "1995")

friendsEpisode1 = media.TVShow("Friends",
                               "Follows the personal and professional lives of six 20 to 30-something-year-old friends"
                               " living in Manhattan.",
                               "https://images-na.ssl-images-amazon.com/images/M"
                               "/MV5BMTg4NzEyNzQ5OF5BMl5BanBnXkFtZTYwNTY3NDg4._V1._CR24,0,293,443_.jpg",
                               "https://www.youtube.com/watch?v=hDNNmeeJs1Q",
                               "Episode 1")

eatPrayLove = media.Movie("Eat Pray Love",
                          "A married woman realizes how unhappy her marriage really is,"
                          " and that her life needs to go in a different direction. After a painful divorce,"
                          " she takes off on a round-the-world journey to 'find herself'.",
                          "https://images-na.ssl-images-amazon.com/images/M"
                          "/MV5BMTY5NDkyNzkyM15BMl5BanBnXkFtZTcwNDQyNDk0Mw@@._V1_.jpg",
                          "https://www.youtube.com/watch?v=mjay5vgIwt4",
                          "2010")

'''call for pages'''
medium = [toy_story, friendsEpisode1, eatPrayLove]
fresh_tomatoes.open_movies_page(medium)
