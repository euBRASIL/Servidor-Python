#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import openai


def main():
    openai.organization = "Eletron-Bit"
    openai.api_key = os.getenv("0549690c-63df-4f22-8b9f-6a3359734272")
    openai.Model.list()
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gettingstarted.settings")
    
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
