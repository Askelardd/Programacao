# Generated by Django 5.0.6 on 2025-07-15 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0017_remove_desbasteworker_desbaste_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='afinacaoworker',
            old_name='Afinacao',
            new_name='afinacao',
        ),
        migrations.RenameField(
            model_name='desbasteagulhaworker',
            old_name='DesbasteAgulha',
            new_name='desbaste_agulha',
        ),
        migrations.RenameField(
            model_name='desbastecalibreworker',
            old_name='DesbasteCalibre',
            new_name='desbasteCalibre',
        ),
        migrations.RenameField(
            model_name='qrdata',
            old_name='desbasteAgulha',
            new_name='desbaste_agulha',
        ),
        migrations.RenameField(
            model_name='qrdata',
            old_name='desbasteCalibre',
            new_name='desbaste_calibre',
        ),
    ]
