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

@app.route('/news/<int:num>/')
def get_news(num):

    base = [{'title':'title1', 'name': 'name1', 'date_pub': '2022'},
            {'title':'title2', 'name': 'name2', 'date_pub': '2023'},
            {'title':'title3', 'name': 'name3', 'date_pub': '2024'}
            ]
    context = base[num-1]
    print(context)
    return render_template('news.html', news=context)

if __name__ == "__main__":
    app.run()