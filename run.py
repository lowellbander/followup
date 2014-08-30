from flask import Flask, render_template, request
import json
import os
import unirest

HEADERS = {'Accept':'application/json', 'Content-Type':'application-json'}

app = Flask(__name__)
app.debug = True

def get(famID):
    response = unirest.get(os.environ['CLERK_URL'] + 'tour/' + famID)
    return response.body

@app.route('/')
def index():
    #they are submitting the form, so post and redirect
    if request.args.get('q1') is not None:
        #post the data
        #TODO: validate that this is an actual family
        data = {}
        data['family'] = request.args.get('family')
        response = unirest.post(CLERK_URL + 'followup/', headers=HEADERS,
                                params = json.dumps(data))
        print response.body
        #redirect
        return render_template('submitted.html')

    #they are asking for a new form
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
            data = {'name': name, 'id':famID}
            return render_template('followup.html', data=data)

if __name__ == '__main__':
    app.run()
