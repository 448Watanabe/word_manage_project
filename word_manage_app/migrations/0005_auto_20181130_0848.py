# Generated by Django 2.0.6 on 2018-11-29 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('word_manage_app', '0004_auto_20181127_0404'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expression',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expression', models.CharField(max_length=128)),
                ('meaning', models.TextField()),
                ('note', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='word',
            name='reference',
        ),
        migrations.AlterField(
            model_name='word',
            name='access',
            field=models.IntegerField(default=0, editable=False),
        ),
        migrations.AddField(
            model_name='reference',
            name='reference',
            field=models.ManyToManyField(to='word_manage_app.Word'),
        ),
    ]