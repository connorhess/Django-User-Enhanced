# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2025-12-15

### Added
- Initial release of Django User Enhanced
- Login view with styled form
- Registration view with email support
- Password reset flow (request, email, confirm, complete)
- User profile page
- Logout functionality
- Modern, responsive templates with gradient design
- Comprehensive CSS styling
- URL routing configuration
- Enhanced forms with Bootstrap-like styling
- Example Django project demonstrating integration
- Comprehensive test suite (14 tests)
- Setup.py and pyproject.toml for package distribution
- Detailed README with usage instructions
- MANIFEST.in for package data inclusion

### Features
- Easy 3-step integration into existing Django projects
- Works with Django 3.2+ and Python 3.8+
- Fully customizable templates and forms
- Mobile-responsive design
- Email-based password reset
- Clean, accessible UI

### Testing
- 14 automated tests covering:
  - Login functionality (GET, POST success/failure)
  - Registration (GET, POST, email saving)
  - Profile view (authentication required, display)
  - Password reset (GET request)
  - Logout functionality
  - Form validation (user creation, authentication, password reset)

### Security
- CodeQL security analysis: No vulnerabilities found
- CSRF protection on all forms
- Password validation using Django's built-in validators
- Secure password storage using Django's authentication system

[0.1.0]: https://github.com/connorhess/Django-User-Enhanced/releases/tag/v0.1.0
