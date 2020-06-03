<template>
  <div class="container">
    <h2>Home page</h2>
    <div v-for="questionnaire in questionnaireList" :key="questionnaire.id">
      <router-link :to="'/questionnaire/'+questionnaire.id">{{questionnaire.title}}</router-link>
    </div>
  </div>
</template>


<script>
  import axios from 'axios'

  export default {
    name: 'Questionnaire',
    data(){
      return{
        questionnaireList : []
      }
    },
    created: function () {
      axios
          .get('http://127.0.0.1:8000/questionnaires/blanks/')
          .then(response => (this.questionnaireList = response.data));
      console.log('this.questionnaireList', this.questionnaireList)
    }

  }
</script>