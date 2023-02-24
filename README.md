# Golden-Raspberry-Awards

API RESTful Leitura da lista de indicados e vencedores da categoria Pior Filme do Golden Raspberry Awards

## Installation

Install with pip:

```
$ pip install -r requirements.txt
```

## Flask Application Structure 
```
.
|──────app/
|       |──── model/
|       |-------|────__init__.py
|       |-------|──────── sql.py
|       |────__init__.py
|       |────  export.py
|       |────  list.csv
|──────run.py
|──────requirements.txt

```

## Run Flask
### Run flask for develop
```
$ python run.py
```
In flask, Default port is `5000`

## Reference

Offical Website

- [Flask](http://flask.pocoo.org/)
- [Flask Extension](http://flask.pocoo.org/extensions/)
- [Flask restplus](http://flask-restplus.readthedocs.io/en/stable/)