import os
import azure.cognitiveservices.speech as speechsdk

# This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
# Set up the Speech Configuration using the environment variables
speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('SPEECH_KEY'), region=os.environ.get('SPEECH_REGION'))

# Set the voice for speech synthesis
#speech_config.speech_synthesis_voice_name='en-US-JennyNeural'
speech_config.speech_synthesis_voice_name='it-IT-BenignoNeural'

# Set the language for speech recognition
#speech_config.speech_recognition_language="en-EN"
speech_config.speech_recognition_language="it-IT"

def recognize_from_microphone():
    # Set up the audio configuration using the default microphone
    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)

    # Create a Speech Recognizer
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    print("Speak into your microphone.")

    # Perform speech recognition on the audio input from the microphone
    speech_recognition_result = speech_recognizer.recognize_once_async().get()

    if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
        print("Recognized: {}".format(speech_recognition_result.text))
        return speech_recognition_result.text
    elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(speech_recognition_result.no_match_details))
        return "error"
    elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_recognition_result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))
            print("Did you set the speech resource key and region values?")
        return "error"

def text_to_speech(text):
    # Set up the audio output configuration using the default speaker
    audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

    # Create a Speech Synthesizer
    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    
    # Perform speech synthesis to generate audio from text
    speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()

    if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        print("Speech synthesized for text [{}]".format(text))
    elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_synthesis_result.cancellation_details
        print("Speech synthesis canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            if cancellation_details.error_details:
                print("Error details: {}".format(cancellation_details.error_details))
                print("Did you set the speech resource key and region values?")

    return text
