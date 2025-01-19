🎥 Video Panel Feedback Platform

A Django-based web application designed for structured video feedback collection. Participants watch randomized videos and provide ratings, severity assessments, and comments. The system securely manages participant data, tracks progress, and ensures a streamlined feedback workflow.

🚀 Features

Participant Management

New users register securely.

Existing users resume feedback via login.

Admin panel to track participants, consent, and feedback.

Informed Consent Workflow

Participants must consent before proceeding.

Consent timestamps are recorded for tracking.

Video Feedback Collection

Videos fetched dynamically from AWS S3.

Users provide ratings (1-5), Yips severity, and indicate neurological disorder presence.

Optional comments for qualitative feedback.

Security & Compliance

Secure authentication with hashed passwords.

CSRF protection enabled on all forms.

Presigned URLs for secure video streaming.

Completion Tracking

Participants are redirected to a "Thank You" page upon completing all assigned videos.

🛠️ Technology Stack

Backend: Django (Python)

Database: PostgreSQL (Hosted on Heroku)

Frontend: HTML, CSS, Django Templates

Cloud Storage: AWS S3

Deployment: Heroku

📌 Installation Guide

1️⃣ Prerequisites

Ensure you have:

Python 3.x

Django 4.2

PostgreSQL

AWS Credentials (for S3)

Heroku CLI (if deploying)

2️⃣ Setup Instructions

🔗 Connecting to a PostgreSQL Database (Railway) 🐍

To set up a PostgreSQL database using Railway (a free-tier option), follow these steps:

Sign Up & Create a Database

Go to Railway and sign up.

Create a new project and select "PostgreSQL" as the database type.

Railway will provide a database URL in the format:

postgresql://user:password@host:port/database

Copy this URL.

Configure Django to Use Railway Database

Update your .env file:

DATABASE_URL=your_railway_database_url

Modify settings.py to use the environment variable:

import dj_database_url
DATABASES = {
    'default': dj_database_url.config(default=os.getenv('DATABASE_URL'))
}

Run migrations to apply database changes:

python manage.py migrate

☁️ Setting Up an AWS S3 Bucket for Video Storage 🌍

Create an AWS S3 Bucket

Sign in to AWS Console.

Go to S3 and create a new bucket.

Set permissions (for public or private access as needed).

Generate Credentials

In AWS IAM, create a user with S3 permissions.

Get the AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY.

Configure Django for S3 Storage

Add credentials to .env:

AWS_ACCESS_KEY_ID=your_key
AWS_SECRET_ACCESS_KEY=your_secret
AWS_STORAGE_BUCKET_NAME=your_bucket_name

Use Django's boto3 library to interact with S3 for secure video storage and retrieval.



🏗️ Django Setup Instructions

🏗️ Clone the Repository

git clone https://github.com/yourusername/video-panel-feedback.git
cd video-panel-feedback

🏗️ Create a Virtual Environment

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

🏗️ Install Dependencies

pip install -r requirements.txt

🏗️ Set Up Environment Variables

Create a .env file in the project root:

FIXED_USER_PASSWORD=your_password
DATABASE_URL=your_postgres_connection_string
AWS_ACCESS_KEY_ID=your_aws_access_key
AWS_SECRET_ACCESS_KEY=your_aws_secret_key
AWS_DEFAULT_REGION=your_region

🏗️ Apply Database Migrations

python manage.py migrate

🏗️ Run the Development Server

python manage.py runserver

🏗️ Access the Application

Open http://127.0.0.1:8000/ in your browser.

🚀 Deployment to Heroku

1️⃣ Login to Heroku

heroku login

2️⃣ Create a Heroku App

heroku create your-app-name

3️⃣ Set Environment Variables on Heroku

heroku config:set FIXED_USER_PASSWORD=your_password
heroku config:set DATABASE_URL=your_postgres_connection_string
heroku config:set AWS_ACCESS_KEY_ID=your_aws_access_key
heroku config:set AWS_SECRET_ACCESS_KEY=your_aws_secret_key
heroku config:set AWS_DEFAULT_REGION=your_region

4️⃣ Deploy to Heroku

git push heroku main

5️⃣ Run Database Migrations on Heroku

heroku run python manage.py migrate

6️⃣ Open the App

heroku open

📂 Project Structure

🔐 Configuring settings.py

The settings.py file is a crucial component of the Django project as it containssettings necessary for the application to function properly. To ensure security and smooth operation, this file must be populated with credentials for Heroku, AWS, and Railway.



Structure: 

video-panel-feedback/
│-- feedback_backend_project/  # Main Django app
│   │-- migrations/            # Database migrations
│   │-- static/                # Static files (CSS, JS)
│   │-- templates/             # HTML templates
│   │-- views.py               # Business logic
│   │-- models.py              # Database models
│   │-- urls.py                # URL routing
│-- settings.py                # Django settings
│-- manage.py                  # Django CLI tool
│-- requirements.txt           # Dependencies
│-- README.md                  # Project documentation

📜 License

This project isn't licensed.

📬 Contact

For questions or contributions, please reach out to Beorn Nijenhuis

