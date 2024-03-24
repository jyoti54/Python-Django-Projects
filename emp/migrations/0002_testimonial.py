# Generated by Django 5.0.3 on 2024-03-20 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('testinomial', models.TextField()),
                ('picture', models.ImageField(upload_to='testimonials/')),
                ('rating', models.ImageField(max_length=1, upload_to='')),
            ],
        ),
    ]
