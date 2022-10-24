#import library
import speech_recognition as sr


def speech_recognition():
    audio_file = 'f2bjrop1.0.wav'
    # Initialize recognizer class (for recognizing the speech)
    r = sr.Recognizer()

    # Reading Audio file as source
    # listening the audio file and store in audio_text variable

    with sr.AudioFile(audio_file) as source:
        
        audio_text = r.listen(source)
        
    # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
        try:
            
            # using google speech recognition
            text = r.recognize_google(audio_text)
            print('Converting audio transcripts into text ...')
            print("Converted test: ")
            return text
        
        except:
            print('Sorry.. run again...')
