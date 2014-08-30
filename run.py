from flask import Flask, render_template, request
import os
import unirest

app = Flask(__name__)
app.debug = True

def get(famID):
    response = unirest.get(os.environ['CLERK_URL'] + 'tour/' + famID)
    return response.body

@app.route('/')
def index():
    famID = request.args.get('id')
    if famID is None:
        return render_template('index.html')
    else:
        fam = get(famID)
        try:
            name = fam['name']
        except TypeError:
            return "invalid ID in URL"
        else:
            return render_template('followup.html')

if __name__ == '__main__':
    app.run()
