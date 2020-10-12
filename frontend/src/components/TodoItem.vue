<template>
  <li>
    <div class="todo__content">{{ todo.text }}</div>
    <div class="todo__priority">{{ todo.priority }}</div>
    <div class="group-btns">
      <div class="todo__status" @click="setStatus">

        <img v-if="!todo.isCompleted" src="https://img.icons8.com/fluent/48/000000/checkmark.png" alt="notCompleted"/>
        <img v-else src="https://img.icons8.com/fluent/48/000000/cancel.png" alt="Completed"/>
      </div>
      <div class="remove-todo-btn" @click="removeTodo">
        <img
            src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAYAAADgdz34AAAABmJLR0QA/wD/AP+gvaeTAAAA0ElEQVRIie1VsQrCMBB9J6Xubk5SMH5B/adQO6ir4C5OCmr/qdkc6yq4iZsF9RxsoVCb1qqIkDflLnfv5V0CIZTA3ex8EI8BONk8A3tiXiop5iDion7SkfeDyGNgpash8DCUvUXRfkPXzIRRwjJhOtlKClJSkNPqWkw8fdSQrz9AAjeICm3WgZKCgBIHf4HcJb87Krpa7XDgHNL46yP6rUD6EqquXxb4BIyAETACRqACnv0HZwDNuoTxzW5tvc4xjXMOGJgBiGtwXxhYZ8kB4A7wsDrMojY1GAAAAABJRU5ErkJggg==">
      </div>
    </div>
  </li>
</template>

<script>

export default {
  name: "TodoItem",
  props: {
    todo: Object,
  },

  methods: {

    removeTodo() {
      this.$emit('remove-todo')
    },

    setStatus(){
      this.$emit('set-status')
    }
  }

}

</script>

<style scoped>

img {
  height: 20px;
}

.group-btns {
  display: flex;
}

.group-btns * {
  padding-left: 15px;
}


.todo__content {
  width: 75%;
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;

}

.todo__priority {
  width: 15%;
}

.remove-todo-btn, .todo__status {
  cursor: pointer;
}


li {
  display: flex;
  padding: 10px;
  list-style: none;
}
</style>