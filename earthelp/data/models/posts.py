from datetime import datetime
from earthelp.data.models.users import *
from earthelp import db

class Posts(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable= False)
    date_posted = db.Column(db.DateTime, nullable= False, default=datetime.utcnow())
    content = db.Column(db.Text, nullable= False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable= False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
    