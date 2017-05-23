from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired

class CarForm(FlaskForm):
    model = StringField('model', validators=[DataRequired()])
    owner_id = IntegerField('owner id', validators=[DataRequired()])
