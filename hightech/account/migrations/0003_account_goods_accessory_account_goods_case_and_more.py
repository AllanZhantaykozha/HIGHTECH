# Generated by Django 4.0.3 on 2022-09-06 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('charger', '0003_alter_charger_content'),
        ('phone', '0002_phone_price'),
        ('case', '0001_initial'),
        ('accessory', '0001_initial'),
        ('account', '0002_remove_account_goods_accessory_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='goods_accessory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='g_accessory', to='accessory.accessory'),
        ),
        migrations.AddField(
            model_name='account',
            name='goods_case',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='g_case', to='case.case'),
        ),
        migrations.AddField(
            model_name='account',
            name='goods_charger',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='g_charger', to='charger.charger'),
        ),
        migrations.AddField(
            model_name='account',
            name='goods_phone',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='g_phone', to='phone.phone'),
        ),
    ]
