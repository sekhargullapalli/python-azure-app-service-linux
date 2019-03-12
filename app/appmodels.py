from app import db

class Countries (db.Model):
    """
    Countries model defined according the json format @
    https://github.com/cristiroma/countries/blob/master/data/json/countries.json
    """
    __tablename__='Countries'

    id = db.Column(db.Integer, primary_key=True)
    enabled = db.Column(db.Boolean, nullable=False)
    code31 = db.Column(db.String(3), nullable=False)
    code21 = db.Column(db.String(3), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    name_official = db.Column(db.String(200), nullable=False)
    flag_32 = db.Column(db.String(200), nullable=False)
    flag_128 = db.Column(db.String(200), nullable=False)
    latitude = db.Column(db.String(200))
    longitude = db.Column(db.String(200))
    zoom = db.Column(db.Integer)

    def __repr__(self):
        return '{}:{}'.format(self.id, self.name)




   


