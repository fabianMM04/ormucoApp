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

@app.route('/person/<int:person_id>/edit',methods=['GET', 'POST'])
def editPerson(person_id):

    editedPerson = session.query(Person).filter_by(id=person_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedPerson.name = request.form['name']
        if request.form['favorite_color']:
            editedPerson.favorite_color = request.form['favorite_color']
        if request.form['cats_or_dog']:
            editedPerson.cats_or_dog = request.form['cats_or_dog']
        session.add(editedPerson)
        session.commit()
        return redirect(url_for('showPeople'))
    else:

        return render_template('editmenuitem.html',item=editedPerson)

@app.route('/person/<int:person_id>/delete',methods=['GET', 'POST'])
def deletePerson(person_id):

    itemToDelete = session.query(Person).filter_by(id=person_id).one()
    if request.method == 'POST':
        session.delete(itemToDelete)
        session.commit()
        return redirect(url_for('showPeople'))
    else:
        return render_template('deleteperson.html', item=itemToDelete)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)