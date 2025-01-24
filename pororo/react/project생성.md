## React 프로젝트 생성하기(react v.18, router v.6)

- React 프로젝트를 Vite CLI로 생성하고, PWA 기능추가 하기 위해 vite-plugin-pwa 설정

1. React 프로젝트 생성 

    `npm create vite@latest my-pwa-app --template react`

    (React 프로젝트를 Vite CLI로 생성한 후 React 18을 사용하려면 프로젝트 생성 후 수동으로 React와 React DOM 버전을 설치해야 한다.)

    React, React DOM의 버전을 18로 변경(기존 버전 제거후 react 18 설치)

    `npm uninstall react react-dom`

    `npm install react@18 react-dom@18`

    react 버전 확인

    `npm list react react-dom`

2. 프로젝트로 이동

    `cd my-pwa-app`

3. 필수 패키지 설치(PWA 기능 추가)

    `npm install vite-plugin-pwa --save-dev`

4. `vite.config.js` 설정 

    PWA를 구성하기 위해 vite.config.js 파일에 vite-plugin-pwa 설정

    - vite.config.js

        ```js
        import { defineConfig } from 'vite';
        import react from '@vitejs/plugin-react';
        import { VitePWA } from 'vite-plugin-pwa';

        export default defineConfig({
        plugins: [
            react(),
            VitePWA({
            registerType: 'autoUpdate', // 서비스 워커 자동 업데이트 설정
            manifest: {
                name: 'My PWA App', // 앱의 전체 이름
                short_name: 'PWA App', // 앱의 짧은 이름
                start_url: '/', // 시작 URL
                display: 'standalone', // PWA의 표시 모드
                background_color: '#ffffff', // 배경 색상
                theme_color: '#000000', // 테마 색상
                icons: [
                {
                    src: 'icon-192x192.png', // 192x192 아이콘 경로
                    sizes: '192x192',
                    type: 'image/png',
                },
                {
                    src: 'icon-512x512.png', // 512x512 아이콘 경로
                    sizes: '512x512',
                    type: 'image/png',
                },
                ],
            },
            }),
        ],
        });`
        ```
5. PWA 아이콘 추가

    `vite.config.js` 의
    `manifest.json` 에 설정된 아이콘 경로에 맞게 아이콘 파일 준비 

    - 파일 위치

        프로젝트의 public/ 디렉토리에 아이콘 파일 저장

        파일 이름: icon-192x192.png, icon-512x512.png (이름은 자유롭게 변경 가능, 설정과 일치해야 함).
    
    - 아이콘 크기

        192x192, 512x512

6. 로컬 서버 실행

    개발 중인 PWA 확인하기 위해 로컬 서버 실행

    `npm run dev`

    브라우저에서 http://localhost:5173로 접속

7. PWA 테스트 

    로컬 개발 환경에서는 HTTPS가 기본적으로 활성화되지 않아 PWA 기능(예: 서비스 워커, 설치 가능 여부)이 제한될 수 있다. 

    - vite.config.js에서 HTTPS 서버를 설정하거나

        ```js
        server: {
        https: true,
        },
        ```
    
    - 빌드 후 배포된 환경에서 테스트 한다. 

8. 프로덕션 빌드

    PWA는 정적 파일로 배포되므로 빌드하여 결과물을 생성한다. 

    `npm run build`

    dist/ 디렉토리에 빌드된 파일이 생성된다.

9. 정적 서버에서 실행

    - serve로 실행 

        `npm install -g serve`
        `serve -s dist`

    - url 확인

        브라우저에서 http://localhost:3000으로 접속하여 PWA가 정상적으로 동작하는지 확인

10. PWA 배포 

    PWA는 HTTPS에서 완전한 기능을 제공한다. 

    현재는 nginx 를 이용해서 배포할 예정

11. PWA 테스트 하기

    - 배포 후 브라우저에서 PWA 기능을 확인:

        Chrome DevTools → Application 탭 → Manifest 및 Service Worker 확인.

    - "Install" 버튼 확인:
    
        URL 입력창 옆에 PWA 설치 버튼이 표시되면 성공적으로 설정된 것



### React Router v6

- React router v6 설치 

    `npm install react-router-dom@6`

    버전 확인

    `npm list react-router-dom`

- React Router v6 기본 설정

    React Router v6를 사용하려면 Routes와 Route를 사용해 라우터를 설정해야 한다.

    프로젝트에서  App.jsx 또는 라우팅 설정 파일을 아래와 같이 수정한다.

    ```js
    import React from "react";
    import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

    const Home = () => <h1>Home Page</h1>;
    const About = () => <h1>About Page</h1>;

    function App() {
    return (
        <Router>
        <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/about" element={<About />} />
        </Routes>
        </Router>
    );
    }

    export default App;
    ```

    
