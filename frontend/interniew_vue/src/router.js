import Vue from 'vue'
import Router from 'vue-router'
import QuestionnaireList from './views/QuestionnaireList'
import Questionnaire from './views/Questionnaire'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      component: QuestionnaireList
    },
    {
      path: '/questionnaire/:id',
      component: Questionnaire
    },
  ]
})
