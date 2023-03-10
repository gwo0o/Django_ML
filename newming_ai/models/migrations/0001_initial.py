# Generated by Django 4.1.5 on 2023-02-02 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.CharField(db_column='_id', max_length=255, primary_key=True, serialize=False)),
                ('title', models.TextField(blank=True, db_column='title', null=True)),
                ('content', models.TextField(blank=True, db_column='content', null=True)),
                ('tags', models.CharField(blank=True, db_column='tags', max_length=255, null=True)),
            ],
            options={
                'db_table': 'nm_interest_press_article_60days_content',
                'managed': False,
            },
        ),
    ]
