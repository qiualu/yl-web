#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "基础项目.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # print(f" sys.argv : {type(sys.argv)} {sys.argv}")
    execute_from_command_line(['manage.py', 'test', '投票应用'])



if __name__ == "__main__":
    import time
    time.sleep(5)
    main()

