import json
import settings
import unirest

HEADERS = {'Accept':'application/json', 'Content-Type':'application-json'}

def post(followup):
    response = unirest.post(settings.API_URL + 'followup/', headers=HEADERS,
                            params = json.dumps(followup))
    return response.body

def main():
    followup = {'family': '123'}
    print post(followup)

if __name__ == '__main__':
    main()
