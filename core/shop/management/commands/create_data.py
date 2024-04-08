import random
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django.core.files import File

from faker import Faker
from faker.providers import BaseProvider
from pathlib import Path

from shop.models import ImageModel, ProductModel, CategoryModel

BASE_DIR = Path(__file__).resolve().parent

CATEGORIES = [
    "Shoes",
    "Boots",
    "Trainers",
    "Clothes",
    "Dress",
    "T-shirt",
    "Jeans",
    "Shirts",
    "PrintedShirts",
    "TankTops",
    "PoloShirt",
    "Beauty",
    "DIYTools",
    "GardenOutdoors",
    "Grocery",
    "HealthPersonalCare",
    "Lighting",
]

PRODUCTS = [
    "Shoes",
    "Boots",
    "Trainers",
    "Clothes",
    "Dress",
    "T-shirt",
    "Jeans",
    "Shirts",
    "PrintedShirts",
    "TankTops",
    "PoloShirt",
    "Beauty",
    "DIYTools",
    "GardenOutdoors",
    "Grocery",
    "HealthPersonalCare",
    "Lighting",
]

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

class Provider(BaseProvider):
    def ecommerce_category(self):
        return self.random_element(CATEGORIES)

    def ecommerce_product(self):
        return self.random_element(PRODUCTS)

class Command(BaseCommand):
    help = 'Create Product and Category object'

    def handle(self, *args, **kwargs):
        fake = Faker(locale="fa_IR")
        fake.add_provider(Provider)

        user = get_user_model().objects.get(type=4)

        for _ in range(20):
            CategoryModel.objects.create(
                title=fake.ecommerce_category(),
                slug=slugify(fake.ecommerce_category())
            )
        cat = CategoryModel.objects.all()
        for _ in range(20):

            product = ProductModel.objects.create(
                user=user,
                title =fake.ecommerce_product(),
                slug=slugify(fake.ecommerce_product()),
                price=fake.random_int(10000, 100000),
                stock= fake.random_int(min=0, max=10),
                discount_percent=fake.random_int(min=0, max=50),
                status=fake.random_int(min=1, max=2),
                display_status=fake.random_int(min=1, max=2),
                description=fake.text(max_nb_chars=600),
                brief_description=fake.paragraph(nb_sentences=1)
            )
            num_categories = random.randint(1, 4)
            selected_categories = random.sample(list(cat), num_categories)

            product.categories.set(selected_categories)

        for i in range(1, 21):
            selected_image = random.choice(IMAGES)
            img_obj = File(file=open(BASE_DIR / selected_image, 'rb'), name=Path(selected_image).name)
            product = ProductModel.objects.get(id=i)
            ImageModel.objects.create(
                product=product,
                title=fake.text(max_nb_chars=20),
                image=img_obj
            )
        check_category = CategoryModel.objects.all().count()
        self.stdout.write(self.style.SUCCESS(f"Number of categories: {check_category}"))

        check_product = ProductModel.objects.all().count()
        self.stdout.write(self.style.SUCCESS(f"Number of Product: {check_product}"))

        check_product = ImageModel.objects.all().count()
        self.stdout.write(self.style.SUCCESS(f"Number of Image: {check_product}"))



