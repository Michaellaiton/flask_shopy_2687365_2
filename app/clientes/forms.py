from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import InputRequired

class ClienteForm():
    username = StringField('Ingrese un usuario: ',
                           validators=[InputRequired(message="Debe ingresar un usuario!")])
    email = StringField('Ingrese una contraseña: ',
                              validators=[InputRequired(message="Debe registar una contraseña")])


class NewCustomerForm(FlaskForm,ClienteForm):
    password = PasswordField('Ingrese una contraseña: ',
                              validators=[InputRequired(message="Debe registar una contraseña")])
   
    submit = SubmitField('Registar')

class EditClienteForm(FlaskForm,ClienteForm):
    submit = SubmitField('Registrar')