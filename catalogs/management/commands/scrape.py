from django.core.management.base import BaseCommand
from catalogs.scrapper import main


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Scrapping is in progress!'))
        self.stdout.write(self.style.WARNING('Do not close until the scrapping is not done. Thanks for your patience!'))
        main()
