import os
import django
django.setup()
import random
from faker import Faker
from django.conf import settings
from django.core.files import File
from taggit.models import Tag
from django.utils.text import slugify
from django.contrib.auth.models import User
from products.models import Product, ProductImage, Brand, Category, BrandCategory, ProductReview, FlagOption
from companyinfo.models import Company

fake = Faker()

def get_image_paths(directory):
    #Returns a list of file paths for all images in the given directory.
    image_extensions = ('.jpg', '.jpeg', '.png', '.gif')
    image_paths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(image_extensions):
                image_paths.append(os.path.join(root, file))
    return image_paths


def seed_category(n):
    image_paths = get_image_paths(os.path.join(settings.MEDIA_ROOT, 'products', 'categories'))
    category_names = ["cat 01", "cat 02", "cat 03", "cat 04", "cat 05", "cat 06", "cat 07",  
            "cat 08", "cat 09", "cat 10", "cat 11", "cat 12", "cat 13", "cat 14", "cat 15",  
            "cat 16", "cat 17", "cat 18", "cat 19", "cat 20"]
    used_names = set()
    
    for _ in range(n):
        while True:
            name = fake.word(ext_word_list=category_names)
            if name not in used_names:
                used_names.add(name)
                break
        image_path = random.choice(image_paths)

        with open(image_path, 'rb') as f:
            category = Category.objects.create(
                name=name,
                image=File(f, name=f'{name}.jpg')
            )
    
    print(f'Successfully Seeded {n} Category')


def seed_brand(n):
    image_paths = get_image_paths(os.path.join(settings.MEDIA_ROOT, 'products', 'brands'))
    categories = Category.objects.all()
    brand_names = ["Brand A", "Brand B", "Brand C", "Brand D", "Brand E", "Brand F", 
            "Brand G", "Brand H", "Brand I", "Brand J", "Brand K", "Brand L", "Brand M", "Brand N", 
            "Brand O", "Brand P", "Brand Q", "Brand R", "Brand S", "Brand T"]
    used_names = set()
    
    for _ in range(n):
        while True:
            name = fake.word(ext_word_list=brand_names)
            if name not in used_names:
                used_names.add(name)
                break
        image_path = random.choice(image_paths)
        with open(image_path, 'rb') as f:
            brand = Brand.objects.create(
                name=name,
                image=File(f, name=f'{name}.jpg')
            )
        
        # Add fake categories to the brand
        num_categories = random.randint(1, 3)
        brand_categories = random.sample(list(categories), num_categories)
        for category in brand_categories:
            BrandCategory.objects.create(
                brand=brand,
                category=category
            )
    
    print(f'Successfully Seeded {n} Brand')


def seed_flag_option():
    flag_types = ['New', 'Feature', 'Sale']
    flag_instances = []
    for name in flag_types:
        flag_option, created = FlagOption.objects.get_or_create(name=name)
        flag_instances.append(flag_option)
    return flag_instances


def seed_product(n):
    images = get_image_paths(os.path.join(settings.MEDIA_ROOT, 'products', 'products'))
    flag_instances = seed_flag_option()
    categories = Category.objects.all()
    brands = Brand.objects.all()
    product_images = get_image_paths(os.path.join(settings.MEDIA_ROOT, 'products', 'product_images'))
    product_image_dict = {}
    
    for _ in range(n):
        product_names = ["Apple", "Banana", "Orange", "Grape", "Pineapple", "Mango", "Watermelon", 
                "Kiwi", "Strawberry", "Blueberry", "Raspberry", "Blackberry", "Lemon", "Lime", 
                "Grapefruit", "Peach", "Plum", "Cherry", "Apricot", "Avocado", "Tomato", "Cucumber", 
                "Carrot", "Broccoli", "Cauliflower", "Spinach", "Lettuce", "Cabbage", "Potato", 
                "Sweet potato", "Onion", "Garlic", "Mushroom", "Eggplant", "Zucchini", "Bell pepper", 
                "Jalapeno", "Habanero", "Cheese", "Milk", "Yogurt", "Butter", "Cream", "Ice cream", 
                "Chicken", "Beef", "Lamb", "Fish", "Shrimp", "Lobster", "Crab", "Oyster", "Clam", 
                "Scallop", "Rice", "Pasta", "Bread", "Cake", "Cookie", "Chocolate", "Candy", "Snack",
                "Cereal", "Juice", "Tea", "Coffee",]
        name = fake.word(ext_word_list=product_names)
        subtitle = fake.paragraph()
        sku = random.randint(10000, 1000000)
        description = fake.text(max_nb_chars=10000)
        price = round(random.uniform(20.99, 99.99), 2)
        image_path = random.choice(images)
        flag = random.choice(flag_instances)
        quantity = random.randint(1, 100)
        category = random.choice(categories)
        brand = random.choice(brands)

        with open(image_path, 'rb') as f:
            product = Product.objects.create(
                name=name,
                subtitle=subtitle,
                sku=sku,
                description=description,
                price=price,
                image=File(f, name=f'{name}.jpg'),
                flag=flag,
                quantity=quantity,
                brand=brand,
                category=category,
                slug=slugify(name)
            )
            # add the specified tags to the product
            tag_names = ["Organic", "Fruits", "Chilis"]
            num_tags = random.randint(1, 3)
            selected_tags = random.sample(tag_names, num_tags)
            for tag_name in selected_tags:
                tag, _ = Tag.objects.get_or_create(name=tag_name)
                product.tags.add(tag)
            # create a list of image paths for this product
            product_image_paths = random.sample(product_images, 5)
            product_image_dict[product] = product_image_paths
            # add some additional images to the product
            for image_path in product_image_paths:
                product_image_name = os.path.splitext(os.path.basename(image_path))[0]
                with open(image_path, 'rb') as f:
                    product_image = ProductImage.objects.create(
                        product=product,
                        image=File(f, name=f'{product_image_name}.jpg')
                    )
    
    print(f'Successfully Seeded {n} Product')

'''
def seed_product_image(n):
    images = get_image_paths(os.path.join(settings.MEDIA_ROOT, 'product_images'))
    
    for product in Product.objects.all():
        for _ in range(n):
            image_path = random.choice(images)
            product_name = os.path.splitext(os.path.basename(image_path))[0]
            with open(image_path, 'rb') as f:
                product_image =ProductImage.objects.create(
                    product=product,
                    image=File(f, name=f'{product_name}.jpg')
                )
    
    print(f'Successfully Seeded {n} Product Images')


def seed_product_review(n):
    fake = Faker()
    users = User.objects.all()
    products = Product.objects.all()
    
    for _ in range(n):
        user = random.choice(users)
        product = random.choice(products)
        rate = random.randint(0, 5)
        review = fake.text(max_nb_chars=500)
        created_at = fake.date_time_between(start_date='-1y', end_date='now')
        product_review = ProductReview.objects.create(
            user=user,
            product=product,
            rate=rate,
            review=review,
            created_at=created_at
        )
    
    print(f'Successfully Seeded {n} Product Reviews')
'''
# seed_category(6)
# seed_brand(4)
# seed_product(8)
