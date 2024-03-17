from flask import Flask, render_template, request, redirect
from models import db, Meetings  # Assuming 'Meetings' is a SQLAlchemy model
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
db.init_app(app)


# Route for registering a new meeting
@app.route('/meeting/register', methods=['GET', 'POST'])
def meeting_register():
    if request.method == 'POST':
        # Gather data from the form
        subject = request.form['meeting_subject']
        date = request.form['date']
        start_time = request.form['start_time']
        end_time = request.form['end_time']
        participants = request.form['participants']

        # Create a new meeting object and add it to the database
        new_meeting = Meetings(subject=subject, date=date, start_time=start_time, end_time=end_time, participants=participants)
        db.session.add(new_meeting)
        db.session.commit()

        # Redirect to the list of meetings
        return redirect('/meetings')

    # Render the meeting registration form
    return render_template('meeting_registration.html')


# Route for updating an existing meeting
@app.route('/meeting/update/<int:meeting_id>', methods=['GET', 'POST'])
def meeting_update(meeting_id):
    # Fetch the meeting from the database based on its ID
    meeting = Meetings.query.get_or_404(meeting_id)

    if request.method == 'POST':
        # Update the meeting details based on the form data
        meeting.subject = request.form['new_subject']
        meeting.date = request.form['new_date']
        meeting.start_time = request.form['new_start_time']
        meeting.end_time = request.form['new_end_time']
        meeting.participants = request.form['new_participants']

        # Commit the changes to the database
        db.session.commit()

        # Redirect to the list of meetings
        return redirect('/meetings')

    # Render the meeting update form with the meeting details
    return render_template('meeting_update.html', meeting=meeting, meeting_id=meeting_id)


# Route for deleting a meeting
@app.route('/meeting/delete/<int:meeting_id>', methods=['GET', 'POST'])
def meeting_delete(meeting_id):
    # Fetch the meeting from the database based on its ID
    meeting = Meetings.query.get_or_404(meeting_id)

    if request.method == 'POST':
        # If the user confirms deletion, remove the meeting from the database
        db.session.delete(meeting)
        db.session.commit()
        return redirect('/meetings')

    # If the request is a GET request, render the confirmation page
    return render_template('meeting_delete.html', meeting=meeting)


# Route for displaying the list of meetings
@app.route('/meetings')
def meetings():
    # Retrieve all meetings from the database
    meeting = Meetings.query.all()
    return render_template('meeting_list.html', meetings=meeting)


# Default route redirects to the list of meetings
@app.route('/')
def home():
    return redirect('/meetings')


# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)
