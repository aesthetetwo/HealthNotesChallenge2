# Generated by Django 3.2 on 2022-01-25 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywow', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('body', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='tags',
        ),
        migrations.AlterField(
            model_name='treatments',
            name='chemotherapy',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='treatments',
            name='clinical_trials',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='treatments',
            name='medical',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='treatments',
            name='radiation',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='treatments',
            name='surgical',
            field=models.CharField(max_length=255),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]