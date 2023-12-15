from jinja2 import Environment, FileSystemLoader

f_template = open('task2.html', 'r', encoding='utf-8-sig')
html = f_template.read()
f_template.close()

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('task2.html')

books = {
     "title": ["Мастер и Маргарита", "Белая гвардия", "Война и мир", "Анна Каренина", "Игрок"],
     "author": ["Булгаков М.А.", "Булгаков М.А.", "Толстой Л.Н.", "Толстой Л.Н.", "Достоевский Ф.М."],
     "price": [581.50, 600.00, 899.99, 450.10, 234.55]
}

result_html = template.render(books=books, first_card=3, last_card=2)

f = open('exit.html', 'w', encoding='utf-8-sig')
f.write(result_html)
f.close()
