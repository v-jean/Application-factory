from . import db

class Brand(db.Model):
    __tablename__ = "brands"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=True)
    cars = db.relationship("Cars", backref="brand")

    def __repr__(self):
        return "<Brand object %s>" % self.name

class Car(db.Model):
    __tablename__ = "cars"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), unique=True, index=True)
    brand_id = db.Column(db.Integer, db.ForeignKey("brands.id"))

    def __repr__(self):
        return "<Car object %s>" % self.name