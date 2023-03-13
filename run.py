from flask import Flask, jsonify
from flask import make_response
from app import export
from app.model import sql

app = Flask(__name__)


@app.get('/')
def index():
    res = sql.connect().QuerySelect()
    result = export.treatment(res)
    res = list(set(filter(None, result)))
    result = sql.connect().WorstMmovieTreatment(lista=res)
    return make_response(result, 200)

@app.errorhandler(404)
def page_not_found(error):
    result = {
        'status' : '404',
        'mensage' : 'Page Not Found'
    }
    return make_response(jsonify(result), 404)


if __name__ == "__main__":
    export.csv()
    app.debug = False
    app.run(host='0.0.0.0')
