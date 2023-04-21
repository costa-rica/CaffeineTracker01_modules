from .modelsBase import Base, sess
from sqlalchemy.orm import sessionmaker, Session, relationship
from sqlalchemy import Column, Integer, String, Text, Float, DateTime, ForeignKey, \
    Date, Boolean, Table
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from datetime import datetime
from flask_login import UserMixin
from .config import config
import os


def default_username(context):
    return context.get_current_parameters()['email'].split('@')[0]


class Users(Base, UserMixin):
    __tablename__ = 'users'
    id = Column(Integer, primary_key = True)
    email = Column(Text, unique = True, nullable = False)
    password = Column(Text, nullable = False)
    username = Column(Text, default=default_username)
    admin = Column(Boolean, default=False)
    time_stamp_utc = Column(DateTime, nullable = False, default = datetime.utcnow)
    caffeine_log = relationship('CaffeineLog', backref='caffeine_log_ref', lazy=True)

    def get_reset_token(self, expires_sec=1800):
        s=Serializer(config.SECRET_KEY, expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s=Serializer(config.SECRET_KEY)
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return sess.query(Users).get(user_id)

    def __repr__(self):
        return f'Users(id: {self.id}, email: {self.email}, username: {self.username})'


class CaffeineLog(Base):
    __tablename__ = 'caffeine_log'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey("users.id"))
    drink_type = Column(Text)
    latitude = Column(Float(precision=6, decimal_return_scale=None))
    longitude = Column(Float(precision=6, decimal_return_scale=None))
    public = Column(Boolean, default=False)
    uuid = Column(Text)
    time_stamp_utc = Column(DateTime, nullable = False, default = datetime.utcnow)


    def __repr__(self):
        return f'CaffeineLog(id: {self.id}, user_id: {self.user_id}, drink_type: {self.drink_type},' \
        f'lat: {self.lat}, lon: {self.lon})'


