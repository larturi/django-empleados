# Generated by Django 3.2.7 on 2021-10-02 22:07

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0004_empleado_fecha_nacimiento'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='resumen',
            field=ckeditor.fields.RichTextField(default=''),
            preserve_default=False,
        ),
    ]
