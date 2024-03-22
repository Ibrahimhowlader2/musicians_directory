# Generated by Django 5.0.3 on 2024-03-22 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('musicians', '0002_delete_musicianmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('instrument_type', models.CharField(choices=[('Guitar', 'Guitar'), ('Piano', 'Piano'), ('Violin', 'Violin'), ('Drums', 'Drums'), ('Saxophone', 'Saxophone')], max_length=20)),
            ],
        ),
    ]