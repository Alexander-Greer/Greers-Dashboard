from flask import Flask, redirect, url_for, request, render_template
from waitress import serve


app = Flask(__name__)

@app.route('/')
@app.route('/index')
def hello_world():
    return render_template(
        'index.html',
        bruh_variable="Bruh"
    )

# https://stackoverflow.com/questions/21689364/method-not-allowed-flask-error-405
@app.route('/recipe', methods=['GET', 'POST'])
def recipe():

    submitted_url = request.args.get('recipe_url')
    print("GOT", submitted_url)

    return render_template(
        'recipe.html',
        recipe_url=submitted_url
    )

if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=8000)
