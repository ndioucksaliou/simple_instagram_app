# Generated by Django 4.1.1 on 2022-09-27 11:17

from django.db import migrations, models
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_albumpage_userfeedpage_userprofilepage_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofilepage',
            name='bio',
            field=models.CharField(blank=True, default='I am a Software developer', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userprofilepage',
            name='body',
            field=wagtail.fields.StreamField([('photo', wagtail.images.blocks.ImageChooserBlock(required=False))], use_json_field=None, verbose_name='Contenu'),
        ),
    ]
