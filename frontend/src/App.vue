<template>
  <div id="app">
    <div class="container">
      <div class="header">
        <div class="header__brand">
          <span>TODO-APP</span>
        </div>
        <div class="header__user">
          <img src="../src/assets/default.jpeg" alt="user-logo" height="40" width="40">
        </div>
      </div>
      <AddTodo/>

      <TodoList/>

    </div>
  </div>
</template>

<script>
import AddTodo from "@/components/AddTodo";
import TodoList from "@/components/TodoList";
import {mapActions} from 'vuex';

export default {

  name: 'App',
  components: {
    AddTodo,
    TodoList,
  },

  methods: {
    ...mapActions(['getTodo']),

  },

  mounted() {
    this.getTodo()
  }

}
</script>

<style>
* {
  outline: none;
  border: none;
}

#app {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(to top left, #4169E1, #87CEFA);
}

.container {
  background-color: white;
  height: 700px;
  width: 1500px;
  position: absolute;
  top: 50%;
  left: 50%;
  margin-right: -50%;
  transform: translate(-50%, -50%);
}

.header {
  padding: 40px;
  display: flex;
  justify-content: space-between;
  font-size: 28px;
}

.header__brand span {
  margin-left: 40px;
  font-size: 45px;
}

.header__user {
  margin-right: 80px;
}
</style>
