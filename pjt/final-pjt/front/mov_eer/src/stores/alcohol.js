import { ref } from 'vue'
import { defineStore } from 'pinia'

export const useAlcoholStore = defineStore(
  'alcohol',
  () => {
    // 상태 정의
    const beers = ref([
      {
        name: "Asahi Super Dry",
        imageUrl: "http://127.0.0.1:8000/media/beer_images/Asahi-Super-Dry.jpg",
      },
      {
        name: "Beck's",
        imageUrl: "http://127.0.0.1:8000/media/beer_images/Beck's.jpg",
      },
      {
        name: "Beer Oharas Stout",
        imageUrl: "http://127.0.0.1:8000/media/beer_images/beer-oharas-stout.jpg",
      },
      {
        name: "Blanc",
        imageUrl: "http://127.0.0.1:8000/media/beer_images/blanc.jpg",
      },
      {
        name: "Boston Ale Bottles_Orig",
        imageUrl: "http://127.0.0.1:8000/media/beer_images/boston-ale-bottles_orig.jpg",
      },
      {
        name: "Brewdog_Punk_Ipa",
        imageUrl: "http://127.0.0.1:8000/media/beer_images/BrewDog_Punk_IPA.jpg",
      },
      {
        name: "Budweiser",
        imageUrl: "http://127.0.0.1:8000/media/beer_images/Budweiser.jpg",
      },
      {
        name: "Guinness",
        imageUrl: "http://127.0.0.1:8000/media/beer_images/guinness.jpg",
      },
      {
        name: "Heineken",
        imageUrl: "http://127.0.0.1:8000/media/beer_images/Heineken.jpg",
      },
      {
        name: "Hoegaarden",
        imageUrl: "http://127.0.0.1:8000/media/beer_images/Hoegaarden.jpg",
      },
      {
        name: "Jeju Ale",
        imageUrl: "http://127.0.0.1:8000/media/beer_images/Jeju Ale.jpg",
      },
      {
        name: "Paulaner Hefe Weibier",
        imageUrl: "http://127.0.0.1:8000/media/beer_images/Paulaner Hefe-Weibier.jpg",
      },
      {
        name: "Pilsner Urquell",
        imageUrl: "http://127.0.0.1:8000/media/beer_images/Pilsner Urquell.jpg",
      },
      {
        name: "Weihenstephaner Hefeweissbier",
        imageUrl: "http://127.0.0.1:8000/media/beer_images/Weihenstephaner Hefeweissbier.jpg",
      },
    ])

    const whisky = ref([
        {
            name: "Ardbeg 10 Year Old",
            imageUrl: "http://127.0.0.1:8000/media/whisky_images/Ardbeg 10 Year Old.jpg",
          },
          {
            name: "Balvenie Doublewood 12 Year Old",
            imageUrl: "http://127.0.0.1:8000/media/whisky_images/Balvenie DoubleWood 12 Year Old.jpg",
          },
          {
            name: "Buffalo Trace",
            imageUrl: "http://127.0.0.1:8000/media/whisky_images/Buffalo Trace.jpg",
          },
          {
            name: "Bulleit Rye",
            imageUrl: "http://127.0.0.1:8000/media/whisky_images/Bulleit Rye.jpg",
          },
          {
            name: "Bushmills Black Bush",
            imageUrl: "http://127.0.0.1:8000/media/whisky_images/Bushmills Black Bush.jpg",
          },
          {
            name: "Chivas Regal 12 Year Old",
            imageUrl: "http://127.0.0.1:8000/media/whisky_images/Chivas Regal 12 Year Old.jpg",
          },
          {
            name: "Dewar's White Label",
            imageUrl: "http://127.0.0.1:8000/media/whisky_images/Dewar's White Label.jpg",
          },
          {
            name: "George Dickel No. 12",
            imageUrl: "http://127.0.0.1:8000/media/whisky_images/George Dickel No. 12.jpg",
          },
          {
            name: "Glenfiddich 12 Year Old",
            imageUrl: "http://127.0.0.1:8000/media/whisky_images/Glenfiddich 12 Year Old.jpg",
          },
          {
            name: "Glenlivet 12 Year Old",
            imageUrl: "http://127.0.0.1:8000/media/whisky_images/Glenlivet 12 Year Old.jpg",
          },
          {
            name: "Hibiki Harmony",
            imageUrl: "http://127.0.0.1:8000/media/whisky_images/Hibiki Harmony.jpg",
          },
          {
            name: "Jack Daniel's Old No. 7",
            imageUrl: "http://127.0.0.1:8000/media/whisky_images/Jack Daniel's Old No. 7.jpg",
          },
          {
            name: "Jack Daniel's Single Barrel",
            imageUrl: "http://127.0.0.1:8000/media/whisky_images/Jack Daniel's Single Barrel.jpg",
          },
          {
            name: "Jameson Irish Whiskey",
            imageUrl: "http://127.0.0.1:8000/media/whisky_images/Jameson Irish Whiskey.jpg",
          },
          {
            name: "Johnnie Walker Black Label",
            imageUrl: "http://127.0.0.1:8000/media/whisky_images/Johnnie Walker Black Label.jpg",
          },
          {
            name: "Lagavulin 16 Year Old",
            imageUrl: "http://127.0.0.1:8000/media/whisky_images/Lagavulin 16 Year Old.jpg",
          },
          {
            name: "Macallan Sherry Oak 12 Year Old",
            imageUrl: "http://127.0.0.1:8000/media/whisky_images/Macallan Sherry Oak 12 Year Old.jpg",
          },
          {
            name: "Maker's Mark",
            imageUrl: "http://127.0.0.1:8000/media/whisky_images/Maker's Mark.jpg",
          },
          {
            name: "Nikka From The Barrel",
            imageUrl: "http://127.0.0.1:8000/media/whisky_images/Nikka From the Barrel.jpg",
          },
          {
            name: "Redbreast 12 Year Old",
            imageUrl: "http://127.0.0.1:8000/media/whisky_images/Redbreast 12 Year Old.jpg",
          },
          {
            name: "Sazerac Rye",
            imageUrl: "http://127.0.0.1:8000/media/whisky_images/Sazerac Rye.jpg",
          },
          {
            name: "Wild Turkey Rye",
            imageUrl: "http://127.0.0.1:8000/media/whisky_images/Wild Turkey Rye.jpg",
          },
          {
            name: "Woodford Reserve",
            imageUrl: "http://127.0.0.1:8000/media/whisky_images/Woodford Reserve.jpg",
          },
          {
            name: "Yamazaki 12 Year Old",
            imageUrl: "http://127.0.0.1:8000/media/whisky_images/Yamazaki 12 Year Old.jpg",
          },
    ])

    const wine = ref([
        {
            name: "Cabernet Sauvignon (Robert Mondavi Napa Valley)",
            imageUrl: "http://127.0.0.1:8000/media/wine_images/Cabernet Sauvignon (Robert Mondavi Napa Valley).jpg",
          },
          {
            name: "Cava (Freixenet Cordon Negro Brut)",
            imageUrl: "http://127.0.0.1:8000/media/wine_images/Cava (Freixenet Cordon Negro Brut).jpg",
          },
          {
            name: "Champagne (Moet & Chandon Brut Imperial)",
            imageUrl: "http://127.0.0.1:8000/media/wine_images/Champagne (Moet & Chandon Brut Imperial).jpg",
          },
          {
            name: "Chardonnay (Louis Latour Pouilly Fuisse)",
            imageUrl: "http://127.0.0.1:8000/media/wine_images/Chardonnay (Louis Latour Pouilly-Fuisse).jpg",
          },
          {
            name: "Chateau D'Esclans Garrus Rose",
            imageUrl: "http://127.0.0.1:8000/media/wine_images/Chateau d'Esclans Garrus Rose.jpg",
          },
          {
            name: "Domaine Lapierre Morgon (Beaujolais, France)",
            imageUrl: "http://127.0.0.1:8000/media/wine_images/Domaine Lapierre Morgon (Beaujolais, France).jpg",
          },
          {
            name: "Gut Oggau Josephine (Austria)",
            imageUrl: "http://127.0.0.1:8000/media/wine_images/Gut Oggau Josephine (Austria).jpg",
          },
          {
            name: "Merlot (Chateau Petrus)",
            imageUrl: "http://127.0.0.1:8000/media/wine_images/Merlot (Chateau Petrus).jpg",
          },
          {
            name: "Miraval Rose (Provence)",
            imageUrl: "http://127.0.0.1:8000/media/wine_images/Miraval Rose (Provence).jpg",
          },
          {
            name: "Pinot Noir (Domaine De La Romanee Conti)",
            imageUrl: "http://127.0.0.1:8000/media/wine_images/Pinot Noir (Domaine de la Romanee-Conti).jpg",
          },
          {
            name: "Prosecco (La Marca Prosecco)",
            imageUrl: "http://127.0.0.1:8000/media/wine_images/Prosecco (La Marca Prosecco).jpg",
          },
          {
            name: "Radikon Ribolla Gialla (Italy)",
            imageUrl: "http://127.0.0.1:8000/media/wine_images/Radikon Ribolla Gialla (Italy).jpg",
          },
          {
            name: "Riesling (Dr. Loosen Mosel)",
            imageUrl: "http://127.0.0.1:8000/media/wine_images/Riesling (Dr. Loosen Mosel).jpg",
          },
          {
            name: "Sauvignon Blanc (Cloudy Bay Marlborough)",
            imageUrl: "http://127.0.0.1:8000/media/wine_images/Sauvignon Blanc (Cloudy Bay Marlborough).jpg",
          },
          {
            name: "Whispering Angel Rose (Cotes De Provence)",
            imageUrl: "http://127.0.0.1:8000/media/wine_images/Whispering Angel Rose (Cotes de Provence).jpg",
          },
    ])

    const nonalcohol = ref([
        {
            name: "Americano",
            imageUrl: "http://127.0.0.1:8000/media/pororo_images/americano.jpg",
          },
          {
            name: "Coke",
            imageUrl: "http://127.0.0.1:8000/media/pororo_images/coke.jpg",
          },
          {
            name: "Pororo",
            imageUrl: "http://127.0.0.1:8000/media/pororo_images/pororo.jpg",
          },
          {
            name: "Qoo",
            imageUrl: "http://127.0.0.1:8000/media/pororo_images/qoo.jpg",
          },
          {
            name: "Sprite",
            imageUrl: "http://127.0.0.1:8000/media/pororo_images/sprite.jpg",
          },
    ])

    return { beers, whisky, wine, nonalcohol }
  },
  { persist: true } // persist 설정
)
