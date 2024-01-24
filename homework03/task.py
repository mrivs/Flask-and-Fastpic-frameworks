'''
## homework03
Задание

Создать форму для регистрации пользователей на сайте. Форма должна содержать поля "Имя", "Фамилия", "Email", "Пароль" и кнопку "Зарегистрироваться". При отправке формы данные должны сохраняться в базе данных, а пароль должен быть зашифрован.
'''
import secrets
from flask_wtf.csrf import CSRFProtect

from flask import Flask, flash, request, make_response, render_template, redirect, url_for

from models import db, User, hash_password
from forms import RegistrationForm


app=Flask(__name__)
# app.secret_key = 
app.config['SECRET_KEY'] =secrets.token_hex()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
csrf=CSRFProtect(app)

db.init_app(app)

 
@app.get('/')
def main_get():
  form=RegistrationForm()
  context={"title":"Подписка","info":" @app.get('/') "}
  return render_template('main.html', form=form, **context)

@app.post('/add_user/')
def main_post():
  form=RegistrationForm()
  if form.validate():
    my_first_name =form.first_name.data
    my_second_name=form.second_name.data
    my_email = form.email.data
    my_password = hash_password(form.email.data+form.password.data)
    
    user = User(first_name=my_first_name,second_name=my_second_name, email=my_email,password=my_password)
    
    db.session.add(user)
    db.session.commit()
    
    response = make_response(redirect('/success_hello'))
    return response
  return render_template('main.html', form=form)

  

@app.get('/success_hello/')
def success_hello():
  context={"title":"Пользователь добавлен в БД!","info":" @app.get('/success_hello/') "}
  return render_template('hello.html',**context)

@app.route('/about/')
def about_():
    context={"title":"О нас","info":" @app.route('/about/') "}
    return render_template('about.html', **context)
  

@app.post('/return/')
def return_to_main():
  response=make_response(redirect(url_for('main_get')))
  return response

@app.cli.command("init-db")
def init_db():
    db.create_all()
    print('db created')

@app.cli.command("add-john")
def add_user():
  user = User(first_name='john',second_name='Smith', email='john@example.com',password="1234")
  db.session.add(user)
  db.session.commit()
  print('John add in DB!')
  
  
if __name__ == "__main__":
  with app.app_context():
        db.create_all()
  app.run(debug=True)
   
    