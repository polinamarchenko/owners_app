from project import db

class Car(db.Model):
    __tablename__ = 'cars'

    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.Text, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('owners.id'))

    def __init__(self, model, owner_id):
        self.model = model
        self.owner_id = owner_id
