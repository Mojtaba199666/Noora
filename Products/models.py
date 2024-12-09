from django.db import models


class Type(models.Model):
    name = models.CharField(max_length=100)
    disc = models.TextField(max_length=500)

    def __str__(self):
        return self.name


class SubType(models.Model):
    name = models.CharField(max_length=100)
    disc = models.TextField(max_length=500)

    type = models.ForeignKey(Type, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Product_info(models.Model):
    name = models.CharField(max_length=100)
    disc = models.TextField(max_length=500)
    application = models.CharField(max_length=100)
    material = models.CharField(max_length=50)
    work_temp = models.CharField(max_length=20)
    illumination_class = models.CharField(max_length=20)
    FWHM = models.CharField(max_length=20)
    Light_source_type = models.CharField(max_length=20)
    Transparency = models.IntegerField(default=90)

    type = models.ForeignKey(Type, on_delete=models.SET_NULL, null=True)
    subtype = models.ForeignKey(SubType, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    lens = models.ImageField(upload_to='images/lens/')
    holder = models.ImageField(upload_to='images/holder/', null=True)
    optical_diagram = models.ImageField(upload_to='images/optical_diagram/', null=True)
    lens_drawing = models.ImageField(upload_to='images/lens_drawing/', null=True)

    product_info = models.ForeignKey(Product_info, on_delete=models.CASCADE)

    def __str__(self):
        return self.product_info.name
