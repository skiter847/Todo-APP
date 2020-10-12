<template>
  <form>
    <div class="input__wrapper">
      <input v-model="inputValue"
             type="text"
             placeholder="Добавить новый Todo">
      <p v-if="errorMessagesInput">{{ errorMessagesInput }}</p>
      <p v-if="errorMessagesBtn">{{ errorMessagesBtn }}</p>
    </div>
    <div>
      <h4>Приоритет:</h4>
      <div class="radio__wrapper">
        <input type="radio" id="low" value="Низкий" v-model="priority">
        <label for="low">Низкий
        </label>
        <br>
      </div>
      <div class="radio__wrapper">
        <input type="radio" id="medium" value="Средний" v-model="priority">
        <label for="medium">Средний</label>
        <br>
      </div>
      <div class="radio__wrapper">
        <input type="radio" id="high" value="Высокий" v-model="priority">
        <label for="high">Высокий</label>
        <br>
      </div>
    </div>
    <button type="submit" @click.prevent="createTodo">Добавить</button>
  </form>
</template>

<script>
import {mapActions} from 'vuex'

export default {
  name: "AddTodo",

  data() {
    return {
      inputValue: '',
      priority: '',
      errorMessagesBtn: '',
      errorMessagesInput: '',

    }
  },


  methods: {
    ...mapActions(['addTodo']),

    validateRadioBtns() {
      if (this.priority) {
        return true
      } else {
        this.errorMessagesBtn = 'Выберите преоритет'
      }
    },
    validateInputField() {
      if (this.inputValue) {
        return true
      } else {
        this.errorMessagesInput = 'Введите текст'
      }
    },

    clearErrorMessages() {
      this.errorMessagesInput = ''
      this.errorMessagesBtn = ''
    },

    createTodo() {
      if (this.validateInputField() && this.validateRadioBtns()) {
        const newTodo = {
          text: this.inputValue,
          priority: this.priority,
          isCompleted: false,
        }
        this.addTodo(newTodo)
        this.inputValue = ''
        this.clearErrorMessages()
      }
    }
  }
}


</script>

<style scoped>


form {
  display: flex;
  justify-content: space-around;
  padding: 40px 40px 0 40px;
  border-bottom: 2px solid #87CEFA;
  max-height: 140px;
}

input[type='text'], button {
  margin: 10px;
}

h4 {
  margin: 0;
}

p {
  margin: 0;
  padding-left: 10px;
  color: red;
  font-weight: bold;
}

input[type='text'] {
  padding: 5px;
  font-size: 25px;
  width: 950px;
  border: none;
  border-bottom: 3px solid dodgerblue;
}

.radio__wrapper {
  padding: 5px;
}


button {
  max-height: 50px;
  width: 300px;
  font-size: 25px;
  padding: 10px;
  background-color: dodgerblue;
  border-radius: 6px;
  transition: 0.1s;
}


button:hover {
  cursor: pointer;
  transform: scale(1.1);
  background-color: #4169E1;

}
</style>