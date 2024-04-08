from typing import Any
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from faker import Faker

from shop.models import CategoryModel


class Command(BaseCommand):
    help = 'Generate fake Categories'

    def handle(self, *args: Any, **options: Any) -> str | None:
        fake = Faker(locale='fa_IR')
        for _ in range(20):
            title = fake.word()
            CategoryModel.objects.create(
                title= title,
                slug=slugify(title, allow_unicode=True)
            )

        check_category = CategoryModel.objects.all().count()
        self.stdout.write(self.style.SUCCESS(f"Number of categories: {check_category}"))

