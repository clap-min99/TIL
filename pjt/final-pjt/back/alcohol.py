import os
import django
from django.conf import settings

# Django 프로젝트 설정 초기화
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mov_eer.settings")
django.setup()

# 필요한 모델 가져오기
from movies.models import Beer, BeerImage, Whiskey, WhiskeyImage, Wine, WineImage, NonAlcohol, NonAlcoholImage

# media 디렉토리 경로
media_root = settings.MEDIA_ROOT
directories = {
    "beer_images": BeerImage,
    "whiskey_images": WhiskeyImage,
    "wine_images": WineImage,
    "nonalcohol_images": NonAlcoholImage,
}

# 디렉토리 확인 및 이미지 연결
for folder, image_model in directories.items():
    dir_path = os.path.join(media_root, folder)
    print(f"Checking directory: {dir_path}")
    if not os.path.exists(dir_path):
        print(f"Directory {dir_path} does not exist.")
        continue

    for filename in os.listdir(dir_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            file_path = os.path.join(dir_path, filename)
            base_name = os.path.splitext(filename)[0].lower().replace(" ", "_")

            if image_model == BeerImage:
                parent_model = Beer
            elif image_model == WhiskeyImage:
                parent_model = Whiskey
            elif image_model == WineImage:
                parent_model = Wine
            elif image_model == NonAlcoholImage:
                parent_model = NonAlcohol

            try:
                parent_object = parent_model.objects.get(examples__icontains=base_name)
                image_model.objects.create(
                    **{parent_model._meta.model_name: parent_object},
                    image=os.path.join(folder, filename),
                    description=f"Image for {base_name}",
                )
                print(f"Added image {filename} to {parent_model.__name__}.")
            except parent_model.DoesNotExist:
                print(f"No matching {parent_model.__name__} found for {base_name}.")
