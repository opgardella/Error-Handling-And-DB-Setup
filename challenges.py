from flask import Flask, render_template, request
import json
import requests

app = Flask(__name__)

# Challenge 1: Return the 404.html template
# Edit it such that it displays an interesting message
@app.errorhandler(404)
def page_not_found(e):
    # return "This page was not found"
    return render_template('404.html')

# Challenge 2: Include the link to homepage i.e. http://localhost:5000 in 404.html.
# DONE

# Challenge 3: Write an error handler for 500 error
@app.errorhandler(500)
def server_overloaded(e):
    # return "Page not found"
    return render_template('500.html')

# Challenge 4: Edit the 500.html template to display link to homepage and link to itunes-form.
# DONE

@app.route('/')
def index():
    return "Hello, World!"

@app.route('/itunes-form')
def ituneForm():
    return render_template('itunes-form.html')

@app.route('/itunes-result', methods = ['GET'])
def resultTunes():
    pass
    if request.method == 'GET':
        base_url = 'https://itunes.apple.com/search?'
        params_diction = {}
        params_diction['term'] = request.args.get('artist')
        params_diction['limit'] = request.args.get('num')
        response = requests.get(base_url, params = params_diction)
        response_text = json.loads(response.text)
        response_py = response_text['results']
        return render_template('list.html', results = response_py)
    flash('Must enter an artist')
    return redirect(url_for('albumform'))


if __name__ == '__main__':
    app.run(debug = True)
