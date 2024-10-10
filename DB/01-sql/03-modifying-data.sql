CREATE TABLE articles (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title VARCHAR(100) NOT NULL,
  content TEXT NOT NULL,
  created_at DATE NOT NULL
);

-- 공통
SELECT * FROM articles;
DROP TABLE articles;
PRAGMA table_info('articles');


-- 1. Insert data into table
INSERT INTO articles (title, content, created_at)
VALUES ('제목', '내용1', '2000-01-01');

INSERT INTO articles (title, content, created_at)
VALUES 
  ('제목2', '내용2', '2001-01-01'),
  ('제목3', '내용3', '2002-01-01'),
  ('제목4', '내용4', '2003-01-01');
-- 2. Update data in table

UPDATE 
  articles
SET
  title = 'update title'
WHERE id =1;

UPDATE
  articles
SET
  title = 'UPDATE TITLE',
  content = 'UPDATE CONTENT'
WHERE id
  id = 2;
-- 3. Delete data from table
DELETE FROM articles
WHERE Id = 1; 


DELETE FROM articles
WHERE
  Id IN(
    select id FROM articles
    ORDER BY created_atL
    LIMIT 2
  );
  
  INSERT INTO articles(title, content, created_at)
  VALUES 
  ('제목5', '내용5', '2004-01-01'),
  ('제목6', '내용6', '2005-01-01'),
  ('제목7', '내용7', '2006-01-01');

