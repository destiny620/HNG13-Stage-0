# HNG13-Stage-0
Dynamic Profile Endpoint
# Django Cat Fact Profile API

This project provides a RESTful `/me` endpoint that returns your profile information along with a dynamic cat fact fetched from an external API.

## Features

- GET `/me` returns:
  - Your profile info (name, email, stack)
  - A random cat fact from [Cat Facts API](https://catfact.ninja/fact)
  - Current UTC timestamp in ISO 8601 format

## Setup Instructions

### 1. Clone the repository

```sh
git clone <your-repo-url>
cd <project-folder>
```

### 2. Create and activate a virtual environment

```sh
python -m venv venv
venv\Scripts\activate   # On Windows
# Or
source venv/bin/activate   # On macOS/Linux
```

### 3. Install dependencies

```sh
pip install django requests
```

### 4. Start a new Django project (if not already done)

```sh
django-admin startproject catprofile .
python manage.py startapp api
```

### 5. Add the code

- Add the provided `me` view to `api/views.py`.
- Add the URL pattern to `api/urls.py`.
- Include `api` in `INSTALLED_APPS` in `settings.py`.
- Include `api.urls` in your main `urls.py`.

### 6. Run migrations

```sh
python manage.py migrate
```

### 7. Start the development server

```sh
python manage.py runserver
```

### 8. Test the endpoint

Visit [http://localhost:8000/me](http://localhost:8000/me) in your browser or use `curl`:

```sh
curl http://localhost:8000/me
```

## Example Response

```json
{
  "status": "success",
  "user": {
    "email": "your@email.com",
    "name": "Your Name",
    "stack": ["python", "django"]
  },
  "timestamp": "2025-10-17T12:34:56.789012Z",
  "fact": "Cats have five toes on their front paws, but only four on the back ones."
}
```

## Notes

- Replace profile info in the view with your own details.
- Make sure you have internet access to fetch cat
