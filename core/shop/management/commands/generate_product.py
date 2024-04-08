import random
from typing import Any
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from pathlib import Path

from faker import Faker

from shop.models import ProductModel, CategoryModel, ImageModel



BASE_DIR = Path(__file__).resolve().parent



IMAGES = [
    "./images/img1.jpg",
    "./images/img2.jpg",
    "./images/img3.jpg",
    "./images/img4.jpg",
    "./images/img5.jpg",
    "./images/img6.jpg",
    "./images/img7.jpg",
    "./images/img8.jpg",
]


class Command(BaseCommand):
    help = 'Generate fake product'

    def handle(self, *args: Any, **options: Any) -> str | None:
        fake = Faker(locale='fa_IR')

        user = get_user_model().objects.get(type=4)
        cat = CategoryModel.objects.all()

        for _ in range(20):
            title = " ".join([fake.word() for _ in range(1,3)]) # 2 word generate and join with space
            slug=slugify(title, allow_unicode=True)
            description = fake.paragraph(nb_sentences=10) # generate paragraph with 10 sentences
            brief_description =fake.paragraph(nb_sentences=1)
            stock = fake.random_int(min=0, max=20)
            price = fake.random_int(min=10000, max=1000000)
            discount_percent = fake.random_int(min=0, max=35)
            status = random.randrange(1,3)
            display_status = random.randrange(1,3)


            product = ProductModel.objects.create(
                user=user,
                title=title,
                slug=slug,
                description=description,
                brief_description=brief_description,
                stock=stock,
                discount_percent=discount_percent,
                status=status,
                display_status=display_status,
                price=price
            )

            num_categories = random.randint(1, 4)
            selected_categories = random.sample(list(cat), k=num_categories) # list(cat) ==> convert QuerySet to list

            product.categories.set(selected_categories)


        check_product = ProductModel.objects.all().count()
        self.stdout.write(self.style.SUCCESS(f"Number of Product: {check_product}"))



