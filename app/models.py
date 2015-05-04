from app import db
import unicodedata

class Film_location(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100),index=True)
    year_released=db.Column(db.Integer)
    location=db.Column(db.String(120))
    latitude = db.Column(db.Float())
    longitude=db.Column(db.Float())

    def __repr__(self):
        return  "Film location of movie {}".format(self.title)\
               +" is {}".format(unicodedata.normalize('NFKD',self.location).encode('ascii','ignore'))
