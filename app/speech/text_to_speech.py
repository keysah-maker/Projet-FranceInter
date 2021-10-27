import azure.cognitiveservices.speech as speechsdk
import os, sys


key_speech = 'SPEECH_TEXT_SUBSCRIPTION_KEY'
if key_speech not in os.environ:
    raise Exception('Please set/export the environment variable: {}'.format(key_speech))
subscription_key = os.environ[key_speech]

service_region = "francecentral"
speech_config = speechsdk.SpeechConfig(subscription=subscription_key, region=service_region)


def sound_conversion(message, language):
    if language == 'fr':
        speech_config.speech_synthesis_language = 'fr-FR'
        audio_filename = "static/audios/fr_message.wav"
    elif language == 'en':
        speech_config.speech_synthesis_language = 'en-US'
        audio_filename = "static/audios/en_message.wav"
    else:
        audio_filename = "static/audios/error.wav"

    try:
        audio_output = speechsdk.audio.AudioOutputConfig(filename=audio_filename)
        speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_output)
        speech_synthesizer.speak_text_async(message).get()
    except Exception as e:
        print(str(e))


def text_to_wav(json):
    for translation in json[0]["translations"]:
        sound_conversion(translation["text"], translation["to"])
