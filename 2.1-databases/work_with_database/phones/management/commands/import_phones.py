import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            # TODO: Добавьте сохранение модели
            name_split_list = phone['name'].split()
            name_for_slug = ''
            for element in name_split_list:
                name_for_slug += f'{element}-'
            phone_in_db = Phone(
                name=phone['name'],
                price=phone['price'],
                image=phone['image'],
                release_date=phone['release_date'],
                lte_exist=phone['lte_exists'],
                slug=name_for_slug.rstrip('-').lower(),
            )
            phone_in_db.save()
