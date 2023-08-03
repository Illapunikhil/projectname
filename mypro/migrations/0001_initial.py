# Generated by Django 4.2.3 on 2023-08-02 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField(default=50)),
                ('description', models.TextField(default='Its too yummy')),
                ('image', models.ImageField(upload_to='images')),
                ('order_status', models.BooleanField(default=False)),
                ('items', models.IntegerField(default=0)),
            ],
        ),
    ]
