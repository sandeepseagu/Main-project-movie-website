class Movie():
  def __init__(self,movie_title,movie_storyline,movie_poster_url,trailer_youtube_url):
    self.title= movie_title
    self.storyline= movie_storyline
    self.poster_image_url=movie_poster_url
    self.trailer_youtube_url=trailer_youtube_url
    


  def show_trailer():
    webbroswer.open(self.trailer_youtube_url)
    
