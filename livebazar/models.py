from django.db import models
from django import forms


class Costumer(models.Model):
    product_categories = [
        ("meva", "Meva-sabzavotlar"),
        ("gosht", "Go‘sht va parranda mahsulotlari"),
        ("sut", "Sut va sut mahsulotlari"),
        ("non", "Non va un mahsulotlari"),
        ("ichimlik", "Ichimliklar"),
        ("shakar", "Shakar va shirinliklar"),
        ("ziravor", "Oziq-ovqat ziravorlari"),
        ("uy", "Uy-ro‘zg‘or buyumlari"),
        ("texnika", "Maishiy texnika"),
        ("kiyim", "Kiyim-kechak"),
        ("gozallik", "Go‘zallik va parvarish vositalari"),
        ("qurilish", "Qurilish mollari"),
        ("avto", "Avto ehtiyot qismlar"),
        ("elektronika", "Elektronika"),
        ("hayvon", "Hayvonlar uchun mahsulotlar"),
    ]

    locations = [
        ("toshkent", "Toshkent"),
        ("fargona", "Farg'ona"),
        ("andijon", "Andijon"),
        ("namangan", "Namangan"),
        ("samarqand", "Samarqand"),
        ("buxoro", "Buxoro"),
        ("xorazm", "Xorazm"),
        ("navoiy", "Navoiy"),
        ("jizzax", "Jizzax"),
        ("sirdaryo", "Sirdaryo"),
        ("qashqadaryo", "Qashqadaryo"),
        ("surxondaryo", "Surxondaryo")
    ]

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=13)
    email = models.EmailField()
    password = models.CharField()
    location = models.CharField(choices=locations)
    market_name = models.CharField(max_length=256)
    product_category = models.CharField(choices=product_categories)

    def __str__(self):
        return f"{self.id}. {self.first_name}({self.location}) ------------- {self.product_category}"





