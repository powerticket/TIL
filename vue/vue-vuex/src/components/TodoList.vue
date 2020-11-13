<template>
  <div id="todo-list">
    <h2>TodoList.vue</h2>
    <Todo
      v-for="(todo, idx) in todos"
      :key="idx"
      :todo="todo"
    />
  </div>
</template>

<script>
import { mapState } from 'vuex'
import Todo from './Todo'

export default {
  name: 'TodoList',
  components: {
    Todo,
  },
  computed: {
    // todos: function () {
    //   return this.$store.state.todos
    // }
    // ...mapState({
    //   'todos': 'todos',
    // })
    ...mapState([
      'todos',
    ])
  }
}
</script>

<style>
#todo-list {
  width: 50%;
  margin: 1rem auto;
  border: 3px solid olive;
}
</style>
