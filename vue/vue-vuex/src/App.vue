<template>
  <div id="app">
    <h2>App.vue</h2>
    <h3>전체 할 일: {{ allTodosCount }}</h3>
    <h3>완료 된 일: {{ completedTodosCount }}</h3>
    <h3>완료 되지 않은 일: {{ uncompletedTodosCount }}</h3>
    <TodoList />
    <TodoForm />
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import TodoForm from '@/components/TodoForm'
import TodoList from '@/components/TodoList'
export default {
  name: 'App',
  components: {
    TodoForm,
    TodoList,
  },
  computed: {
    // allTodosCount: function () {
    //   return this.$store.getters.allTodosCount
    // },
    // completedTodosCount: function () {
    //   return this.$store.getters.completedTodosCount
    // },
    // uncompletedTodosCount: function () {
    //   return this.$store.getters.uncompletedTodosCount
    // },
    // ...mapGetters({
    //   'allTodosCount': 'allTodosCount',
    //   'completedTodosCount': 'completedTodosCount',
    //   'uncompletedTodosCount': 'uncompletedTodosCount',
    // })
    ...mapGetters([
      'allTodosCount',
      'completedTodosCount',
      'uncompletedTodosCount',
    ])
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  border: 3px solid black;
  user-select: none;
}
</style>
