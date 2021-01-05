from django.core.management.base import CommandError, no_translations
from django.core.management.commands.makemigrations import Command as BaseCommand


class Command(BaseCommand):
    @no_translations
    def handle(self, *app_labels, **options):
        if not (options["dry_run"] or options["check_changes"]):
            if not options["name"]:
                raise CommandError("Please provide name for migration file(s).")
        super().handle(*app_labels, **options)
