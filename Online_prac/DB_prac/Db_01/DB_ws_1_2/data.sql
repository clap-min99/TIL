-- Active: 1728531640968@@127.0.0.1@3306
# age 18세 미만인 유저를 age 기준으로 내림차순 정렬
SELECT
  *
FROM 
  users
WHERE
  age < 18
ORDER BY
  age DESC;

# age 18세 미만인 유저 last_name과 age 필드만 출력하되
# last_name 기준으로 우선 오름차순 정렬하고, last_name같은 경우 age기준으로 다시 내림차순 정렬
SELECT
  last_name, age
FROM 
  users
WHERE
  age < 18
ORDER BY
  last_name ASC,
  age DESC;


# 위와 동일한 조회, last_name age 동일한 중복 데이터 제외
SELECT DISTINCT
  last_name, age
FROM 
  users
WHERE
  age < 18
ORDER BY
  last_name ASC,
  age DESC;

