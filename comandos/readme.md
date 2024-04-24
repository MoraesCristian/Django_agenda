Iniciar o projeto Django

python -m venv venv
. venv/bin/activate
pip install django
django-admin startproject project .
python manage.py startapp contact


# Configurando o git inicial -

git config --global user.name 'Seu nome'
git config --global user.email 'seu_email@gmail.com'
git config --global init.defaultBranch main
# Configure o .gitignore
git init
git add .
git commit -m 'Mensagem'
git remote add origin git@github.com:MoraesCristian/Django_agenda.git

# MIGRANDO BASE DE DADOS NO DJANGO 

python manage.py makemigrations
python manage.py migrate

# CRIANDO E MODIFICANDO A SENHA DE UM SUPER USUÁRIO DJANGO

python manage.py createsuperuser

# Alteracao de senha caso esqueça
python manage.py changepassword USERNAME