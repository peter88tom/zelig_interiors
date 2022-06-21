from django.db import models
from django.template.defaultfilters import slugify
from .category import Category


class Products(models.Model):
    name = models.CharField(max_length=60)
    slug = models.SlugField(null=False, unique=True)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.TextField(default='-', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/products/%Y/%m/%d/')
    is_featured = models.BooleanField(default=False)
    is_new = models.BooleanField(default=False)
    is_best_sale = models.BooleanField(default=False)

    @staticmethod
    def get_products_by_id(ids):
        return Products.objects.filter(id__in=ids)

    @staticmethod
    def get_all_products():
        return Products.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Products.objects.filter(category=category_id)
        else:
            return Products.get_all_products()

    @staticmethod
    def get_all_feature_products():
        return Products.objects.filter(is_featured=True)[:3]

    @staticmethod
    def get_new_product():
        return Products.objects.filter(is_new=True).order_by("-id")[:1]

    @staticmethod
    def get_best_sale_product():
        return Products.objects.filter(is_best_sale=True).order_by("-id")[:1]

    @staticmethod
    def get_products_by_slug_name(slug):
      return Products.objects.filter(slug=slug)
