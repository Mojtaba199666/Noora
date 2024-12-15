# Generated by Django 4.2.13 on 2024-12-10 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('disc', models.TextField(blank=True, max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='SubType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('disc', models.TextField(blank=True, max_length=500)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Products.type')),
            ],
        ),
        migrations.CreateModel(
            name='Product_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('disc', models.TextField(max_length=500)),
                ('application', models.CharField(max_length=100)),
                ('material', models.CharField(max_length=50)),
                ('work_temp', models.CharField(max_length=20)),
                ('illumination_class', models.CharField(max_length=20)),
                ('FWHM', models.CharField(max_length=20)),
                ('Light_source_type', models.CharField(max_length=20)),
                ('Transparency', models.IntegerField(default=90)),
                ('subtype', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Products.subtype')),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Products.type')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lens', models.ImageField(upload_to='images/lens/')),
                ('holder', models.ImageField(blank=True, upload_to='images/holder/')),
                ('optical_diagram', models.ImageField(blank=True, upload_to='images/optical_diagram/')),
                ('lens_drawing', models.ImageField(blank=True, upload_to='images/lens_drawing/')),
                ('product_info', models.ForeignKey(blank=True, default='1', null=True, on_delete=django.db.models.deletion.SET_NULL, to='Products.product_info')),
            ],
        ),
    ]
