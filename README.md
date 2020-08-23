# BookStoreChallange


## Installation

1. Clone the project

```bash
git clone https://github.com/arachnidiskandar/bookstoreChallange.git
```
2. Create and start a virtual environment
```bash
virtualenv env

source env/bin/activate #linux
env/Scripts/activate    #windowns
```
3. Install the project dependencies
```bash
pip install django
pip install djangorestframework
pip install markdown
pip install django-filter
```
4. change the directory and run the migration
```bash
cd bookstore
python migrate.py migrate
```
5. Create the admin account
```bash
python manage.py createsuperuser
```
6. Run the server
```bash
python manage.py runserver
```
7. Access it through http://127.0.0.1:8000/admin

## Endpoints
http://127.0.0.1:8000/client/id/books/

http://127.0.0.1:8000/books/

http://127.0.0.1:8000/books/id/reserve
