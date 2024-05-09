from django.db import migrations, models

def create_default_logins(apps, schema_editor):
    Login = apps.get_model('webapp', 'Login')
    Login.objects.create(usuario='usuario1', password='password1')
    Login.objects.create(usuario='usuario2', password='password2')

class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('cancha', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('duracion', models.IntegerField()),
                ('cel', models.CharField(max_length=50)),
                ('pago', models.BooleanField(default=False)), 
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.RunPython(create_default_logins),
    ]
