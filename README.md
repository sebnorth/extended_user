django task
===============

###The solution to django-task

cd C:\Users\sebnorth\workspace\django\roboczy
mkdir roboczy
cd roboczy
C:\Python34\python -m venv myvenv
myvenv\Scripts\activate
pip install django==1.9.7
pip install python-dateutil
git clone https://github.com/sebnorth/extended_user.git
cd extended_user
python manage.py makemigrations polls
python manage.py migrate
python manage.py runserver
wpisujemy w adres przeglądarki http://127.0.0.1:8000/polls

link download pojawi się o ile w bazie jest co najmniej jeden user

