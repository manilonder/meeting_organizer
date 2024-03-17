from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize SQLAlchemy instance
db = SQLAlchemy()

# Define a SQLAlchemy model for meetings


class Meetings(db.Model):
    # Define table columns
    id = db.Column(db.Integer, primary_key=True)  # Primary key column
    subject = db.Column(db.String(100), nullable=False)  # Meeting subject column, cannot be null
    date = db.Column(db.Date, nullable=False)  # Meeting date column, cannot be null
    start_time = db.Column(db.Time, nullable=False)  # Meeting start time column, cannot be null
    end_time = db.Column(db.Time, nullable=False)  # Meeting end time column, cannot be null
    participants = db.Column(db.Text)  # Participants column, can be null

    # Constructor method to initialize object instances
    def __repr__(self):
        return f"Meeting('{self.subject}', '{self.date}', '{self.start_time}', '{self.end_time}')"
        # Return a string representation of the object for debugging purposes
