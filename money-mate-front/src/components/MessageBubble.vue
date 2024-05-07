<template>
  <div :class="['message', position]" :id="loading ? 'loader' : 'message'">
    <span v-html="message" style="text-align: left"></span>
  </div>
</template>

<script>
export default {
  name: "MessageBubble",
  props: {
    message: String,
    sentByMe: Boolean,
    loading: Boolean,
  },
  computed: {
    position() {
      return this.sentByMe ? "right" : "left";
    },
    isLoading() {
      return this.loading ? "loading" : "";
    },
  },
};
</script>

<style scoped>
.message {
  display: flex;
  flex-direction: column;
  max-width: 70%;
  margin: 5px;
  padding: 10px;
  border-radius: 10px;
}

.message.right {
  align-self: flex-end;
  background-color: #f0f0f0;
  border-radius: 35px;
  padding: 15px;
}

.message.left {
  align-self: flex-start;
  background-color: #0075ff;
  border: 1px solid #0075ff;
  border-radius: 35px;
  padding: 15px;
  color: white;
}

span {
  font-size: 20px;
  padding: 0px !important;
  display: block;
  overflow-wrap: break-word;
}

.message-meta.right {
  font-size: 0.8em;
  display: flex;
  justify-content: end;
}

.message-meta.left {
  font-size: 0.8em;
  display: flex;
  justify-content: start;
}

#loader {
  position: relative;
}

#loader::after {
  content: "●";
  animation: typingAnimation 3s infinite;
}

@keyframes typingAnimation {
  0% {
    content: "●";
  }
  33% {
    content: "● ●";
  }
  66% {
    content: "● ● ●";
  }
}
</style>
