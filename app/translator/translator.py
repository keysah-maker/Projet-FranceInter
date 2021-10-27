import os, uuid, requests, json

key_translator = 'TRANSLATOR_TEXT_SUBSCRIPTION_KEY'
if key_translator not in os.environ:
    raise Exception('Please set/export the environment variable: {}'.format(key_translator))
subscription_key = os.environ[key_translator]

base_url = 'https://api.cognitive.microsofttranslator.com'
path = '/translate?api-version=3.0'
params = '&to=en&to=fr'
constructed_url = base_url + path + params

headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Ocp-Apim-Subscription-Region': 'westeurope',
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }


def translate(message):
    body = [{
        'text': message
    }]
    request = requests.post(constructed_url, headers=headers, json=body)
    response = request.json()
    #print(json.dumps(response, sort_keys=True, indent=4, ensure_ascii=False, separators=(',', ': ')))
    return response
