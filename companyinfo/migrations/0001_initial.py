# Generated by Django 4.2 on 2023-07-15 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('logo', models.ImageField(upload_to='companyinfo/logos/', verbose_name='Logo')),
                ('subtitle', models.CharField(max_length=255, verbose_name='Subtitle')),
                ('call_us', models.CharField(max_length=20, verbose_name='Call Us')),
                ('email_us', models.EmailField(max_length=254, verbose_name='Email Us')),
                ('fb_link', models.URLField(blank=True, null=True, verbose_name='Facebook Link')),
                ('twit_link', models.URLField(blank=True, null=True, verbose_name='Twitter Link')),
                ('insta_link', models.URLField(blank=True, null=True, verbose_name='Instagram Link')),
                ('emails', models.TextField(verbose_name='Emails')),
                ('numbers', models.TextField(verbose_name='Numbers')),
                ('address', models.TextField(verbose_name='Address')),
            ],
        ),
    ]
