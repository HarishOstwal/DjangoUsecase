# Generated by Django 4.2.5 on 2023-09-26 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Encroachment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('encroachment_id', models.CharField(max_length=255)),
                ('encroachment_type', models.CharField(max_length=255)),
                ('region', models.CharField(max_length=255)),
                ('subregion', models.CharField(max_length=255)),
                ('encroachment_size_sq_ft', models.DecimalField(decimal_places=2, max_digits=10)),
                ('distance_from_center_ft', models.IntegerField()),
                ('criticality', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='EncroachmentStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='EncroachmentWorkflow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='EncroachmentDepartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enchroachAPP.department')),
                ('encroachment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enchroachAPP.encroachment')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enchroachAPP.encroachmentstatus')),
                ('workflow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enchroachAPP.encroachmentworkflow')),
            ],
        ),
        migrations.AddField(
            model_name='encroachment',
            name='departments',
            field=models.ManyToManyField(through='enchroachAPP.EncroachmentDepartment', to='enchroachAPP.department'),
        ),
        migrations.CreateModel(
            name='DepartmentWorkflow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enchroachAPP.department')),
                ('workflow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enchroachAPP.encroachmentworkflow')),
            ],
        ),
        migrations.CreateModel(
            name='DepartmentStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enchroachAPP.department')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enchroachAPP.encroachmentstatus')),
            ],
        ),
        migrations.CreateModel(
            name='DepartmentStage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enchroachAPP.department')),
            ],
        ),
    ]
