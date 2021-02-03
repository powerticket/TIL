<template>
  <div id="todo">
    <div>
      <span :class="{ completed: todo.completed }" @click="updateTodoStatus(todo)">{{ todo.title }}</span>
    </div>
    <button @click="deleteTodo(todo)">Delete</button>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
export default {
  name: 'Todo',
  props: {
    todo: Object,
  },
  methods: {
    // deleteTodo: function () {
    //   this.$store.dispatch('deleteTodo', this.todo)
    // },
    // updateTodoStatus: function () {
    //   this.$store.dispatch('updateTodoStatus', this.todo)
    // },
    ...mapActions([
      'deleteTodo',
      'updateTodoStatus',
    ])
  }
}
</script>

<style scoped>
#todo {
  margin: 1rem auto;
  width: 75%;
  border: 3px solid yellowgreen;
}
.completed {
  text-decoration: line-through;
}
</style>