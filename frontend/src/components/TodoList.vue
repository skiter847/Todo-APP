<template>
  <ul>
    <TodoItem v-for="(todo, index) in allTodo"
              :todo="todo"
              :key="index"
              @remove-todo="removeTodo(todo.id)"
              @set-status="setStatus(todo.id)"
    />
  </ul>
</template>

<script>
import {mapActions, mapGetters} from 'vuex';
import TodoItem from "@/components/TodoItem";

export default {

  name: "TodoList",
  components: {
    TodoItem
  },
  computed: mapGetters(['allTodo']),


  methods: {
    ...mapActions(['deleteTodo', 'setTodoStatus']),

    removeTodo(id){
      this.deleteTodo(id)
    },

    setStatus(id){
      this.setTodoStatus(id)
    }
  }
}
</script>

<style>
ul {
  max-height: 400px;
  width: 97%;
  overflow-y: scroll;
}

/* width */
::-webkit-scrollbar {
  width: 10px;
}

/* Track */
::-webkit-scrollbar-track {
  background: #f1f1f1;
}

/* Handle */
::-webkit-scrollbar-thumb {
  background: #4169E1;
}

/* Handle on hover */
::-webkit-scrollbar-thumb:hover {
  background: #555;
}
</style>