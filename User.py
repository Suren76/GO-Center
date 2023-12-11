import flask_login.mixins as mixin
from sqlite3 import Row, Connection
from flask import Flask, url_for
from models import User, Profile


class UserLogin(mixin.UserMixin):
    __user: Row
    __profile: Row

    def __init__(self, user=None):
        self.create(user)

    def create(self, user):
        self.__user = user

    def fromDB(self, db: User, user_id=None, username=None):
        self.__user = User.query.get(user_id) if user_id is not None else User.query.filter_by(username=username).first_or_404()
        self.__profile = Profile.query.get(self.get_id())
        return self

    @property
    def profile(self):
        return self.__profile

    def get_avatar(self, app: Flask):
        img = None
        if not self.__profile.avatar:
            try:
                with app.open_resource(app.root_path + url_for('static', filename='img/profile-image.png')) as f:
                    img = f.read()
            except Exception as e:
                print(e)
        else:
            img = self.__profile.avatar

        return img

    def get_id(self):
        return str(self.__user.id)

    @property
    def user(self):
        return self.__user

    @staticmethod
    def verify_ext(filename: str):
        return filename.split(".")[1].lower() == "png"


class AnonymousUser(mixin.AnonymousUserMixin):
    pass
