from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TimeField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class MeetingRegistrationForm(FlaskForm):
    """Form for registering a new meeting"""

    meeting_subject = StringField('Meeting Subject', validators=[DataRequired()])
    date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()])
    start_time = TimeField('Start Time', validators=[DataRequired()])
    end_time = TimeField('End Time', validators=[DataRequired()])
    participants = TextAreaField('Participants')
    submit = SubmitField('Submit')


class MeetingUpdateForm(FlaskForm):
    """Form for updating an existing meeting"""

    meeting_id = StringField('Meeting ID', validators=[DataRequired()])
    new_subject = StringField('New Subject')
    new_date = DateField('New Date', format='%Y-%m-%d')
    new_start_time = TimeField('New Start Time')
    new_end_time = TimeField('New End Time')
    new_participants = TextAreaField('New Participants')
    submit = SubmitField('Update')
