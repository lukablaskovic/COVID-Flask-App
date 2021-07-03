from flask import Flask, render_template, flash, redirect, url_for
from forms import enterForm
import mysql.connector
import os
# za koristenje potrebno instalirati mySQL Connector (pip install mysql-connector-python)
app = Flask(__name__)

key = os.urandom(12)
app.config['SECRET_KEY'] = key

# Spajanje na mySQL bazu podataka
# Podaci se izmjenjuju ovisno o korisničkom imenu i lozinci
# DEFAULT je user: root, bez passworda
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="db_korona"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM podaci;")
prikaz = mycursor.fetchall()
# fetchall() metoda vraća Python listu svih redaka zadnjeg upita
# fetchone() metoda vraća prvi redak zadnjeg upita


@app.route("/")
@app.route("/about")
def home():
    return render_template('about.html', title='o projektu')


@app.route("/prikaz")
def about():
    return render_template('prikaz.html', title='prikaz podataka', podaci=prikaz)


@app.route("/unos", methods=['GET', 'POST'])
def unos():
    form = enterForm()
    if form.validate_on_submit():
        # Flash message = generira poruku nakon validacije forme
        flash('Uspješno unesen - {} {}!'.format(form.ime.data, form.prezime.data), 'success')
        # Insert u MySQL bazu podataka
        template1 = "INSERT INTO test (datum_testiranja,zarazen) VALUES (%s, %s)"
        data1 = (form.datum_testiranja.data, form.pozitivan.data)
        mycursor.execute(template1, data1)

        template2 = "INSERT INTO osoba (ime,prezime,oib,grad,test_id) VALUES (%s,%s,%s,%s,%s)"
        data2 = (form.ime.data, form.prezime.data, form.oib.data, form.grad.data, mycursor.lastrowid)
        mycursor.execute(template2, data2)

        mydb.commit()
        return redirect(url_for('about'))
    print(form.errors)
    return render_template('unos.html', title='unos pacijenta', form=form)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=1)
