# Generated by Django 2.2 on 2019-08-08 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_python'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('Session', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.Python')),
            ],
        ),
    ]
