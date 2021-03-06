from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from flask_login import UserMixin
from  . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'
              
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    password_hash = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
       
    @property
    def password(self):
        raise AttributeError('You cannnot read the password attribute')

    
    def set_password(self, password):

        self.password_hash = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f'User { self.username}'

    


class Pitch(UserMixin,db.Model):
   __tablename__='pitches'

   id = db.Column(db.Integer,primary_key=True)
   title = db.Column(db.String(255))
   pitch = db.Column(db.String(255))
   category = db.Column(db.String(255))
   comments = db.relationship('Comment',backref='pitch',lazy='dynamic')
   user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
   



   def save_pitch(self):
       db.session.add(self)
       db.session.commit()

class Comment(UserMixin,db.Model):
   __tablename__='comments'
   id = db.Column(db.Integer,primary_key=True)
   user_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
   comment = db.Column(db.String(255))
   username=db.Column(db.String(255))
