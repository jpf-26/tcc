# Generated by Django 5.1.4 on 2025-03-31 02:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Escala',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('escala_horario', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Troca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Pendente', 'Pendente'), ('Aprovada', 'Aprovada'), ('Rejeitada', 'Rejeitada')], default='Pendente', max_length=10)),
                ('data_solicitada', models.DateTimeField(auto_now_add=True)),
                ('motivo', models.TextField(blank=True, null=True)),
                ('ultima_modificacao', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='UsuarioCustomizado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('numero_atirador', models.IntegerField(blank=True, null=True, unique=True)),
                ('foto', models.ImageField(upload_to='imagens/%Y/%m/%d/')),
                ('nome_completo', models.CharField(max_length=150)),
                ('nome_guerra', models.CharField(max_length=50)),
                ('patente', models.CharField(choices=[('SB', 'Subtenente'), ('A', 'Atirador'), ('S', 'Sargento'), ('C', 'Cabo')], max_length=2)),
                ('comandante', models.CharField(choices=[('S', 'Sim'), ('N', 'Não')], max_length=2)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('data_nascimento', models.DateField()),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=1)),
                ('tipo_sanguineo', models.CharField(blank=True, max_length=3, null=True)),
                ('pai', models.CharField(blank=True, max_length=100, null=True)),
                ('mae', models.CharField(blank=True, max_length=100, null=True)),
                ('cpf', models.CharField(max_length=20, unique=True)),
                ('ra', models.CharField(blank=True, max_length=20, null=True)),
                ('escolaridade', models.CharField(blank=True, max_length=50, null=True)),
                ('trabalho', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='endereço de email')),
                ('senha', models.CharField(max_length=50)),
                ('rua', models.CharField(max_length=100)),
                ('bairro', models.CharField(max_length=100)),
                ('cidade', models.CharField(max_length=100)),
                ('numero_casa', models.CharField(max_length=10)),
                ('complemento', models.CharField(blank=True, max_length=50, null=True)),
                ('cep', models.CharField(max_length=8)),
                ('id_turma', models.IntegerField(blank=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Guarda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio', models.DateTimeField()),
                ('data_fim', models.DateTimeField()),
                ('data_guarda', models.DateTimeField(auto_now_add=True)),
                ('observacoes', models.CharField(max_length=250)),
                ('id_escala', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tcc.escala')),
            ],
        ),
        migrations.CreateModel(
            name='Notificacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_envio', models.DateTimeField(auto_now_add=True)),
                ('mensagem', models.TextField()),
                ('status', models.CharField(choices=[('Enviada', 'Enviada'), ('Lida', 'Lida'), ('Pendente', 'Pendente')], default='Pendente', max_length=10)),
                ('numero_atirador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='numero_atirador')),
                ('id_troca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tcc.troca')),
            ],
        ),
        migrations.CreateModel(
            name='TrocaAtirador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('Solicitante', 'Solicitante'), ('Substituto', 'Substituto')], max_length=12)),
                ('id_troca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tcc.troca')),
                ('numero_atirador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='numero_atirador')),
            ],
        ),
        migrations.CreateModel(
            name='TrocaGuarda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_guarda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tcc.guarda')),
                ('id_troca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tcc.troca')),
            ],
        ),
        migrations.CreateModel(
            name='UsuarioGuarda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_guarda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tcc.guarda')),
                ('numero_atirador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='numero_atirador')),
            ],
        ),
    ]
