# Django venv

## Fixtures

### dumpdata

All data in database related apps.

$ `python manage.py dumpdata app_name.ModelName [--options]`

e.g.

$ `python manage.py dumpdata auth.User --indent 4 > users.json`

$ `python manage.py dumpdata articles.Article --indent 4 > articles.json`



### loaddata

Import fixtures file to database.

$ `python manage.py loaddata app_name/dumpdata_name.json`

e.g.

$ `python manage.py loaddata articles/articles.json`

