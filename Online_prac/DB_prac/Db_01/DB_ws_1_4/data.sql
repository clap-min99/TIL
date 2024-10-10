# 전체 사용자의 평균 age
SELECT
  AVG(age) as average_age
FROM
  users;

# 각 country 별 사용자 수
SELECT 
  country, COUNT(*)
FROM
  users
GROUP BY
  country;

# balance가 가장 많은 사용자의 정보 중 가장 먼저 조회되는 한 명의 정보만 조회
SELECT
  *
FROM
  users
ORDER BY
  balance DESC LIMIT 1;

# 각 country별 평균 balance
SELECT
  country, AVG(balance)
FROM
  users
GROUP BY
  country;

# balance가 가장 많은 사용자와 가장 적은 사용자의 balance 차이
SELECT
  MAX(balance)-MIN(balance) AS balance_difference
FROM 
  users
