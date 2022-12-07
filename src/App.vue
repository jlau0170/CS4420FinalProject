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
        <source id="src" src="src/assets/input.mp4">
        </video>
      </div>
      <div class="input">
        <form id="uploadForm" enctype="multipart/form-data" v-on:change="uploadFile">
        <input id="file" type="file" @change="uploadFile">
        <button id="uploadActionButton" type = "button" class="uploadButton">Upload!</button>
        </form>
      </div>
     <div class="algorithms">
      <h2>
        MPEG4
      </h2>
      <button id="mpeg4" class="playButton" @click="loadAnotherVideo">Run</button>
      <h2>
        h265
      </h2>
      <button id="h265" class="playButton">Run</button>
      <h2>
        MPEG2
      </h2>
      <button id="mpeg2" class="playButton" @click="loadAnotherVideo">Run</button>
      <h2>
        h264
      </h2>
      <button id="h264" class="playButton" @click="loadAnotherVideo">Run</button>
    </div>
    <div class="stats">
      <div class="individualStats">
        <h3 id = "mpeg4psnr">
          PSNR:
        </h3>
        <h3 id = "mpeg4runtime">
          Runtime:
        </h3>
        <h3 id = "mpeg4ratio">
          Compression Ratio:
        </h3>
      </div>
      <div class="individualStats">
        <h3 id = "h265psnr">
          PSNR:
        </h3>
        <h3 id = "h265runtime">
          Runtime:
        </h3>
        <h3 id = "h265ratio">
          Compression Ratio:
        </h3>
      </div>
      <div class="individualStats">
        <h3 id = "mpeg2psnr">
          PSNR:
        </h3>
        <h3 id = "mpeg2runtime">
          Runtime:
        </h3>
        <h3 id = "mpeg2ratio">
          Compression Ratio:
        </h3>
      </div>
      <div class="individualStats">
        <h3 id = "h264psnr">
          PSNR:
        </h3>
        <h3 id = "h264runtime">
          Runtime:
        </h3>
        <h3 id = "h264ratio">
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
    var h265Button = document.getElementById("h265");
    var mpeg4Button = document.getElementById("mpeg4");
    var mpeg2Button = document.getElementById("mpeg2");
    var h264Button = document.getElementById("h264");
    var backEndButton = document.getElementById("backendButton");
    var fileUpload = document.getElementById("file");
    var uploadButton = document.getElementById("uploadActionButton");
    var file = new File(['src/assets/stock1.mp4'], 'video.mp4', { type: 'video/mp4' });
    var uploadBool = false;

    //hello world

    function h265Function() {
      const path = 'http://localhost:105/compress-video/h265';
        axios.get(path)
          .then((res) => {
            console.log(res.data);
            document.getElementById("h265psnr").innerHTML = "PSNR: " + parseFloat(res.data["psnr"]).toFixed(2);
            document.getElementById("h265runtime").innerHTML = "Runtime: " + parseFloat(res.data["compression_time"]).toFixed(2) + " seconds";
            document.getElementById("h265ratio").innerHTML = "Compression Ratio: " + parseFloat(res.data["compression_ratio"]).toFixed(2);
          })
          .catch((error) => {
            // eslint-disable-next-line
            console.error(error);
          });
    }

    function h264Function() {
      const path = 'http://localhost:105/compress-video/h264';
        axios.get(path)
          .then((res) => {
            console.log(res.data);
            document.getElementById("h264psnr").innerHTML = "PSNR: " + parseFloat(res.data["psnr"]).toFixed(2);
            document.getElementById("h264runtime").innerHTML = "Runtime: " + parseFloat(res.data["compression_time"]).toFixed(2) + " seconds";
            document.getElementById("h264ratio").innerHTML = "Compression Ratio: " + parseFloat(res.data["compression_ratio"]).toFixed(2);
          })
          .catch((error) => {
            // eslint-disable-next-line
            console.error(error);
          });
    }

    function mpeg4Function() {
      const path = 'http://localhost:105/compress-video/mpeg4';
        axios.get(path)
          .then((res) => {
            console.log(res.data);
            document.getElementById("mpeg4psnr").innerHTML = "PSNR: " + parseFloat(res.data["psnr"]).toFixed(2);
            document.getElementById("mpeg4runtime").innerHTML = "Runtime: " + parseFloat(res.data["compression_time"]).toFixed(2) + " seconds";
            document.getElementById("mpeg4ratio").innerHTML = "Compression Ratio: " + parseFloat(res.data["compression_ratio"]).toFixed(2);
          })
          .catch((error) => {
            // eslint-disable-next-line
            console.error(error);
          });
    }

    function mpeg2Function() {
      const path = 'http://localhost:105/compress-video/mpeg2';
        axios.get(path)
          .then((res) => {
            console.log(res.data);
            document.getElementById("mpeg2psnr").innerHTML = "PSNR: " + parseFloat(res.data["psnr"]).toFixed(2);
            document.getElementById("mpeg2runtime").innerHTML = "Runtime: " + parseFloat(res.data["compression_time"]).toFixed(2) + " seconds";
            document.getElementById("mpeg2ratio").innerHTML = "Compression Ratio: " + parseFloat(res.data["compression_ratio"]).toFixed(2);
          })
          .catch((error) => {
            // eslint-disable-next-line
            console.error(error);
          });
    }


    //upload video
    function uploadVideo() {
      uploadBool = true;
      const path = 'http://localhost:105/upload-video';
      var formData = new FormData();
      var videofile = document.querySelector('#file');
      console.log(videofile);
      formData.append("video", videofile.files[0]);
      axios.post(path, formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
      })

    }

    //load new video onto player
    function loadAnotherVideo() {
      if(uploadBool) {
        var video = document.getElementById('videoplayer');
        var source = document.getElementById('src');

        source.src = 'src/videos/output.mp4';

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

    uploadButton.onclick=uploadVideo;
    h265Button.onclick = h265Function;
    h264Button.onclick = h264Function;
    mpeg2Button.onclick = mpeg2Function;
    mpeg4Button.onclick = mpeg4Function;
    fileUpload.onchange = function(event) {


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
  margin: 0 50px;
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
  right: 20%;
}
.circle2 {
  top: 5%;
  left: 10%;
}
</style>
