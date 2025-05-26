# scripts/17_crop_sample_images.py

import os
import cv2
import json
import numpy as np

IMG_DIR = 'data/SSC_C_images'
JSON_DIR = 'data/SSC_C_json'
CROP_DIR = 'crops/Csamples'
os.makedirs(CROP_DIR, exist_ok=True)

# 최대 N개만 처리
MAX_SAMPLES = 5
count = 0

for filename in os.listdir(JSON_DIR):
    if not filename.endswith('.json'):
        continue

    json_path = os.path.join(JSON_DIR, filename)
    with open(json_path, 'r', encoding='utf-8-sig') as f:
        meta = json.load(f)

    img_name = meta['images']['img_file_name']
    img_path = os.path.join(IMG_DIR, img_name)
    if not os.path.exists(img_path):
        continue

    # 마스크 영역 추출
    points = np.array(meta['annotations']['segmentation']).reshape(-1, 2).astype(np.int32)
    original = cv2.imread(img_path)
    mask = np.zeros(original.shape[:2], dtype=np.uint8)
    cv2.fillPoly(mask, [points], 255)

    masked = cv2.bitwise_and(original, original, mask=mask)
    x, y, w, h = cv2.boundingRect(mask)
    crop = masked[y:y+h, x:x+w]

    crop_name = os.path.splitext(img_name)[0] + '_crop.jpg'
    crop_path = os.path.join(CROP_DIR, crop_name)
    cv2.imwrite(crop_path, crop)
    print(f"✅ 저장 완료: {crop_name}")

    count += 1
    if count >= MAX_SAMPLES:
        break

print("\n📦 샘플 이미지 10개 크롭 완료!")
