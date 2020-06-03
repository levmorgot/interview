<template>
  <nav class="navbar navbar-expand navbar-dark bg-dark">
    <a class="navbar-brand" href="">Опрсник</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbars" aria-controls="navbars" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbars">
      <ul class="navbar-nav mr-auto">
        <li class="nav-item " :class="{active : activeTab =='interview'}"  @click="toActive('interview')">
          <router-link class="nav-link" to="/" >Опросы<span class="sr-only">(current)</span></router-link>
        </li>
        <li class="nav-item" :class="{active : activeTab =='questions'}" @click="toActive('questions')">
          <router-link class="nav-link" to="/questions" >Вопросы</router-link>
        </li>
      </ul>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'NavBar',
  data(){
    return {
      activeTab:'interview',
    }
  },
  methods:{
    toActive(tab){
      this.activeTab = tab
    }
  }

}
</script>
