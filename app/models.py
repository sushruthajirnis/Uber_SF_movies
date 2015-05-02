from app import db

class Film_location(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100),index=True)
    year_released=db.Column(db.Integer)
    location=db.Column(db.String(120))

    def __repr__(self):
        return  "Film location of movie {}\
                is {}".format(self.title,self.location)
