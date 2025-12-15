# Contributing to Django User Enhanced

Thank you for your interest in contributing to Django User Enhanced! This document provides guidelines and instructions for contributing.

## Development Setup

1. Clone the repository:
```bash
git clone https://github.com/connorhess/Django-User-Enhanced.git
cd Django-User-Enhanced
```

2. Create a virtual environment and install dependencies:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
pip install -e .
```

3. Run the example project:
```bash
cd example_project
python manage.py migrate
python manage.py runserver
```

## Running Tests

Run the test suite:
```bash
cd example_project
python manage.py test django_user_enhanced
```

For verbose output:
```bash
python manage.py test django_user_enhanced -v 2
```

## Code Style

- Follow PEP 8 guidelines
- Use meaningful variable and function names
- Add docstrings to classes and functions
- Keep functions small and focused

## Making Changes

1. Fork the repository
2. Create a new branch for your feature or bugfix
3. Make your changes
4. Add or update tests as needed
5. Ensure all tests pass
6. Submit a pull request

## Adding New Features

When adding new features:

1. Update or create relevant tests
2. Update documentation (README.md)
3. Update example project if relevant
4. Ensure backwards compatibility when possible

## Reporting Issues

When reporting issues, please include:

- Django version
- Python version
- Steps to reproduce
- Expected behavior
- Actual behavior
- Any error messages or stack traces

## License

By contributing, you agree that your contributions will be licensed under the AGPL-3.0 License.
