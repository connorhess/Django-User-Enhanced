# Example Project

This is a minimal Django project demonstrating how to integrate Django User Enhanced.

## Setup

1. Install Django and the package:
```bash
pip install django
pip install -e ..  # Install django-user-enhanced from parent directory
```

2. Run migrations:
```bash
python manage.py migrate
```

3. Create a superuser (optional):
```bash
python manage.py createsuperuser
```

4. Run the development server:
```bash
python manage.py runserver
```

5. Visit the following URLs:
- http://127.0.0.1:8000/ - Home page
- http://127.0.0.1:8000/auth/login/ - Login page
- http://127.0.0.1:8000/auth/register/ - Registration page
- http://127.0.0.1:8000/auth/profile/ - Profile page (requires login)
- http://127.0.0.1:8000/admin/ - Django admin

## Project Structure

- `manage.py` - Django management script
- `myproject/` - Project configuration
  - `settings.py` - Django settings with django_user_enhanced configured
  - `urls.py` - URL configuration including django_user_enhanced URLs
  - `views.py` - Simple home page view
- `templates/` - Custom templates
  - `home.html` - Home page template
