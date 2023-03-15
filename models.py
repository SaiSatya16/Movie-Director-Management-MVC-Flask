from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Director(db.Model):
    d_id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(50), nullable = False)
    films = db.relationship('Movie', backref = "creator", secondary = "association")

    def __repr__(self):
        return f"<director {self.name}>"

class Movie(db.Model):
    m_id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(50), nullable = False)
    #creator = db.relationship('Director', backref = "films")


    def __repr__(self):
        return f"<movie {self.name}>"
    
class Association(db.Model):
    director_id = db.Column(db.Integer(),db.ForeignKey("director.d_id"),primary_key = True)
    movie_id = db.Column(db.Integer(),db.ForeignKey("movie.m_id"),primary_key = True)

