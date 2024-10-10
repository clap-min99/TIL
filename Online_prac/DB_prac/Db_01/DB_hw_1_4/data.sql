
# name의 값에 love글자를 포함한 데이터 조회
SELECT
  *
FROM
  tracks
WHERE
  Name LIKE '%love%';

# genreID의 값이 1이고, Milliseconds값이 300000이상인 데이터를 모두 조회하여 unitprice기준으로 내림차순 정렬
SELECT
  *
FROM
  tracks
WHERE
  GenreID = 1 AND Milliseconds >= 300000 
ORDER BY
  UnitPrice DESC;

# GenreID 별로 그룹화하여 GenreID와 각 그룹별 데이터 수 조회
# 단 그룹별 데이터 수는 TotalTracks 필드로 표기하여 나타내기
SELECT
  GenreID, COUNT(*) AS TotalTracks
FROM
  tracks
GROUP BY
  GenreId;

# GenreID 별로 그룹화하여 GenreID와 각 그룹별 UnitPrice의 총합을 계산하여 조회
# UnitPrice의 총 합을 계산하여 조회
SELECT 
  GenreID, SUM(UnitPrice) AS TotalPrice
FROM
  tracks
GROUP BY
  GenreId
HAVING
  TotalPrice >= 100;