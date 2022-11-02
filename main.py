import os
from app import app
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from SpeechRec import speech_recognition
from pydub import AudioSegment

@app.route('/')
def upload_form():
	return render_template('upload.html')

@app.route('/', methods=['POST'])
def upload_video():
	if 'file' not in request.files:
		flash('No file part')
		return redirect(request.url)
	file = request.files['file']
	if file.filename == '':
		flash('No file selected for uploading')
		return redirect(request.url)
	else:
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		file_loc = app.config['UPLOAD_FOLDER']+filename
		if (file_loc.endswith(".mp3")):
			sound = AudioSegment.from_mp3(file_loc)
			sound.export((app.config['UPLOAD_FOLDER']+"audiodata.wav"), format="wav")
		elif(file_loc.endswith(".wav")):
		  os.rename(file_loc, app.config['UPLOAD_FOLDER']+"audiodata.wav") 
		filename=app.config['UPLOAD_FOLDER']+"audiodata.wav"
		#print('upload_video filename: ' + filename)
		flash('Audio successfully uploaded and displayed below')
		return render_template('upload.html', filename=filename,speech_text = speech_recognition(filename))

@app.route('/display/<filename>')
def display_video(filename):
	#print('display_video filename: ' + filename)
	return redirect(url_for('', filename=filename), code=301)


if __name__ == "__main__":
    app.run(host='0.0.0.0')