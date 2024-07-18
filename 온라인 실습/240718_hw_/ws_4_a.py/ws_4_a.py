# 아래에 코드를 작성하시오.
from conf.settings import NAME
from conf.settings import MAIN_URL
from utils.create_url import create_url


create_url(NAME, MAIN_URL)

print(create_url(NAME, MAIN_URL))