<template>
  <div class="container fondo">
    <div class="d-flex fondo-de-pantalla">
      <div
        style="
          display: flex;
          flex-direction: column;
          height: 80vh;
          justify-content: space-between;
          align-items: center;
        "
      >
        <h1>MoneyMate</h1>
        <span id="welcomeMsg"
          >¡Descubre el ChatBot que te <br />
          acompañará en el camino hacia una <br />
          gestión financiera libre de deudas <br />
          al final del mes!
        </span>
        <br />
        <img src="../assets/logo.svg" style="width: 80%" />

        <br />
        <a id="startButton" href="/chatbot-start">Comencemos</a>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "HomeView",
};
</script>
<style>
h1 {
  font-size: 65px !important;
}

#welcomeMsg {
  font-size: 25px;
}

#startButton {
  display: inline-block;
  padding: 10px 90px;
  background-color: black;
  color: #fff;
  text-decoration: none;
  border: none;
  border-radius: 25px;
  cursor: pointer;
}

.fondo {
  background-image: url("../assets/fondo.jpeg");
  background-size: cover;
  background-position: center;
  display: flex;
  justify-content: center;
  text-align: center;
  padding: 10px;
  border-radius: 25px;
}

.fondo-de-pantalla {
  width: 100%;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

.square {
  width: 500px;
  height: 250px;
  border-radius: 35px;
  background-color: #007bff;
  color: #fff;
}
</style>
