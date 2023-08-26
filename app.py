from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, IntegerField, DecimalField, BooleanField, DateField, DateTimeField, SelectField, SelectMultipleField, FileField, HiddenField, SubmitField, FormField, FieldList
from wtforms.validators import DataRequired


app = Flask(__name__)
app.secret_key = 'your_secret_key'


class MyForm(FlaskForm):
   string_field = StringField('String Field', validators=[DataRequired()])
   textarea_field = TextAreaField('Textarea Field', validators=[DataRequired()])
   password_field = PasswordField('Password Field', validators=[DataRequired()])
   integer_field = IntegerField('Integer Field', validators=[DataRequired()])
   decimal_field = DecimalField('Decimal Field', validators=[DataRequired()])
   boolean_field = BooleanField('Boolean Field')
   date_field = DateField('Date Field', format='%Y-%m-%d')
   datetime_field = DateTimeField('DateTime Field', format='%Y-%m-%d %H:%M:%S')
   select_field = SelectField('Select Field', choices=[('option1', 'Option 1'), ('option2', 'Option 2')])
   select_multiple_field = SelectMultipleField('Select Multiple Field', choices=[('option1', 'Option 1'), ('option2', 'Option 2')])
   file_field = FileField('File Field')
   hidden_field = HiddenField('Hidden Field')
   submit_field = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def form_submission():
   form = MyForm()
   if request.method == 'POST' and form.validate_on_submit():
       string_field_value = form.string_field.data
       textarea_field_value = form.textarea_field.data
       password_field_value = form.password_field.data
       integer_field_value = form.integer_field.data
       decimal_field_value = form.decimal_field.data
       boolean_field_value = form.boolean_field.data
       date_field_value = form.date_field.data
       datetime_field_value = form.datetime_field.data
       select_field_value = form.select_field.data
       select_multiple_field_value = form.select_multiple_field.data
       file_field_value = form.file_field.data
       hidden_field_value = form.hidden_field.data
      
       return 'Form submitted successfully!'
   return render_template('form.html', form=form)


if __name__ == '__main__':
   app.run(debug=True)
   app.run(host = '0.0.0.0', port=8080, debug =True)
