<template>
  <div id="todo-form">
    <h2>TodoForm.vue</h2>
    <input type="text" v-model.trim="todoTitle" @keypress.enter="createTodo">
    <button @click="createTodo">Add</button>
  </div>
</template>

<script>
export default {
  name: 'TodoForm',
  data: function () {
    return {
      todoTitle: '',
    }
  },
  methods: {
    createTodo: function () {
      const todoItem = {
        title: this.todoTitle,
        completed: false,
      }
      if (todoItem.title) {
        this.$store.dispatch('createTodo', todoItem)
      }
      this.todoTitle = ''
    }
  }

}
</script>

<style>
#todo-form {
  width: 50%;
  margin: 1rem auto;
  border: 3px solid skyblue;
}
</style>
