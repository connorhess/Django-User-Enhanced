# Django User Enhanced

A Python Django module (like Django Admin) that allows users to easily add login pages, registration pages, password reset, and user profile functionality to their Django projects. Just add it to your installed apps and include the URLs - it's that simple!

## Features

- 🔐 **Login Page** - Beautiful, ready-to-use login form
- 📝 **Registration Page** - User-friendly registration with email validation
- 🔑 **Password Reset** - Complete password reset flow with email
- 👤 **User Profile** - Basic user profile page
- 🎨 **Customizable Templates** - All templates can be overridden
- 💅 **Modern Styling** - Clean, responsive CSS out of the box
- ⚡ **Easy Integration** - Just 3 lines of configuration

## Installation

### Using pip (recommended)

```bash
pip install django-user-enhanced
```

### From source

```bash
git clone https://github.com/connorhess/Django-User-Enhanced.git
cd Django-User-Enhanced
pip install -e .
```

## Quick Start

### 1. Add to INSTALLED_APPS

Add `'django_user_enhanced'` to your `INSTALLED_APPS` in `settings.py`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_user_enhanced',  # Add this line
]
```

### 2. Include URLs

Add the Django User Enhanced URLs to your project's `urls.py`:

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('django_user_enhanced.urls')),  # Add this line
]
```

### 3. Configure Login Redirect (Optional)

In your `settings.py`, you can configure where users are redirected after login:

```python
LOGIN_REDIRECT_URL = '/'  # Redirect to home page after login
LOGIN_URL = '/auth/login/'  # URL to redirect to for login
```

### 4. Run Migrations

```bash
python manage.py migrate
```

### 5. Collect Static Files (for production)

```bash
python manage.py collectstatic
```

## Available URLs

Once configured, the following URLs are available:

- `/auth/login/` - Login page
- `/auth/logout/` - Logout (redirects to login)
- `/auth/register/` - Registration page
- `/auth/password-reset/` - Request password reset
- `/auth/password-reset/done/` - Password reset email sent confirmation
- `/auth/password-reset/confirm/<uidb64>/<token>/` - Password reset confirmation
- `/auth/password-reset/complete/` - Password reset complete
- `/auth/profile/` - User profile page (requires login)

## Email Configuration

For password reset functionality, you need to configure email in your `settings.py`:

```python
# For development (prints emails to console)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# For production (example with Gmail)
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'
DEFAULT_FROM_EMAIL = 'your-email@gmail.com'
```

## Using in Templates

You can link to the authentication pages from your templates:

```html
<!-- Navigation menu example -->
{% if user.is_authenticated %}
    <a href="{% url 'django_user_enhanced:profile' %}">Profile</a>
    <a href="{% url 'django_user_enhanced:logout' %}">Logout</a>
{% else %}
    <a href="{% url 'django_user_enhanced:login' %}">Login</a>
    <a href="{% url 'django_user_enhanced:register' %}">Register</a>
{% endif %}
```

## Customization

### Override Templates

To customize the look and feel, create your own templates in your project's template directory with the same path structure:

```
your_project/
    templates/
        django_user_enhanced/
            login.html
            register.html
            password_reset.html
            # etc.
```

All templates extend `django_user_enhanced/base.html`, so you can override just the base template to change the overall look.

### Override Styles

You can override the default styles by creating your own CSS file and including it in your overridden base template, or by adding custom styles after the default stylesheet.

### Custom Forms

To use custom forms, you can subclass the views in your own `views.py`:

```python
from django_user_enhanced.views import EnhancedRegisterView
from myapp.forms import MyCustomRegistrationForm

class MyRegisterView(EnhancedRegisterView):
    form_class = MyCustomRegistrationForm
```

Then use your custom view in your URL configuration.

## Example Project Structure

```
myproject/
├── manage.py
├── myproject/
│   ├── settings.py
│   ├── urls.py          # Include django_user_enhanced.urls here
│   └── wsgi.py
└── templates/           # Optional: Override templates here
    └── django_user_enhanced/
        └── login.html
```

## Requirements

- Python >= 3.8
- Django >= 3.2

## License

This project is licensed under the GNU Affero General Public License v3 (AGPL-3.0). See the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

If you encounter any issues or have questions, please file an issue on the GitHub repository.

## Author

Connor Hess

## Changelog

### 0.1.0 (2025-12-15)
- Initial release
- Login, logout, registration, password reset functionality
- User profile page
- Default responsive templates and styling
- Easy integration with Django projects
