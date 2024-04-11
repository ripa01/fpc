# Generated by Django 4.1.1 on 2024-04-11 15:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0007_committee_alter_news_news_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('subtitle', models.CharField(max_length=300)),
                ('content', models.TextField()),
                ('event_image', models.ImageField(default='media/logo.jpeg', upload_to='event/images/')),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AlterField(
            model_name='news',
            name='news_image',
            field=models.ImageField(default='media/logo.jpeg', upload_to='news/images/'),
        ),
    ]
