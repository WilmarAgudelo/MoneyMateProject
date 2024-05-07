import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
import HomeView from "../views/HomeView.vue";
import ChatBot from "../views/ChatBot.vue";

const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/chatbot-start",
    name: "ChatBot",
    component: ChatBot,
  },
];

const router = createRouter({
  history: createWebHistory(), // Cambia createWebHashHistory() a createWebHistory()
  routes,
});

export default router;
