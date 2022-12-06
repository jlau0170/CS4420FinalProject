// import the axios library
import axios from 'axios';

// specify the URL of the Flask API and the endpoint
const url = 'http://localhost:5000/compress/h264';

// open the video file and read its content
const videoFile = new File(['video.mp4'], 'video.mp4', { type: 'video/mp4' });

// make a POST request to the endpoint with the video file
axios.post(url, videoFile)
  .then(response => {
    // print the response from the Flask API
    console.log(response.data);
  })
  .catch(error => {
    // handle any errors
    console.error(error);
  });
