# 🎥 Video Panel Feedback Platform

A **Django-based** web application designed for structured **video feedback collection**. ### 
This Django-based web application is designed to facilitate structured video feedback collection for research purposes. Participants watch randomized videos and provide structured feedback, including ratings, severity assessments, and optional comments. The system securely manages participant data, tracks progress, and ensures a streamlined feedback workflow.

### Types of Videos in This Use Case

Currently, this platform is being used to study **golfers with the yips**, a movement disorder characterized by involuntary muscle spasms that can disrupt performance.  The collected data helps advance research into movement disorders and their impact on performance, but the videos could be anything—ranging from sports performance analysis to medical case studies, rehabilitation exercises, or even general movement assessments for biomechanical research.



## 🚀 Features

- **Participant Management**
  - New users register securely.
  - Existing users resume feedback via login.
  - Admin panel to track participants, consent, and feedback.

- **Informed Consent Workflow**
  - Participants must consent before proceeding.
  - Consent timestamps are recorded for tracking.

- **Video Feedback Collection**
  - Videos fetched dynamically from **AWS S3**.

- **Security & Compliance**
  - Secure authentication with hashed passwords.
  - CSRF protection enabled on all forms.
  - **Presigned URLs** for secure video streaming.

- **Completion Tracking**
  - Participants are redirected to a "Thank You" page upon completing all assigned videos.

---

## 🛠️ Technology Stack

- **Backend:** Django (Python)
- **Database:** PostgreSQL (Hosted on Heroku)
- **Frontend:** HTML, CSS, Django Templates
- **Cloud Storage:** AWS S3
- **Deployment:** Heroku

---

## 📌 Installation Guide

### 1️⃣ Prerequisites

Ensure you have:

- **Python 3.x**
- **Django 4.2**
- **PostgreSQL**
- **AWS Credentials** (for S3)
- **Heroku CLI** (if deploying)

### 2️⃣ Setup Instructions

#### 🔗 Connecting to a PostgreSQL Database (Railway) 🐍

To set up a PostgreSQL database using Railway (a free-tier option), follow these steps:

1. **Sign Up & Create a Database**
   - Go to [Railway](https://railway.app/) and sign up.
   - Create a new project and select "PostgreSQL" as the database type.
   - Railway will provide a database URL in the format:
     ```sh
     postgresql://user:password@host:port/database
     ```
   - Copy this URL.

2. **Configure Django to Use Railway Database**
   - Update your `.env` file:
     ```ini
     DATABASE_URL=your_railway_database_url
     ```
   - Modify `settings.py` to use the environment variable:
     ```python
     import dj_database_url
     DATABASES = {
         'default': dj_database_url.config(default=os.getenv('DATABASE_URL'))
     }
     ```
   - Run migrations to apply database changes:
     ```sh
     python manage.py migrate
     ```

#### ☁️ Setting Up an AWS S3 Bucket for Video Storage 🌍

1. **Create an AWS S3 Bucket**
   - Sign in to [AWS Console](https://aws.amazon.com/console/).
   - Go to S3 and create a new bucket.
   - Set permissions (for public or private access as needed).

2. **Generate Credentials**
   - In AWS IAM, create a user with S3 permissions.
   - Get the `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`.

3. **Configure Django for S3 Storage**
   - Add credentials to `.env`:
     ```ini
     AWS_ACCESS_KEY_ID=your_key
     AWS_SECRET_ACCESS_KEY=your_secret
     AWS_STORAGE_BUCKET_NAME=your_bucket_name
     ```
   - Use Django's `boto3` library to interact with S3 for secure video storage and retrieval.

### 🏗️ Django Setup Instructions

#### 🏗️ Clone the Repository

```sh
git clone https://github.com/yourusername/video-panel-feedback.git
cd video-panel-feedback
```

#### 🏗️ Create a Virtual Environment

```sh
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

#### 🏗️ Install Dependencies

```sh
pip install -r requirements.txt
```

#### 🏗️ Set Up Environment Variables

Create a `.env` file in the project root:

```ini
FIXED_USER_PASSWORD=your_password
DATABASE_URL=your_postgres_connection_string
AWS_ACCESS_KEY_ID=your_aws_access_key
AWS_SECRET_ACCESS_KEY=your_aws_secret_key
AWS_DEFAULT_REGION=your_region
```

#### 🏗️ Apply Database Migrations

```sh
python manage.py migrate
```

#### 🏗️ Run the Development Server

```sh
python manage.py runserver
```

#### 🏗️ Access the Application

Open `http://127.0.0.1:8000/` in your browser.

---

## 🚀 Deployment to Heroku

#### 1️⃣ Login to Heroku

```sh
heroku login
```

#### 2️⃣ Create a Heroku App

```sh
heroku create your-app-name
```

#### 3️⃣ Set Environment Variables on Heroku

```sh
heroku config:set ALLOWED_HOSTS=your_allowed_hosts
heroku config:set AWS_ACCESS_KEY_ID=your_aws_access_key
heroku config:set AWS_DEFAULT_REGION=your_aws_region
heroku config:set AWS_SECRET_ACCESS_KEY=your_aws_secret_key
heroku config:set DATABASE_URL=your_postgres_connection_string
heroku config:set DEBUG=True  # or False in production
heroku config:set DJANGO_SETTINGS_MODULE=your_django_settings_module
heroku config:set FIXED_USER_PASSWORD=your_password
heroku config:set SECRET_KEY=your_secret_key
```

#### 4️⃣ Deploy to Heroku

```sh
git push heroku main
```

#### 5️⃣ Run Database Migrations on Heroku

```sh
heroku run python manage.py migrate
```

#### 6️⃣ Open the App

```sh
heroku open
```

---

## 📂 Project Structure

### 🔐 Configuring `settings.py`

The `settings.py` file is a crucial component of the Django project as it contains settings necessary for the application to function properly. To ensure security and smooth operation, this file must be populated with credentials for **Heroku**, **AWS**, and **Railway**.

---

## 📜 License

This project isn't licensed.

---

## 📬 Contact

For questions or contributions, please reach out to **Beorn Nijenhuis**.
