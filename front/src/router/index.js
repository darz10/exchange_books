import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/mainPage.vue'
import Single from "../views/SingleBook";

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'mainPage',
        component: Home
    },
    {
        path: '/:id',
        name: 'SingleBook',
        component: Single,
        props: true
    },
]

const router = new VueRouter({
    mode: 'history',
    routes
})

export default router