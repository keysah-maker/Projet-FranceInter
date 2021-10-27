import os
import json
import requests
from PIL import Image, ImageDraw


key_vision = 'COMPUTER_VISION_SUBSCRIPTION_KEY'
if key_vision not in os.environ:
    raise Exception('Please set/export the environment variable: {}'.format(key_vision))
subscription_key = os.environ[key_vision]

endpoint_vision = 'COMPUTER_VISION_ENDPOINT'
if endpoint_vision not in os.environ:
    raise Exception('Please set/export the environment variable: {}'.format(endpoint_vision))
endpoint = os.environ[endpoint_vision]

analyze_url = endpoint + "vision/v3.0/detect"


def read_json_config(path):
    try:
        with open(path, 'r') as file:
            data = file.read()
        obj = json.loads(data)
    except:
        return -1

    return obj


def get_persons(image_path):
    img = Image.open(image_path)
    draw = ImageDraw.Draw(img)
    image_data = open(image_path, "rb").read()

    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Content-Type': 'application/octet-stream'
    }
    params = {
        'visualFeatures': 'Categories,Description',
    }

    response = requests.post(analyze_url, headers=headers, params=params, data=image_data)
    response.raise_for_status()

    analysis = response.json()

    persons = 0
    for obj in analysis["objects"]:
        if obj["object"] == "person":
            x = obj["rectangle"]["x"]
            y = obj["rectangle"]["y"]
            x2 = x + obj["rectangle"]["w"]
            y2 = y + obj["rectangle"]["h"]
            draw.rectangle(((x, y), (x2, y2)), outline="blue")
            persons += 1
    # img.show()
    return persons

