<template>
  <div class="container">
    <h2>{{questionnaire.title}}</h2>
    <p>{{questionnaire.description}}</p>
    <p>Дата старта: {{questionnaire.start_date}}</p>
    <p>Дата окнончания: {{questionnaire.end_date}}</p>
    <h3>Список вопросов</h3>
  </div>
</template>


<script>
  import axios from 'axios'

  export default {
    name: 'Questionnaire',
    data(){
      return{
        questionnaire : null
      }
    },
    created: function () {
      axios
          .get(('http://127.0.0.1:8000/questionnaires/blanks/')+this.$route.params.id)
          .then(response => (this.questionnaire = response.data));
      axios
          .get(('http://127.0.0.1:8000/questionnaires/blanks/')+this.$route.params.id)
          .then(response => (this.questionnaire = response.data));
    }

  }
</script>
