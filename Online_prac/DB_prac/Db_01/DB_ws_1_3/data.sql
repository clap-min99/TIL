-- Active: 1728544335844@@127.0.0.1@3306
# 사용자 중에서 first_name이 '하'로 시작하는 사용자 정보 조회
SELECT
  *
FROM 
  users
WHERE
  first_name LIKE '하%';

SELECT
  *
FROM
  users
WHERE
  phone LIKE '%555';

SELECT
  *
FROM 
  users
WHERE
  country LIKE '경상%'

SELECT
  *
FROM 
  users
WHERE
  country LIKE '경_남%' OR country LIKE '충_남%'