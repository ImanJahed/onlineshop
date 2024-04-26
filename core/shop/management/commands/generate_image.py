import random
from typing import Any
from django.core.management.base import BaseCommand
from django.core.files import File
from pathlib import Path
from faker import Faker

from shop.models import ProductImageModel, ProductModel

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
    help = 'Add Image to Product'

    def handle(self, *args: Any, **options: Any) -> str | None:
        fake = Faker(locale='fa_IR')

        all_products = ProductModel.objects.all()

        for _ in range(20):
            title = fake.word()
            product = random.choice(all_products)
            selected_image = random.choice(IMAGES)
            image = File(file=open(BASE_DIR / selected_image, 'rb'), name=Path(selected_image).name)

            ProductImageModel.objects.create(
                file=image,
                product=product
            )

        check_image = ProductImageModel.objects.all().count()
        self.stdout.write(self.style.SUCCESS(f"Number of Image: {check_image}"))



# selected_image = random.choice(IMAGES)
# print(selected_image)
# print(Path(selected_image))
# print(Path(selected_image).name)
