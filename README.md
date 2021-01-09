# django-require-migration-name

[![codecov](https://codecov.io/gh/whtsky/django-require-migration-name/branch/master/graph/badge.svg?token=WXUN262JEF)](https://codecov.io/gh/whtsky/django-require-migration-name)

require `name` in Django's `makemigrations`

## Installation

```bash
pip install django-require-migration-name
```

## Usage

Add `django_require_migration_name` into your `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    # ...

    'django_require_migration_name',
]
```

Then you can't `makemigrations` without `name`:

```bash
>> python manage.py makemigrations
CommandError: Please provide name for migration file(s).
>> python manage.py makemigrations -n name_here
No changes detected
```

## Changelog

### v0.2.0

- fix: use underscore in package folder name

### v0.1.0

- Initial release
