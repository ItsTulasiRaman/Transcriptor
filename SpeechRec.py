"""
#import library
import speech_recognition as sr

def speech_recognition(filename):
    audio_file = filename
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
            return text
        
        except:
            print('Sorry.. run again...')

"""

import speech_recognition as sr
from os import path
from pydub import AudioSegment
import wave, math, contextlib
import moviepy

def speech_recognition(filename):                                                                   
    src = filename
    dst = filename

    # this will return a tuple of root and extension
    split_tup = path.splitext(src)
    print(split_tup)

    # extract the file name and extension
    file_name = split_tup[0]
    file_extension = split_tup[1]

    #audio = "test.mp3"

    #checking if it is a video file
    #and converting it to .mp3
    if file_extension==".mp4":
        videoclip = VideoFileClip(src)
        audioclip = videoclip.audio
        audioclip.write_audiofile(audio)
        audioclip.close()
        videoclip.close()

    # convert wav to mp3                                                            
    sound = AudioSegment.from_mp3(src)
    sound.export(dst, format="wav")

    transcribed_audio_file_name = dst

    with contextlib.closing(wave.open(transcribed_audio_file_name,'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)

    total_duration = math.ceil(duration / 60)
    r = sr.Recognizer()

    for i in range(0, total_duration):
        with sr.AudioFile(transcribed_audio_file_name) as source:
            audio = r.record(source, offset=i*60, duration=60)
            f = open("transcription.txt", "a")
            f.write(r.recognize_google(audio))
            f.write(" ")
            f.close()

    with open('transcription.txt', 'r') as file:
        speech_text = file.read()

    return speech_text
