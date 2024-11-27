<template>
    <div class="container">
      <h1>영화에 나오는 술과 같이 한 잔 🧑‍🤝‍🧑</h1>
      <div class="cards-container">
        <div class="card" v-for="(pairing, index) in pairings" :key="index">
          <div class="card-content">
            <!-- 왼쪽: 술 사진과 설명 -->
            <div class="left-content">
              <div class="image-container">
                <img :src="pairing.drinkImageUrl" alt="술 이미지" class="drink-image" />
              </div>
              <div class="drink-description">
                <h3 class="drink-name">{{ pairing.drinkName }}</h3>
                <p class="drink-details">{{ pairing.drinkType }} / {{ pairing.drinkCountry }} / {{ pairing.drinkPrice }}</p>
                <div class="drink-rating">
                  <p>{{ pairing.alcohol }}</p>
                </div>
              </div>
            </div>
  
            <!-- 오른쪽: 영상과 전체 설명 -->
            <div class="right-content">
              <div class="video-container">
                <iframe
                  v-if="pairing.youtubeUrl"
                  :src="`https://www.youtube.com/embed/${extractYoutubeId(pairing.youtubeUrl)}`"
                  frameborder="0"
                  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                  allowfullscreen
                ></iframe>
                <video
                  v-else
                  :src="pairing.videoUrl"
                  controls
                  muted
                ></video>
              </div>
              <div class="description">
                <p>{{ pairing.description }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  
  <script setup>
  import { ref } from "vue";
  
  const pairings = ref([
    {
      title: "위대한 개츠비 & 모엣샹동",
      drinkImageUrl: "/images/moet.png", // public 폴더 경로
      youtubeUrl: "https://youtu.be/w8IQ3jXuJ1c", // 유튜브 URL
      drinkName: "모엣 샹동 임페리얼 (Moet & Chandon Imperial)",
      drinkType: "스파클링 와인",
      drinkCountry: "프랑스(샹파뉴)",
      drinkPrice: "6~7만원",
      alcohol: '12%, 브리오슈/시리얼/견과류의 달콤하고 부드러운 풍미를 지니고 있습니다',
      description: "영화는 잘 몰라도 익숙한 이 장면, 어떤 술인지 알고 계셨나요?🍾 디카프리오가 명대사와 함께 들어 올린 이 샴페인은 ‘모엣 샹동 임페리얼’으로, 검정, 빨간색이 섞인 병과 코르크를 감싸는 금박지, 고급스러운 모엣 샹동의 로고까지. 호화스러운 파티에 어울리는 술이라고 할 수 있습니다😜. 기분 좋은 날 위대한 개츠비 보면서 모엣 샹동 한 잔 어때요?",
     
    },
  {
    title: "킹스맨 & 달모어12",
    drinkImageUrl: "/images/dalmore.png",
    youtubeUrl: "https://www.youtube.com/watch?v=qMtf3TGU-io", // 유튜브 URL
    drinkName: "달모어(Dalmore)",
    drinkType: "싱글몰트 위스키",
    drinkCountry: "스코틀랜드 하이랜드(Scotland Highland)",
    drinkPrice: "12~15만원",
    alcohol: "40%, 열대과일의 향과 함께 바닐라와 셰리의 맛을 즐길 수 있습니다.",
    description:
      "영화 킹스맨 속 매너가 사람을 만든다는 대사처럼, 달모어는 매너와 품격을 상징하는 술입니다. 풍부한 맛과 향으로, 한 모금만으로도 영화 속 주인공이 된 듯한 기분을 느껴보세요! 🥃"
  },
  {
    title: "신세계 & 시바스리갈 12년",
    drinkImageUrl: "/images/chivas_regal.png",
    youtubeUrl: "https://www.youtube.com/watch?v=Ji0kOp2iSrk", // 유튜브 URL
    drinkName: "시바스리갈(Chivas Regal)",
    drinkType: "블렌디드 위스키",
    drinkCountry: "스코틀랜드(Scotland)",
    drinkPrice: "6~9만원",
    alcohol: "40%, 벌꿀, 잘 익은 사과, 헤이즐넛 향이 어우러진 풍미.",
    description:
      "영화 신세계에서 느껴지는 강렬한 카리스마와 시바스리갈의 부드러움은 완벽한 조화를 이룹니다. 한 잔의 위스키와 함께 영화의 긴장감을 즐겨보세요.🔥"
  },
  {
    title: "기생충 & 로얄살루트 21",
    drinkImageUrl: "/images/royal_salute.png",
    youtubeUrl: "https://www.youtube.com/watch?v=Nt8WpWyGZ74", // 유튜브 URL
    drinkName: "로얄살루트(Royal Salute) 21",
    drinkType: "블렌디드 위스키",
    drinkCountry: "스코틀랜드(Scotland)",
    drinkPrice: "21만~32만원",
    alcohol:
      "40%, 달콤한 배와 멜론, 오렌지 마멀레이드와 스파이시함이 조화를 이룹니다.",
    description:
      "영화 기생충의 고급스러움과 사회적 메시지는 로얄살루트 21년의 깊은 풍미와 닮아 있습니다. 특별한 날, 영화와 함께 로얄살루트의 우아함을 느껴보세요.✨"
  },
    {
      title: "내부자들 & 참이슬",
      drinkImageUrl: "/images/soju.png",
      youtubeUrl: "https://www.youtube.com/watch?v=-NHikS21FAM", // 로컬 비디오 URL
      drinkName: "참이슬",
      drinkType: "쏘주",
      drinkCountry: "한국",
      drinkPrice: "1800~6000원",
      alcohol: '😄🤗🤪🤢👽😇',
      description: "우리반 덕분에 한 학기 너무 즐거웠어요 ~! 저녁에 이슬 한 잔 하러 갑시당 🍻"
    },
  ]);
  
  const extractYoutubeId = (url) => {
    const match = url.match(/(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})/);
    return match ? match[1] : "";
  };
  </script>
  
  
