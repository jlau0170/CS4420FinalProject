<script setup>
import HelloWorld from './components/HelloWorld.vue'
import TheWelcome from './components/TheWelcome.vue'
import axios from 'axios'
</script>

<template>
  <main class="background">
    <section class="glass">
      <h1 class="title">
        PSNR Video Compression
      </h1>
      <h2 class="upload">
        Upload File:
      </h2>
      <div class="video">
        <video id="videoplayer" width="400" height="200" controls style="position: absolute; top: 10px; left: 10px">
        <source id="src" src="src/assets/stock.mp4">
        </video>
      </div>
      <div class="input">
        <input id="file" type="file" @change="uploadFile" ref="file">
        <button id="uploadActionButton" class="uploadButton" @click="submitFile">Upload!</button>
      </div>
     <div class="algorithms">
      <h2>
        Algorithm 1
      </h2>
      <button id="actionButton" class="playButton" @click="loadAnotherVideo">Play</button>
      <h2>
        Algorithm 2
      </h2>
      <button id="actionButton" class="playButton">Play</button>
      <h2>
        Algorithm 3
      </h2>
      <button id="actionButton" class="playButton" @click="loadAnotherVideo">Play</button>
      <h2>
        Algorithm 4
      </h2>
      <button id="backendButton" class="playButton" @click="loadAnotherVideo">Play</button>
    </div>
    <div class="stats">
      <div class="individualStats">
        <h3>
          PSNR:
        </h3>
        <h3>
          Runtime:
        </h3>
        <h3>
          Compression Ratio:
        </h3>
      </div>
      <div class="individualStats">
        <h3>
          PSNR:
        </h3>
        <h3>
          Runtime:
        </h3>
        <h3>
          Compression Ratio:
        </h3>
      </div>
      <div class="individualStats">
        <h3>
          PSNR:
        </h3>
        <h3>
          Runtime:
        </h3>
        <h3>
          Compression Ratio:
        </h3>
      </div>
      <div class="individualStats">
        <h3>
          PSNR:
        </h3>
        <h3>
          Runtime:
        </h3>
        <h3>
          Compression Ratio:
        </h3>
      </div>
    </div>

    </section>
    <div class="circle1"></div>
    <div class="circle2"></div>
  </main>
</template>

<script>
  import { defineComponent } from 'vue'
  import { VideoPlayer } from '@videojs-player/vue'
  import 'video.js/dist/video-js.css'

  export default defineComponent({
    components: {
      VideoPlayer
    }
  })

  window.onload = function() {
    var button = document.getElementById("actionButton");
    var backEndButton = document.getElementById("backendButton");
    var fileUpload = document.getElementById("file");
    var uploadButton = document.getElementById("uploadActionButton");

    var uploadBool = false;

    //hello world
    function testBackEnd() {
      const path = 'http://127.0.0.1:5000/hello/';
        axios.get(path)
          .then((res) => {
            console.log(res.data);
          })
          .catch((error) => {
            // eslint-disable-next-line
            console.error(error);
          });
    }


    //upload video
    function uploadVideo() {
      uploadBool = true;
      const path = 'http://127.0.0.1:5000/upload_video/';
        axios.post(path)
          .then(() => {
            console.log("success");
          })
          .catch((error) => {
            // eslint-disable-next-line
            console.error(error);
          });
    }

    //load new video onto player
    function loadAnotherVideo() {
      if(uploadBool) {
        var video = document.getElementById('videoplayer');
        var source = document.getElementById('src');

        source.src = 'src/assets/stock1.mp4';

        video.load();
        video.play();
        
        console.log({
          source,video
        });
      }
      else {
        console.log(
          "fail"
        );
      }
    }

    button.onclick=loadAnotherVideo;
    backEndButton.onclick=testBackEnd;
    uploadButton.onclick=uploadVideo;
    fileUpload.onchange = function(event) {
      var file = fileUpload.files;
      if(file) {
        console.log("success");
      }
      else {
        console.log("fail");
      }
    }
  }
</script>

<style>
.background {
  background: linear-gradient(
      to right bottom,
      rgba(25, 171, 255, 0.7),
      rgb(10, 230, 255)
    );
    height: 100vh;
    width: 100.2vw;
    right: 10vw;
    overflow: hidden;
}
.input {
  left: 550px;
  top: 150px;
}

.video {
  left: 30px;
}

.algorithms {
  top: 220px;
  display: flex;
  flex-direction: row;
  justify-content: center;
}

input {
  color: black;
}

.uploadButton {
  background-color: rgba(25, 171, 255, 0.7);
  color: black;
  border-radius: 15px;
  border-color: rgba(25, 171, 255, 0.7);
  width: 90px;
  height: 30px;
}

.playButton {
  background-color: rgba(25, 171, 255, 0.7);
  color: black;
  border-radius: 15px;
  border-color: rgba(25, 171, 255, 0.7);
  width: 40px;
  height: 30px;
}

::-webkit-file-upload-button {
  background-color: rgba(25, 171, 255, 0.7);
  color: black;
  border-radius: 15px;
  border-color: rgba(25, 171, 255, 0.7);
  width: 90px;
  height: 30px;
}

.upload {
  top: 90px;
  left: 620px;
  color: black;
}
.title {
  top: 20px;
  left: 250px;
  font-size: 3em;
  color: black;
}
.glass {
    background: white;
    min-height: 80vh;
    width: 1000px;
    background: linear-gradient(
      to right bottom,
      rgba(255, 255, 255, 0.7),
      rgba(255, 255, 255, 0.3)
    );
    border-radius: 2rem;
    z-index: 2;
    backdrop-filter: blur(2rem);
    display: flex;
    flex-direction: column;
    position: relative;
    left: 270px;
    top: 100px;
  }

h2 {
  color: black;
  font-size: 2.0rem;
  margin: 0 15px;
}

h3 {
  color: black;
  font-size: 1.2rem;
  margin: 0 37px;
}

.stats {
  display: flex;
  flex-direction: row;
  top: 250px;
  left: 3px;
}

.individualStats {
  display: flex;
  flex-direction: column;
}

.circle1,
.circle2 {
  background: white;
  background: linear-gradient(
    to right bottom,
    rgba(255, 255, 255, 0.8),
    rgba(255, 255, 255, 0.3)
  );
  height: 20rem;
  width: 20rem;
  position: absolute;
  border-radius: 50%;
}

.circle1 {
  top: 5%;
  right: 10%;
}
.circle2 {
  top: 5%;
  left: 10%;
}
</style>
