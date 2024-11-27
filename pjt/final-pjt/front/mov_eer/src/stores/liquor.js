import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'
import { createPersistedState } from 'pinia-plugin-persistedstate'


export const useLiquorStore = defineStore('liquor', () => {

    const API_URL = 'http://127.0.0.1:8000'
    const router = useRouter()

    const beers = ref([])
    const beer = ref(null)

    const whiskeys = ref([])
    const whiskey = ref(null)

    const wines = ref([])
    const wine = ref(null)

    const nonalcohols = ref([])
    const nonalcohol = ref(null)


    const getBeers = function() {
        axios({
          method: 'get',
          url: `${API_URL}/api/v1/beers/`
        })
        .then((res) => {
          beers.value = res.data
        })
        .catch((err) => {
          console.log(err)
        })
      }

    const getBeer = function(beerPk) {
        axios({
          method: 'get',
          url: `${API_URL}/api/v1/beers/${beerPk}`
        })
        .then((res) => {
          beer.value = res.data
        })
        .catch((err) => {
          console.log(err)
        })
      }

    const getWhiskeys = function() {
        axios({
          method: 'get',
          url: `${API_URL}/api/v1/whiskeys/`
        })
        .then((res) => {
          whiskeys.value = res.data
        })
        .catch((err) => {
          console.log(err)
        })
      }

      const getWhiskey = function(whiskeyPk) {
        axios({
          method: 'get',
          url: `${API_URL}/api/v1/whiskeys/${whiskeyPk}`
        })
        .then((res) => {
          whiskey.value = res.data
        })
        .catch((err) => {
          console.log(err)
        })
      }
       // Wine API functions
  const getWines = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/wines/`,
    })
      .then((res) => {
        wines.value = res.data;
      })
      .catch((err) => {
        console.log(err);
      });
  };

  const getWine = function (winePk) {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/wines/${winePk}`,
    })
      .then((res) => {
        wine.value = res.data;
      })
      .catch((err) => {
        console.log(err);
      });
  };

  // Nonalcohol API functions
  const getNonalcohols = () => {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/nonalcohols/`,
    })
      .then((res) => {
        nonalcohols.value = res.data;
      })
      .catch((err) => {
        console.log(err);
      });
  };

  const getNonalcohol = function (nonalcoholPk) {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/nonalcohols/${nonalcoholPk}`,
    })
      .then((res) => {
        nonalcohol.value = res.data;
      })
      .catch((err) => {
        console.log(err);
      });
  };

      return{ beers, beer, whiskey, whiskeys,  wines,
        wine,
        nonalcohols,
        nonalcohol,
        getBeer, getBeers, getWhiskey, getWhiskeys,
        getWines,
        getWine,
        getNonalcohols,
        getNonalcohol,}
})