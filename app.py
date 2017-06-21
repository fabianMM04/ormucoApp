from flask import Flask, request, render_template, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import db, Person
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/mydatabase'

'''
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()
'''

migrate= Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

@app.route('/', methods=['GET', 'POST'])
def newPerson():

    if request.method == 'POST':
        newPerson = Person(name=request.form['name'],  favorite_color=request.form['favorite_color'], cats_or_dog=request.form['cats_or_dog'])
        db.session.add(newPerson)
        db.session.commit()
        return redirect(url_for('showPeople'))
    else:
        return render_template('newperson.html')


@app.route('/people')
def showPeople():
    items = Person.query(Person).all()
    return render_template('showpeople.html', items=items)

@app.route('/person/<int:person_id>/edit',methods=['GET', 'POST'])
def editPerson(person_id):

    editedPerson = db.session.query(Person).filter_by(id=person_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedPerson.name = request.form['name']
        if request.form['favorite_color']:
            editedPerson.favorite_color = request.form['favorite_color']
        if request.form['cats_or_dog']:
            editedPerson.cats_or_dog = request.form['cats_or_dog']
        db.session.add(editedPerson)
        db.session.commit()
        return redirect(url_for('showPeople'))
    else:

        return render_template('editperson.html',item=editedPerson)

@app.route('/person/<int:person_id>/delete',methods=['GET', 'POST'])
def deletePerson(person_id):

    itemToDelete = db.session.query(Person).filter_by(id=person_id).one()
    if request.method == 'POST':
        db.session.delete(itemToDelete)
        db.session.commit()
        return redirect(url_for('showPeople'))
    else:
        return render_template('deleteperson.html', item=itemToDelete)

if __name__ == '__main__':
    manager.run()
    
