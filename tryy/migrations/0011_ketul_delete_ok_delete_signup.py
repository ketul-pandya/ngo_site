# Generated by Django 4.1.5 on 2023-01-28 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tryy', '0010_ok_alter_signup_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='ketul',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='ok',
        ),
        migrations.DeleteModel(
            name='Signup',
        ),
    ]