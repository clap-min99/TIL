import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import { VitePWA } from 'vite-plugin-pwa';

// https://vite.dev/config/
export default defineConfig({
  plugins: [react(),
  VitePWA({
    registerType: 'autoUpdate', // 서비스 워커 자동 업데이트 설정
    devOptions: {
        enabled: true, // 개발 환경에서 PWA 활성화
      },
    manifest: {
        name: 'My PWA App', // 앱의 전체 이름
        short_name: 'PWA App', // 앱의 짧은 이름
        start_url: '/', // 시작 URL
        display: 'standalone', // PWA의 표시 모드
        background_color: '#ffffff', // 배경 색상
        theme_color: '#000000', // 테마 색상
        icons: [
        {
            src: '192image.png', // 192x192 아이콘 경로
            sizes: '192x192',
            type: 'image/png',
        },
        {
            src: '512image.png', // 512x512 아이콘 경로
            sizes: '512x512',
            type: 'image/png',
        },
        ],
    },
    }),
],
})
