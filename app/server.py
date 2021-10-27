from flask import Flask, render_template, request, send_file
import os
import sys
sys.path.insert(1, './translator/')
from translator import translate
sys.path.insert(1, './speech/')
from text_to_speech import text_to_wav
sys.path.insert(1, './image_analyse/')
from analyse import get_persons, read_json_config

app = Flask(__name__)
app.config['IMAGE_UPLOADS'] = './static/uploads/images/'
app.config['AUDIO_UPLOADS'] = './static/uploads/audios/'
app.config['CONFIG_UPLOADS'] = './static/uploads/configs/'


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/get_message', methods=['POST'])
# TODO -> this route needs protection (mandatory)
def get_message():
    message = request.form['message']
    # TODO -> format message so you can use data in config.json (not mandatory)
    response = translate(message)
    text_to_wav(response)
    return render_template('download.html')


@app.route('/send_audio/<id>')
def send_audio(id):
    if id == 1:
        return send_file('./static/audios/fr_message.wav')
    return send_file('./static/audios/en_message.wav')


@app.route('/analyse', methods=['GET'])
def analyse():
    return render_template('analyse.html')


@app.route('/compute_image', methods=['POST'])
def compute_image():
    image = request.files['image']
    config = request.files['config']
    audiofr = request.files['audio-fr']
    audioen = request.files['audio-en']

    if not image or not config:
        return render_template("error_input.html") # TODO create template for error input (mandatory) it should take parameters (check flask and jinja2)

    image.save(os.path.join(app.config['IMAGE_UPLOADS'], image.filename))
    config.save(os.path.join(app.config['CONFIG_UPLOADS'], config.filename))
    audiofr.save(os.path.join(app.config['AUDIO_UPLOADS'], audiofr.filename))
    audioen.save(os.path.join(app.config['AUDIO_UPLOADS'], audioen.filename))
    nb_person = get_persons(app.config['IMAGE_UPLOADS'] + image.filename)
    conf_obj = read_json_config(app.config['CONFIG_UPLOADS'] + config.filename)

    if conf_obj == -1:
        return render_template("error_input.html")
    if "max_people" in conf_obj:
        try:
            value = int(conf_obj["max_people"])
        except:
            return render_template("error_input.html")
    else:
        return render_template("error_input.html")
    if nb_person > int(conf_obj["max_people"]):
        return render_template('play_sound.html', audio1="uploads/audios/" + audiofr.filename,
                               audio2="uploads/audios/" + audioen.filename)
    return render_template('analyse.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
