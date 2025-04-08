# Inventry

## Project Description

This project is a Django-based API application that provides various functionalities.

## Installed Apps

- **api**: Main application for the API.
- **rest_framework**: Used for building RESTful APIs.
- **corsheaders**: Handles Cross-Origin Resource Sharing (CORS).
- **rest_framework_simplejwt.token_blacklist**: Manages token blacklisting for JWT authentication.

## Database Setup

To set up PostgreSQL as the database, follow these steps:

1. Install PostgreSQL on your machine if it is not already installed.
2. Create a new database for the project.
3. Update the `settings.py` file to configure PostgreSQL as follows:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

4. Run the following command to apply migrations:

```bash
python manage.py migrate
```

5. Start the development server:

```bash
python manage.py runserver
```

## Current State

- The API currently has defined models for users and profiles.
- The views and URL patterns are not yet implemented.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/AY-10/invent
   ```
2. Navigate to the project directory:
   ```bash
   cd backend
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To run the project, use the following command:

```bash
python manage.py runserver
```

## API Endpoints

- (To be added once implemented)

## Models

- **User**: Custom user model with additional fields.
- **Profile**: User profile model with additional information.
