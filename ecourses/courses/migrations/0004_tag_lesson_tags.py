# Generated by Django 4.2.6 on 2023-10-28 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_alter_category_options_alter_lesson_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='lesson',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='courses.tag'),
        ),
    ]