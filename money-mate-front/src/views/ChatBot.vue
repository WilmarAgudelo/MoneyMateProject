<template>
  <div class="container fondo" style="height: 100vh">
    <div
      class="d-flex"
      style="display: flex; flex-direction: column; width: 30%"
    >
      <div id="chatContainer">
        <div id="chatBox">
          <div id="chatHeader">
            <div id="logoContainer">
              <a href="/"><img src="../assets/bot.svg" id="" /></a>
              <h2>MoneyMate</h2>
            </div>
            <span>{{ startedDate }}</span>
          </div>
          <div id="messagesBox">
            <MessageBubble
              v-for="(msg, index) in messages"
              :key="index"
              :message="msg.text"
              :loading="msg.loading"
              :sentByMe="msg.sentByMe"
            ></MessageBubble>
          </div>
        </div>
        <div id="messageBox">
          <form @submit.prevent="sendMessage" style="width: 90%">
            <input
              id="clientMessage"
              type="text"
              v-model="newMessage"
              @keyup.enter="sendMessage"
              placeholder="Mensaje"
            />
            <button type="submit" hidden>Send</button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { onMounted, ref } from "vue";
import moment from "moment";
import MessageBubble from "../components/MessageBubble.vue";
import axios from "axios";

export default {
  name: "ChatBot",
  components: { MessageBubble },
  data() {
    return {
      messages: [
        {
          text: "¡Hola!",
          loading: false,
          sentByMe: false,
        },
        {
          text: "¿Qué deseas hacer hoy? <br/> <br/>&nbsp;&nbsp;1 - Registrar Datos <br/>&nbsp;&nbsp;2 - Consultar balance de deudas <br/>&nbsp;&nbsp;3 - Obtener consejos para ahorrar",
          loading: false,
          sentByMe: false,
        },
      ],
      newMessage: "",
      input: null,
    };
  },
  methods: {
    sendMessage(e) {
      e.stopPropagation();
      const message = {
        text: this.newMessage,
        loading: false,
        sentByMe: true,
      };
      this.messages.push(message);
      this.newMessage = "";
      this.input.disabled = true;
      this.onLoadingResponse();
    },
    onLoadingResponse() {
      const message = this.messages[this.messages.length - 1].text;
      this.messages.push({
        text: "",
        loading: true,
        sentByMe: false,
      });
      this.sendMessageRequest(message);
    },
    deleteLoadingMessage() {
      const contenedor = document.getElementById("messagesBox");
      const loader = document.getElementById("loader");

      if (loader) {
        contenedor.removeChild(loader);
        const loaderIndex = this.messages.findIndex(
          (msg) => msg.text === "" && msg.loading
        );
        this.messages.slice(loaderIndex, 1);
      }
    },
    async sendMessageRequest(message) {
      axios
        .post("http://127.0.0.1:5000/get-response", {
          message: message,
        })
        .then((response) => {
          setTimeout(() => {
            this.deleteLoadingMessage();
            setTimeout(() => {
              if (response.status === 200) {
                this.messages.push({
                  text: response.data.response,
                  loading: false,
                  sentByMe: false,
                });
              } else {
                this.messages.push({
                  text: "Perdón, el sistema no está funcionando en estos momentos, intenta más tarde",
                  loading: false,
                  sentByMe: false,
                });
              }
            }, 500);
          }, 4000);
        })
        .catch((e) => {
          console.log("Error" + e);
          setTimeout(
            function () {
              this.deleteLoadingMessage();
              this.messages.push({
                text: "Perdón, el sistema no está funcionando en estos momentos, intenta más tarde",
                loading: false,
                sentByMe: false,
              });
              this.input.disabled = false;
            }.bind(this),
            4000
          );
        });
      this.input.disabled = false;
    },
  },
  mounted() {
    this.input = document.getElementById("clientMessage");
  },
  setup() {
    const startedDate = ref(null);

    onMounted(() => {
      startedDate.value = moment(new Date()).format("[Hoy a las] h:mm A");
    });

    return {
      startedDate,
    };
  },
};
</script>

<style>
#logoContainer img {
  width: 17%;
  position: absolute;
  margin-bottom: 20px;
  top: -2px;
  left: 50%;
  transform: translate(-50%, -50%);
}

#chatHeader {
  display: flex;
  align-items: center;
  flex-direction: column;
  margin-bottom: 10px;
}

#logoContainer {
  margin-top: 25px;
  margin-bottom: 15px;
  background-color: #129fff40;
  border-radius: 50px;
  position: relative;
  height: 95px;
  width: 93%;
  display: flex;
  flex-direction: column;
  justify-content: end;
}

#chatBox {
  widows: 90%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: end;
}

#messagesBox {
  padding: 0px 25px;
  display: flex;
  justify-content: flex-end;
  flex-direction: column;
  max-height: 840px;
  margin-bottom: 20px;
  overflow-y: scroll;
}
#messagesBox::-webkit-scrollbar {
  display: none;
}

#chatContainer {
  display: flex;
  justify-content: space-between;
  background-image: url("../assets/chatFondo.svg");
  background-position: bottom;
  background-size: cover;
  flex-direction: column;
  width: 100%;
  border: 1px solid white;
  height: 95vh;
  overflow-y: auto;
  padding: 10px;
  border-radius: 50px;
  border: 10px solid white;
}

.message {
  margin-bottom: 10px;
}

#messageBox {
  justify-content: center;
  display: flex;
  margin-bottom: 10px;
}
h2 {
  padding: 0px !important;
}

#messageBox input {
  background-color: black;
  border-radius: 50px;
  padding-top: 15px;
  padding-bottom: 15px;
  padding-left: 15px;
  padding-right: 10px;
  font-size: 25px;
  color: white;
  text-align: start;
  justify-content: center;
  display: flex;
  width: 95%;
}
</style>
