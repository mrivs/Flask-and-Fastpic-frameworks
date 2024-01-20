'''
## homework02 
Задание

Создать страницу, на которой будет
форма для ввода имени и электронной почты, 
при отправке которой будет создан cookie-файл с данными пользователя,
а также будет произведено перенаправление на страницу приветствия,
где будет отображаться имя пользователя.
На странице приветствия должна быть кнопка «Выйти», при нажатии на которую будет удалён cookie-файл с данными пользователя 
и произведено перенаправление на страницу ввода имени и электронной почты.
'''
import secrets
from flask import Flask, flash, request, make_response, render_template, redirect, url_for

app=Flask(__name__)
app.secret_key = secrets.token_hex()

 
@app.get('/')
def main_get():
  context={"title":"Подписка","info":" @app.get('/') "}
  return render_template('main.html',**context)

@app.post('/hello/')
def main_post():
  my_name = request.form.get('name')
  my_email= request.form.get('email')

  if not my_name:
    flash('Введите имя!', 'danger')
    return redirect(url_for('main_get'))
  if not my_email:
     flash('Введите почту!', 'danger')
     return render_template('main.html',username=my_name)
   
  response = make_response(redirect('/success_hello'))
  response.set_cookie('username', my_name)
  response.set_cookie('email', my_email)
  return response

@app.get('/success_hello/')
def success_hello():
  name = request.cookies.get('username')
  email= request.cookies.get('email')
  context={"title":"Hello","info":" @app.get('/success_hello/') ","name":name,"mal":email}
  return render_template('hello.html',**context)

@app.route('/about/')
def about_():
    context={"title":"О нас","info":" @app.route('/about/') "}
    return render_template('about.html', **context)
  

@app.post('/return/')
def return_to_main():
  response=make_response(redirect(url_for('main_get')))
  response.set_cookie("username","",expires=0)
  response.set_cookie("email","",expires=0)
  return response



if __name__ == "__main__":
    app.run()