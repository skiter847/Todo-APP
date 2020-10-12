import Vue from "vue"
import Vuex from "vuex"
import axios from "axios"

Vue.use(Vuex)

export default new Vuex.Store({
    actions: {
        getTodo(context) {
            axios.get('http://127.0.0.1:8000/items/').then(result => {
                context.commit('updateTodo', result.data)
            })
        },

        deleteTodo(context, id) {
            axios.delete(`http://127.0.0.1:8000/items/${id}`)
            setTimeout(function () {
                context.dispatch('getTodo')
            }, 50)


        },

        addTodo(context, todo) {
            axios.post('http://127.0.0.1:8000/items/', todo)
            setTimeout(function () {
                context.dispatch('getTodo')
            }, 50)

        },

        setTodoStatus(context, id) {
            axios.patch(`http://127.0.0.1:8000/items/${id}`)
            setTimeout(function () {
                context.dispatch('getTodo')
            }, 50)
        }
    },
    mutations: {
        updateTodo(state, todos) {
            state.todos = todos
        },
    },
    state: {
        todos: []
    },
    getters: {
        allTodo(state) {
            return state.todos.sort(function (todo) {
                return todo.isCompleted
            })
        },
    },
})