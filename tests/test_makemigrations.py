from io import StringIO

from django.core.management import call_command
from django.core.management.base import CommandError
from django.test import TestCase


class MakemigrationsTest(TestCase):
    def test_dry_run(self):
        out = StringIO()
        call_command("makemigrations", dry_run=True, stdout=out)
        self.assertIn("No changes detected", out.getvalue())

    def test_check(self):
        out = StringIO()
        call_command("makemigrations", check=True, stdout=out)
        self.assertIn("No changes detected", out.getvalue())

    def test_makemigration_without_name(self):
        out = StringIO()
        with self.assertRaises(CommandError):
            call_command("makemigrations", stdout=out)

    def test_makemigration_with_name(self):
        out = StringIO()
        call_command("makemigrations", name="test", stdout=out)
        self.assertIn("No changes detected", out.getvalue())
