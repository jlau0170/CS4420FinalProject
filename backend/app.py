from flask import Flask, request, render_template
from skvideo.measure import psnr
import skvideo.io
import time
import ffmpeg
import os
import os.path
import subprocess
import numpy as np

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def welcome():
    return render_template('index.html')


@app.route('/upload-video', methods=['POST'])
def upload_video():

    print("hello")
    print(request.files)
    # Get the file from the POST request
    file = request.files['video']

    # Save the file to the specified location
    file.save('videos/' + "input.mp4")

    return "200"


def PSNR(compressed_video, original_video):
    return subprocess.check_output(["ffmpeg.exe -i " + compressed_video + " -i " + original_video + " -lavfi psnr=stats_file=psnr_logfile.txt -f null -"])


@app.route('/compress-video/mpeg4')
def compress_video_mpeg4():
    # Start the timer
    start_time = time.time()

    # Use the ffmpeg tool to compress the video with the H.264 codec
    subprocess.run(['ffmpeg','-y', '-i', 'videos/input.mp4', '-c:v', 'mpeg4', 'videos/output.mp4'])

    # Stop the timer and calculate the elapsed time
    elapsed_time = time.time() - start_time

    # Calculate the input and output file sizes
    input_size = os.path.getsize('videos/input.mp4')
    output_size = os.path.getsize('videos/output.mp4')

    # Calculate the compression ratio
    ratio = output_size / input_size

    ref = skvideo.io.vread('videos/input.mp4', as_grey=True)
    dis = skvideo.io.vread('videos/output.mp4', as_grey=True)

    scores = skvideo.measure.psnr(ref, dis)

    avg_score = np.mean(scores)

    return {
        'compression_time': elapsed_time,
        'compression_ratio': ratio,
        'psnr': avg_score
    }



@app.route('/compress-video/h265')
def compress_video_h265():
    # Start the timer
    start_time = time.time()

    # Use the ffmpeg tool to compress the video with the H.264 codec
    subprocess.run(['ffmpeg','-y', '-i', 'videos/input.mp4', '-c:v', 'hevc', 'videos/output.mp4'])

    # Stop the timer and calculate the elapsed time
    elapsed_time = time.time() - start_time

    # Calculate the input and output file sizes
    input_size = os.path.getsize('videos/input.mp4')
    output_size = os.path.getsize('videos/output.mp4')

    # Calculate the compression ratio
    ratio = output_size / input_size


    ref = skvideo.io.vread('videos/input.mp4', as_grey=True)
    dis = skvideo.io.vread('videos/output.mp4', as_grey=True)

    scores = skvideo.measure.psnr(ref, dis)

    avg_score = np.mean(scores)


    return {
        'compression_time': elapsed_time,
        'compression_ratio': ratio,
        'psnr': avg_score
    }



@app.route('/compress-video/mpeg2')
def compress_video_dirac():
    # Start the timer
    start_time = time.time()

    # Use the ffmpeg tool to compress the video with the H.264 codec
    subprocess.run(['ffmpeg', '-y', '-i', 'videos/input.mp4', '-c:v', 'mpeg2video', 'videos/output.mp4'])

    # Stop the timer and calculate the elapsed time
    elapsed_time = time.time() - start_time

    # Calculate the input and output file sizes
    input_size = os.path.getsize('videos/input.mp4')
    output_size = os.path.getsize('videos/output.mp4')

    # Calculate the compression ratio
    ratio = output_size / input_size

    ref = skvideo.io.vread('videos/input.mp4', as_grey=True)
    dis = skvideo.io.vread('videos/output.mp4', as_grey=True)

    scores = skvideo.measure.psnr(ref, dis)

    avg_score = np.mean(scores)


    return {
        'compression_time': elapsed_time,
        'compression_ratio': ratio,
        'psnr': avg_score
    }



@app.route('/compress-video/h264')
def compress_video_h264():
    # Start the timer
    start_time = time.time()

    # Use the ffmpeg tool to compress the video with the H.264 codec
    subprocess.run(['ffmpeg', '-y', '-i', 'videos/input.mp4', '-c:v', 'h264_videotoolbox', 'videos/output.mp4'])

    # Stop the timer and calculate the elapsed time
    elapsed_time = time.time() - start_time

    # Calculate the input and output file sizes
    input_size = os.path.getsize('videos/input.mp4')
    output_size = os.path.getsize('videos/output.mp4')

    # Calculate the compression ratio
    ratio = output_size / input_size


    ref = skvideo.io.vread('videos/input.mp4', as_grey=True)
    dis = skvideo.io.vread('videos/output.mp4', as_grey=True)

    scores = skvideo.measure.psnr(ref, dis)

    avg_score = np.mean(scores)


    return {
        'compression_time': elapsed_time,
        'compression_ratio': ratio,
        'psnr': avg_score
    }



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=105)
