import Vue from 'vue'
import VueRouter from 'vue-router'
import mainPage from '../views/mainPage.vue'
import SingleBook from "../views/SingleBook";
import Exchange_chat from "../views/Exchange_chat.vue"
import Login from "../views/Login.vue"
import Profile from "../views/Profile.vue"

Vue.use(VueRouter)

const routes = [
    {
        path: '/login',
        name: 'Login',
        component: Login
    },
    {
        path: '/',
        name: 'mainPage',
        component: mainPage
    },
    {
        path: '/book/:id',
        name: 'SingleBook',
        component: SingleBook,
        props: true
    },
    {
        path: '/exchange_chat/:id',
        name: 'exchange_chat',
        component: Exchange_chat,
        props: true
    },
    {
        path: '/profile',
        name: 'Profile',
        component: Profile,
        props: true
    },
]

const router = new VueRouter({
    mode: 'history',
    routes
})

export default router