from flask_sqlalchemy import SQLAlchemy
 
db = SQLAlchemy()
 
class Songs(db.Model):
    __tablename__ = 'data'
 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    album = db.Column(db.String())
    artist = db.Column(db.String())
    acousticness = db.Column(db.Float())
    danceability = db.Column(db.Float())
    energy = db.Column(db.Float())
    duration = db.Column(db.Float())
 
    def __init__(self, name,album,artist,acousticness,danceability,energy,duration):
        self.name = name
        self.album = album
        self.artist = artist
        self.acousticness = acousticness
        self.danceability = danceability
        self.energy = energy
        self.duration = duration

    def __repr__(self):
        return f"<Song {self.name!r}>"