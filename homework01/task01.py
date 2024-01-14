"""
Создать базовый шаблон для всего сайта, содержащий
общие элементы дизайна (шапка, меню, подвал), и
дочерние шаблоны для каждой отдельной страницы.
Например, создать страницу "О нас" и "Контакты",
используя базовый шаблон.

"""
from flask import Flask
from flask import render_template 

html = """
<h1>Моя первая HTML страница</h1>
<p>Привет, мир!</p>
"""
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

if __name__ == "__main__":
    app.run()