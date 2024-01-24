from flask_sqlalchemy import SQLAlchemy
import hashlib
from datetime import datetime
db = SQLAlchemy()
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), unique=False,
    nullable=False)
    second_name = db.Column(db.String(80), unique=False,
    nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=False)
    password=db.Column(db.String(80), unique=False, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    


def hash_password(password):
    # Хэширование пароля с применением алгоритма SHA-256
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    return hashed_password

# # Пример использования
# password = "my_password"
# hashed_password = hash_password(password)
# print(hashed_password)

  
def __repr__(self):
    return f'User({self.username}, {self.email})'