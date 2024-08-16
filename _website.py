from flask import Flask, render_template, request
from main import main

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        search = request.form['search']
        output = ""
        results = main(search_query=search)
        first = True

        for x in results:
            if first:
                output += f"{x}:<br>{results[x]}"
                first = False
            else:
                output += f"<br>{x}:<br>{results[x]}"

        return output
    return render_template('website.html')
