<template>
  <div class="drawer">
    <v-navigation-drawer permanent>
      <h1>{{ tripSelected.date_from }} - {{ tripSelected.date_to }}</h1>
      <h3 class="my-0">{{ cityName }} 여행</h3>
      <small>{{ cityCountry }} | {{}}</small>
      <div class="chips mt-3">
        <v-chip>+ 항공편</v-chip>
        <v-chip>+ 숙소</v-chip>
      </div>
      <v-divider></v-divider>
      <div v-if="scheduleList">
        <ScheduleList
          v-for="day in days"
          :ref="`day${day}`"
          :key="day"
          :day="day"
          class="mb-5"
        />
      </div>
    </v-navigation-drawer>
  </div>
</template>

<script>
import { mapState, mapMutations, mapActions } from 'vuex'
import ScheduleList from '../components/ScheduleList'

export default {
  components: {
    ScheduleList
  },
  data() {
    return {
      days: 0,
      tripId: 0,
      tripSelected: 0
    }
  },
  computed: {
    ...mapState({
      scheduleList: state => state.trips.scheduleList,
      dayScroll: state => state.trips.dayScroll
    }),
    cityName() {
      return this.tripSelected.city && this.tripSelected.city.name
    },
    cityCountry() {
      return this.tripSelected.city && this.tripSelected.city.country
    },
    cityContinent() {
      return this.tripSelected.city && this.tripSelected.city.continent
    }
  },
  watch: {
    dayScroll() {
      this.$refs[`day${this.dayScroll}`][0].$el.scrollIntoView({
        behavior: 'smooth',
        inline: 'nearest'
      })
    }
  },
  async created() {
    this.tripId = this.$route.params.tripId
    this.tripSelected = await this.FETCH_TRIP(this.tripId)
    await this.FETCH_SCHEDULELIST({ trip: this.tripSelected.id })
    this.calcDays(this.tripSelected)
  },

  mounted() {},
  methods: {
    ...mapMutations({
      SET_DAYSTOTAL: 'trips/SET_DAYSTOTAL'
    }),
    ...mapActions({
      FETCH_SCHEDULELIST: 'trips/FETCH_SCHEDULELIST',
      FETCH_TRIP: 'trips/FETCH_TRIP'
    }),
    calcDays(tripSelected) {
      const from = tripSelected.date_from
      const to = tripSelected.date_to
      const ar1 = from.split('-')
      const ar2 = to.split('-')
      const da1 = new Date(ar1[0], ar1[1], ar1[2])
      const da2 = new Date(ar2[0], ar2[1], ar2[2])
      const dif = da2 - da1
      const cDay = 24 * 60 * 60 * 1000 // 시 * 분 * 초 * 밀리세컨

      this.days = dif / cDay + 1
      this.SET_DAYSTOTAL(this.days)
    }
  }
}
</script>

<style>
.drawer {
  height: calc(100vh - 49px);
  width: 300px;
  position: fixed;
  z-index: 1;
  /* 스크롤 없애기 위해 */
  -ms-overflow-style: none; /* IE and Edge */
  scrollbar-width: none; /* Firefox */
}
/* 스크롤 없애기 위해 */
.drawer ::-webkit-scrollbar {
  display: none; /* Chrome, Safari, Opera*/
}

.v-navigation-drawer {
  padding: 10px;
}

.v-navigation-drawer__border {
  width: 0px;
}

.v-divider {
  margin: 15px 0;
}
</style>
