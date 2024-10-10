-- Active: 1728547599325@@127.0.0.1@3306
# 데이터 조회: 테이블 songs에서 모든 음악데이터 조회 
SELECT
  *
FROM
  songs;

# 데이터 정렬: songs에서 음악의 title을 기준으로 내림차순 정렬
SELECT
  *
FROM
  songs
ORDER BY
  title DESC;

# 데이터 필터링: songs에서 특정 장르의 음악만 조회
SELECT
  *
FROM
  songs
WHERE
  genre = 'Pop';

# 조건부 조회: 플레이 시간 3분 이상 음악 데이터 조회
SELECT
  *
FROM
  songs
WHERE
  duration >= 180