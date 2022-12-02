from flask import Flask
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from CaaS import video_compression
import time

app = Flask(__name__)

@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    return "Hello World!"


@app.route('/upload_video/', methods=['POST'])
def upload_video():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    else:
        filename = "video.mp4"
        file.save(os.path.join("videos/", filename))
        #print('upload_video filename: ' + filename)
        flash('Video successfully uploaded and displayed below')
        return render_template('upload.html', filename=filename)


@app.route('/h264/', methods=['POST'])
def compress_h264():


@app.route('/spc/', methods=['POST'])
def compress_spc():
    

@app.route('/h265/', methods=['POST'])
def compress_h265():
    

@app.route('/av1/', methods=['POST'])
def compress_av1():
    



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)