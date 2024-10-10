-- Active: 1728548419894@@127.0.0.1@3306

# 30세 이상이면서 balance가 1000 이상
SELECT
  *
FROM
  users
WHERE
  age >= 30 and balance >= 1000;

# balance가 1000이하인 사용자들 중에서 age가 20세 이하
SELECT
  *
FROM 
  users
WHERE
  balance <= 1000 and age <= 20;

# first_name이 현으로 시작하고 country가 제주특별자치도 중 가장 age가 많은 사용자 정보
SELECT
  *
FROM 
  users
WHERE
  first_name LIKE '현%' and country = '제주특별자치도'
ORDER BY
  age DESC LIMIT 1;

# last_name이 박이고 age가 25세 이상인 사람들 중에서 가장 age가 어린 사용자
SELECT
  *
FROM 
  users
WHERE
  last_name = '박' and age>= 25
ORDER BY
  age ASC LIMIT 1;

# first_name이 재은 이거나 영일인 사람들중에서 balance가 가장 많은 사용자
SELECT 
  *
FROM
  users
WHERE 
  first_name IN ('재은', '영일')
ORDER BY
  balance DESC LIMIT 1;

# 각 country 별로 가장 많은 balance를 가진 사용자 정보를 조회, balance를 내림차순 정렬
SELECT
  *
FROM
  users
GROUP BY
  country
HAVING
  MAX(balance)
ORDER BY
  balance DESC;

# age가 30세 이상이면서 balance가 age가 30세 이상인 사용자들의 평균 balance보다 높은 사용자 정보 
SELECT
  *
FROM
  users
