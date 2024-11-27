import { createRouter, createWebHistory } from 'vue-router'
import MainView from '@/views/MainView.vue'
import MovieDetailView from '@/views/MovieDetailView.vue'

import SignUpView from '@/views/SignUpView.vue'
import LoginView from '@/views/LoginView.vue'

import BeerView from '@/views/Beer/BeerView.vue'
import AleView from '@/views/Beer/AleView.vue'
import LagerView from '@/views/Beer/LagerView.vue'
import PilsnerView from '@/views/Beer/PilsnerView.vue'
import WheatView from '@/views/Beer/WheatView.vue'
import StoutView from '@/views/Beer/StoutView.vue'

import WhiskeyView from '@/views/Whiskey/WhiskeyView.vue'
import ScotchView from '@/views/Whiskey/ScotchView.vue';
import IrishView from '@/views/Whiskey/IrishView.vue';
import BourbonView from '@/views/Whiskey/BourbonView.vue';
import RyeView from '@/views/Whiskey/RyeView.vue';
import TennesseeView from '@/views/Whiskey/TennesseeView.vue';
import JapaneseView from '@/views/Whiskey/JapaneseView.vue';
import BlendedView from '@/views/Whiskey/BlendedView.vue';
import SingleMaltView from '@/views/Whiskey/SingleMaltView.vue'

import WineView from '@/views/WineView.vue'
import RedView from '@/views/Wine/RedView.vue';
import WhiteView from '@/views/Wine/WhiteView.vue';
import RoseView from '@/views/Wine/RoseView.vue';
import SparklingView from '@/views/Wine/SparklingView.vue';
import NaturalWineView from '@/views/Wine/NaturalWineView.vue';

import NonalcoholView from '@/views/NonalcoholView.vue'

import BestView from '@/views/BestView.vue'

import { useLogStore } from '@/stores/log'
import SearchResultsView from '@/views/SearchResultsView.vue'




const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'MainView',
      component: MainView
    },
    {
      path: '/movies/:moviePk/',
      name: 'MovieDetailView',
      component: MovieDetailView,
      props: true
    },
    {
      path: '/signup',
      name: 'SignUpView',
      component: SignUpView
    },
    {
      path: '/login',
      name: 'LoginView',
      component: LoginView
    },
    {
      path: '/beer/',
      name: 'BeerView',
      component: BeerView
    },
    {
      path: '/whiskey/',
      name: 'WhiskeyView',
      component: WhiskeyView
    },
    {
      path: '/scotch',
      name: 'ScotchView',
      component: ScotchView,
    },
    {
      path: '/singlemalt',
      name: 'SingleMaltView',
      component: SingleMaltView,
    },
    {
      path: '/irish',
      name: 'IrishView',
      component: IrishView,
    },
    {
      path: '/bourbon',
      name: 'BourbonView',
      component: BourbonView,
    },
    {
      path: '/blended',
      name: 'BlendedView',
      component: BlendedView,
    },
    {
      path: '/rye',
      name: 'RyeView',
      component: RyeView,
    },
    {
      path: '/tennessee',
      name: 'TennesseeView',
      component: TennesseeView,
    },
    {
      path: '/japanese',
      name: 'JapaneseView',
      component: JapaneseView,
    },

    {
      path: '/wine/',
      name: 'WineView',
      component: WineView
    },
    {
      path: "/ale",
      name: "AleView",
      component: AleView,
    },
    {
      path: "/lager",
      name: "LagerView",
      component: LagerView,
    },
    {
      path: "/pilsner",
      name: "PilsnerView",
      component: PilsnerView,
    },
    {
      path: "/wheat",
      name: "WheatView",
      component: WheatView,
    },
    {
      path: "/stout",
      name: "StoutView",
      component: StoutView,
    },
    {
      path: '/red',
      name: 'RedWineView',
      component: RedView,
    },
    {
      path: '/white',
      name: 'WhiteView',
      component: WhiteView,
    },
    {
      path: '/rose',
      name: 'RoseView',
      component: RoseView,
    },
    {
      path: '/sparkling',
      name: 'SparklingView',
      component: SparklingView,
    },
    {
      path: '/natural',
      name: 'NaturalWineView',
      component: NaturalWineView,
    },
    {
      path: '/nonalcohol',
      name: 'NonalcoholView',
      component: NonalcoholView,
    },
    {
      path: '/search',
      name: 'SearchResultsView',
      component: SearchResultsView
    },
    {
      path: '/best',
      name: 'BestView',
      component: BestView
    }
  ],
})

router.beforeEach((to, from) => {
  const store = useLogStore()
  // 만약 이동하는 목적지가 메인 페이지이면서
  // 현재 로그인 상태가 아니라면 로그인 페이지로 보냄
  if (to.name === 'MainView' && !store.isLogin) {
    window.alert('로그인이 필요합니다.')
    return { name: 'LoginView' }
  }

  // 만약 로그인 사용자가 회원가입 또는 로그인 페이지로 이동하려고 하면
  // 메인 페이지로 보냄
  if ((to.name === 'SignUpView' || to.name === 'LogInView') && (store.isLogin)) {
    window.alert('이미 로그인 되어있습니다.')
    return { name: 'MainView' }
  }
})

export default router
