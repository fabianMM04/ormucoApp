from flask import Flask, request, render_template, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base, Person
app = Flask(__name__)


engine = create_engine('sqlite:///lista_herramienta.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/', methods=['GET', 'POST'])
def newPerson():

    if request.method == 'POST':
        newPerson = Person(
            name=request.form['name'],  favorite_color=request.form['favorite_color'], cats_or_dog=request.form['cats_or_dog'])
        session.add(newPerson)
        session.commit()
        return redirect(url_for('showPeople'))
    else:
        return render_template('newperson.html')


@app.route('/people')
def showPeople():
    items = session.query(Person).all()
    return render_template('showpeople.html', items=items)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)