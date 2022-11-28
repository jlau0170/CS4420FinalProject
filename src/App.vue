<script setup>
import HelloWorld from './components/HelloWorld.vue'
import TheWelcome from './components/TheWelcome.vue'
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
      <div class="input">
        <input type="file" @change="uploadFile" ref="file">
        <button @click="submitFile">Upload!</button>
      </div>
    <div class="algorithms">
      <h2>
        Algorithm 1
      </h2>
      <h2>
        Algorithm 2
      </h2>
      <h2>
        Algorithm 3
      </h2>
      <h2>
        Algorithm 4
      </h2>
    </div>
    </section>
    <div class="circle1"></div>
    <div class="circle2"></div>
  </main>
</template>

<style scoped>
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
  top: 140px;
  left: 340px;
}

.algorithms {
  top: 220px;
  left: 10px;
  display: flex;
  flex-direction: row;
  justify-content: center;
}

h2 {
  margin: 0 50px;
}

input {
  color: black;
}

button {
  background-color: rgba(25, 171, 255, 0.7);
  color: black;
  border-radius: 15px;
  border-color: rgba(25, 171, 255, 0.7);
  width: 90px;
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
  top: 120px;
  left: 370px;
  color: black;
}
.title {
  top: 80px;
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
}

.row {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
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
