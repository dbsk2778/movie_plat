# Generated by Django 4.1.1 on 2022-11-04 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_id', models.IntegerField()),
                ('title', models.IntegerField()),
                ('released_date', models.TextField()),
                ('popularity', models.FloatField()),
                ('vote_avg', models.FloatField()),
                ('overview', models.TextField()),
                ('poster_path', models.TextField()),
                ('genres', models.ManyToManyField(related_name='movies', to='movie.genre')),
            ],
        ),
    ]
