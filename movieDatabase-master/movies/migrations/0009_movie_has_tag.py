# Generated by Django 2.0.dev20170322162159 on 2017-04-06 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0008_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie_Has_Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_id', models.ManyToManyField(to='movies.Movie')),
            ],
        ),
    ]