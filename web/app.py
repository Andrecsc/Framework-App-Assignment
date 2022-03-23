from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from logic.person import Person
from logic.document import Document

app = Flask(__name__)
bootstrap = Bootstrap(app)
model = []
model_doc = []


@app.route("/")
def index():
    return render_template('index.html')


# person
@app.route('/person', methods=['GET'])
def person():
    return render_template('person.html')


@app.route('/person_detail', methods=['POST'])
def person_detail():
    id_person = request.form['id_person']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    p = Person(id_person=id_person, name=first_name, last_name=last_name)
    model.append(p)
    return render_template('person_detail.html', value=p)


@app.route('/people')
def people():
    data = [(i.id_person, i.name, i.last_name) for i in model]
    print(data)
    return render_template('people.html', value=data)


# document
@app.route('/document', methods=['GET'])
def document():
    return render_template('document.html')


@app.route('/document_detail', methods=['POST'])
def document_detail():
    ID = request.form['ID']
    title = request.form['title']
    number_pages = request.form['number_pages']
    category = request.form['category']
    authors = request.form['authors']
    d = Document(ID=ID, title=title, number_pages=number_pages, category=category, authors=authors)
    model_doc.append(d)
    return render_template('document_detail.html', value=d)


@app.route('/documents')
def documents():
    data = [(i.ID, i.title, i.number_pages, i.category, i.authors) for i in model_doc]
    print(data)
    return render_template('documents.html', value=data)


if __name__ == '__main__':
    app.run()  # (debug = True?)
