### apple_ai 사용법

1. 전북사과 데이터 다운
2. data/images에 사과 사진 그대로 넣기
3. data/json에 그에 맞는 json 파일 넣기
4. 가상환경 만들기
5. pip install requirements.txt
6. scripts/1_crop_and_extract 파일 실행. (crop된 사과 사진 저장 안하고 싶으면 nosave 적힌거 실행)
7. scripts/2_train_model 실행 하면 features에 저장된 csv파일을 기반으로 xgboost 돌리면 pkl 모델이 나옴
8. 3_predict_from_images에 테스트하고 싶은 사과의, crop된 이미지 경로를 넣어서 테스트 해보면 추론된 당도가 나온다.

- 많이 학습할수록 정확도가 높아질 것 같고, nn 임베딩인가 뭔가 근거를 높일 수 있는 뭔가를 더 찾으면 좋을 것 같다. 