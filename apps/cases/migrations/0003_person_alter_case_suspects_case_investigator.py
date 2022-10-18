# Generated by Django 4.1.1 on 2022-10-16 03:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0002_rename_cases_case'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='case',
            name='suspects',
            field=models.ManyToManyField(blank=True, to='cases.suspect'),
        ),
        migrations.AddField(
            model_name='case',
            name='investigator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cases.person'),
        ),
    ]