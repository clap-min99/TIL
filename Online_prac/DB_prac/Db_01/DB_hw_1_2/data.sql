-- Active: 1728527528942@@127.0.0.1@3306

#Track 테이블의 모든 데이터 조회
SELECT
  *
FROM
  tracks;

# Name, Milliseconds, UnitPrice열의 모든 데이터를 조회
SELECT
  Name, Milliseconds, UnitPrice
FROM
  tracks;

# GenreID 행의 값이 1인 모든 데이터 조회
SELECT
  *
FROM
  tracks
WHERE
  GenreID = 1;

# 모든 데이터를 name을 기준으로 오름차순 정렬하여 조회
SELECT 
  *
FROM 
  tracks
ORDER BY 
  Name;


SELECT
  *
FROM
  tracks
LIMIT 10 ASC;