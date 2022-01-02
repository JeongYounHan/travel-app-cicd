<template>
  <div>
    <Drawer></Drawer>
    <Map></Map>
  </div>
  <!-- <div v-else>해당 여행일정은 존재하지 않습니다.</div> -->
</template>

<script>
// import { mapActions } from 'vuex'
import Drawer from '../../components/Drawer.vue'
import Map from '../../components/Map.vue'

export default {
  components: {
    Drawer,
    Map
  },
  data() {
    return {
      tripId: ''
    }
  },
  async created() {
    // this.tripId = this.$route.params.tripId
    // await this.FETCH_TRIP(this.tripId)
  },
  mounted() {},
  // computed: {
  //   trip() {
  //     return this.$store.state.trips.trips.find(v => v.id == this.tripId)
  //   }
  // },
  methods: {
    // ...mapActions({
    //   FETCH_TRIP: 'trips/FETCH_TRIP'
    // })
  },
  middleware: 'authenticated'
}
</script>

<style></style>
