var app = new Vue({
  el: '#app-4',
  data: {
    comments: [],
    seen:true,
    unseen:false
  },
  created: function() {
    this.fetchCommentList();
    this.timer = setInterval(this.fetchCommentList, 10000);
  },
  methods: {
    fetchCommentList: function() {
      axios
        .get('/comments/')
        // .then(response => console.log(response.data))
        .then(response => (this.comments = response.data.comments))
      console.log(this.comments)
      this.seen=false
      this.unseen=true
    },
    cancelAutoUpdate: function() { clearInterval(this.timer) }
  },
  beforeDestroy() {
    // clearInterval(this.timer)
    this.cancelAutoUpdate();
  }
})

var app2 = new Vue({
  el: '#app-2',
  data: {
    isOpen: true,
  },
  methods: {
    toggleAccordion: function() {
      this.isOpen = !this.isOpen;
    }
  },
  computed: {
    accordionClassess: function() {
      return {
      'is-closed': !this.isOpen
      };
    }
  }
})
