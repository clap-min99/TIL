# users 테이블의 모든 데이터 조회
SELECT
  *
FROM
  users;

# age가 18세 미만인 유저의 목록 조회
SELECT
  *
FROM
  users
WHERE
  age < 18;

# age가 18세 미만인 유저의 age와 phone 필드 조회
SELECT
  age, phone
FROM
  users
WHERE
  age < 18;