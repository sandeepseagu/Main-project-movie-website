import media
import fresh_tomatoes
toy_story=media.Movie("TOY STORY"," A story of boy and his toys",
                       "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg"
                       ,"https://www.youtube.com/watch?v=KYz2wyBy3kc")
ben_hur=media.Movie("BEN HUR"," story of prince with jesus","https://upload.wikimedia.org/wikipedia/commons/thumb/7/74/Ben_hur_1959_poster.jpg/800px-Ben_hur_1959_poster.jpg","https://www.youtube.com/watch?v=4hrbRDAOF4k")


harry_potter=media.Movie("Harry Potter"," story of a magical boy",
                         "https://upload.wikimedia.org/wikipedia/en/3/3f/Harry_Potter_and_the_Half-Blood_Prince_poster.jpg",
                         "https://www.youtube.com/watch?v=K1KPcXRMMo4")

transfomers=media.Movie("TRANSFOMERS"," Autoboats on earth","https://upload.wikimedia.org/wikipedia/en/2/26/Transformers_The_Last_Knight_poster.jpg","https://www.youtube.com/watch?v=dxQxgAfNzyE")
rainman=media.Movie("RAINMAN","brothers relationship","https://upload.wikimedia.org/wikipedia/en/b/b2/Rain_Man_poster.jpg","https://www.youtube.com/watch?v=KKC3W0awjm0")

movies=[toy_story,ben_hur,harry_potter,transfomers,rainman]
fresh_tomatoes.open_movies_page(movies)

