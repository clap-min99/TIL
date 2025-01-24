## PWA 개발을 위한 기본 준비

#### 기술 스택

- HTML, CSS, Javascript

- React(ver18)
 
#### 주요 개념

- 서비스 워커(service worker): PWA의 핵심으로 오프라인 캐싱, 푸시 알림 등을 처리

- Manifest 파일: 앱 이름, 아이콘, 시작 url 등 앱의 메타 정보 정의

- 오프라인 지원: 캐싱, 네트워크 전략을 통해 앱이 네트워크 없이도 동작하도록 만듦

## 설치 및 설정

#### 코드 편집도구

- VS code
    
    - PWA 개발에 필요한 확장 프로그램

        Live server(실시간 미리보기)
        
        PWA studio(PWA 분석)

- Node.js & npm 

    - PWA 개발을 위한 패키지 설치를 위해 필요

- CLI 도구

    - Vite

- Lighthouse(PWA 분석 도구)

    - Chrome DevTools에 내장된 도구, PWA 성능과 호환성을 테스트

    - Chrome에서 DevTools 열기 → Lighthouse 탭 → PWA 테스트 실행


## PWA 학습 

### 기본 개념 이해 

- PWA 란?
    
    [MDN progressive Web Apps](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps)

- Mainfest 파일 작성법
    
    [MDN Web app Mainfest](https://developer.mozilla.org/en-US/docs/Web/Manifest)

#### 서비스 워커 구현

- 기본적인 서비스 워커 등록 및 설치 

    서비스 워커는 PWA의 기본 부분입니다. 
    빠른 로드 (네트워크와 무관), 오프라인 액세스, 푸시 알림 및 기타 기능을 지원

    ```js
    if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('/service-worker.js').then(registration => {
        console.log('Service Worker registered:', registration);
    }).catch(error => {
        console.error('Service Worker registration failed:', error);
    });
    }
    ```

#### Mainfest 파일 

- manifest.json 파일 작성

    ```json
    {
    "name": "My PWA",
    "short_name": "PWA",
    "start_url": "/",
    "display": "standalone",
    "background_color": "#ffffff",
    "theme_color": "#000000",
    "icons": [
        {
        "src": "icon-192x192.png",
        "sizes": "192x192",
        "type": "image/png"
        },
        {
        "src": "icon-512x512.png",
        "sizes": "512x512",
        "type": "image/png"
        }
    ]
    }
    ```

#### 캐싱 및 오프라인 지원

- CacheStorage API(캐싱)

    Cache Storage API를 사용하여 기기의 애셋을 다운로드, 저장, 삭제 또는 업데이트할 수 있다. 그러면 이러한 애셋을 네트워크 요청 없이 기기에서 제공할 수 있다.

- Workbox 라이브러리 적용

#### 추천 도구, 라이브러리

- Workbox

    구글에서 제공하는 PWA용 라이브러리. 캐싱과 서비스워커 작업 단순화

- PWA builder

    Mainfest, 서비스 워커 설정을 자동생성 해주는 도구

    [pwa builder](https://www.pwabuilder.com/)



#### PWA Starter Quick Start(사용 안함)

- PWABuilder CLI 이용

    PWA Starter, PWABuilder CLI 이용하려면 Node.js, npm만 설치되어 있으면 된다. 

    - PWA Builder CLI 설치
        
        `npm i -g @pwabuiler/cli`


- CLI 이용해서 앱 만들기

    CLI 설치 후, app 이름 설정

    `pwa create <app-name>` 

    npx를 사용하고 있으면, 

    `npx @pwabuilder/cli craete<app-name>` 

    으로 설치하기
    
    npm dependencies, template 설치

    
- 로컬에서 deploy 하기

    `pwa start`


- 요약

    1. 우리는 Vite 기반 react pjt를 생성할 예정
        
        위 방법은 PWA 프로젝트 생성에 특화된 방법이므로,

        사용하지 않을 것이다.

        pwa 이해를 위해 정리함 

    2. Vite 기반 react 프로젝트 생성 방법은 프로젝트생성.md에 정리 

        `npm create vite@latest <appname> --template react`

        이렇게 만들면 pwa 기능(vite-plugin-pwa)을 추가로 설치해야함 
        (`npm install vite-plugin-pwa --save-dev`)
    


    
    