<style scoped>
.container {
  text-align: center;
  padding: 20px;
}

h1 {
  margin-bottom: 20px;
  font-size: 2.5rem;
  color: #fff;
}

.cards-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 40px; /* 카드 간 간격 */
}

.card {
  background-color: rgba(0, 0, 0, 0.8);
  color: #fff;
  border-radius: 16px;
  padding: 30px;
  width: 1000px; /* 카드 너비 확대 */
  text-align: left;
  box-shadow: 0 10px 15px rgba(0, 0, 0, 0.4);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.card:hover {
  transform: scale(1.05);
  box-shadow: 0 12px 20px rgba(0, 0, 0, 0.5);
}

.card-content {
  display: flex;
  gap: 20px;
}

.left-content {
  flex: 1; /* 1:3 비율에서 왼쪽 */
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.right-content {
  flex: 3; /* 1:3 비율에서 오른쪽 */
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.image-container {
  flex: 4; /* 이미지가 설명 칸보다 3배 크기 */
  display: flex;
  justify-content: center;
}

.drink-image {
  width: 100%;
  max-height: 400px;
  object-fit: cover;
  border-radius: 12px;
  box-shadow: 0 6px 10px rgba(0, 0, 0, 0.3);
}

.drink-description {
  flex: 0.8; /* 설명 칸 크기 */
  background-color: rgba(255, 255, 255, 0.1); /* 배경색 추가 */
  padding: 10px;
  border-radius: 8px;
  font-size: 1rem;
  line-height: 1.4;
}

.drink-name {
  font-size: 1.2rem;
  margin-bottom: 10px;
}

.drink-details {
  font-size: 1rem;
  margin-bottom: 10px;
}

.drink-rating {
  font-size: 0.8rem;
  line-height: 1.6;
}

.drink-rating p {
  margin: 5px 0;
}

.video-container {
  position: relative;
  overflow: hidden;
  padding-top: 56.25%; /* 16:9 비율 유지 */
}

iframe,
video {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  border-radius: 12px;
}

/* description 스타일 */
.description {
  margin-top: 15px; /* 영상과 여백 */
  background-color: rgba(255, 255, 255, 0.1);
  padding: 10px;
  border-radius: 8px;
  font-size: 1rem;
  line-height: 1.6;
  color: #fff;
}
</style>

  