from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, RadioField
from wtforms.validators import Length, InputRequired


class enterForm(FlaskForm):
    ime = StringField('Ime:', validators=[InputRequired("Molimo upišite ime!")])
    prezime = StringField('Prezime:', validators=[InputRequired("Molimo upišite prezime!")])
    oib = StringField('OIB:', validators=[InputRequired("Molimo upišite OIB!"),
                                          Length(min=11, max=11, message="OIB se mora sastojati od 11 brojeva!")])
    grad = StringField('Grad:', validators=[InputRequired()])
    datum_testiranja = DateField('Datum testiranja:', format='%d.%m.%Y', validators=[InputRequired()])
    pozitivan = RadioField('Label', choices=[('1', 'pozitivan'), ('0', 'negativan')], validators=[InputRequired()])
    submit = SubmitField('Unesi')
