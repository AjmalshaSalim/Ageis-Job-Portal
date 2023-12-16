# Generated by Django 4.2.7 on 2023-11-29 12:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ageis_app', '0006_alter_clients_added_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(blank=True, max_length=25, null=True)),
                ('customer_img', models.ImageField(blank=True, null=True, upload_to='customerimg')),
                ('reviews', models.TextField(blank=True, null=True)),
                ('added_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('company_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ageis_app.clients')),
            ],
            options={
                'verbose_name_plural': 'Testimonial',
            },
        ),
    ]