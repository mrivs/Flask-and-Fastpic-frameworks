"""
Задание
Создать базовый шаблон для интернет-магазина, содержащий общие элементы дизайна (шапка, меню, подвал), и дочерние шаблоны для страниц категорий товаров и отдельных товаров. Например, создать страницы «Одежда», «Обувь» и «Куртка», используя базовый шаблон.

"""
from flask import Flask
from flask import render_template 

app = Flask(__name__)

@app.route("/")
def main_():
    context={"title":"Главная"}
    return render_template('main.html', **context)

@app.route('/about/')
def about_():
    context={"title":"О нас"}
    return render_template('about.html', **context)

@app.route('/contacts/')
def contacts_():
    context={"title":"Контакты"}
    return render_template('contacts.html', **context)

@app.route('/clothes/')
def clothes_():
    context={"title":"Одежда"}
    return render_template('clothes.html', **context)

@app.route('/shoes/')
def shoes_():
    context={"title":"Обувь"}
    return render_template('shoes.html', **context)

@app.route('/coat/')
def coat_():
    context={"title":"Куртка"}
    return render_template('coat.html', **context)

@app.route('/jacket/')
def jacket_():
    context={"title":"Пиджак"}
    return render_template('jacket.html', **context)

if __name__ == "__main__":
    app.run()