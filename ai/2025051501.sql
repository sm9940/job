desc mysql.itemtbl;
select productName, amount from mysql.productTBl;
show databases;
show table status;

CREATE TABLE itemTbl
(	id  INT  NOT NULL PRIMARY KEY,
	itemName  VARCHAR(40) NOT NULL,
	cost  INT NOT NULL,
	makeDate  DATE ,
	company  VARCHAR(50) NOT NULL,
	amount  INT NULL
);

show tables;
desc itemTbl;
desc mysql.productTbl;

SELECT  productName, cost, amount  FROM mysql.productTbl
WHERE cost >= 10 AND amount >= 15;

SELECT  productName, cost, amount  FROM mysql.productTbl
WHERE amount BETWEEN 5 AND 20;

SELECT  productName, company,  cost, amount  FROM mysql.productTbl
WHERE company IN('LG', '대우');

SELECT  productName, company,  cost, amount  FROM mysql.productTbl
WHERE company LIKE '%삼%성%';
SELECT  productName, company,  cost, amount  FROM mysql.productTbl
WHERE company LIKE '%성_'; -- 데이터가 없음 : '_' 무조건 한글자가 존재해야 함

SELECT  productName, company,  cost, amount  FROM mysql.productTbl
WHERE cost < (select cost from mysql.productTbl where productName = '컴퓨터');

-- 대우회사의 제품의 가격보다 큰 가격의 물건을 가져와라
SELECT  productName, company,  cost, amount  FROM mysql.productTbl
WHERE cost > (select cost from mysql.productTbl where company = '대우');

INSERT INTO itemTbl VALUES(0, "컴퓨터1", 8, "2021-01-01", "삼성", 0);
INSERT INTO itemTbl VALUES(1, "세탁기1", 25, "2022-09-01","LG", 30);
INSERT INTO itemTbl VALUES(2, "냉장고1", 5, "2023-02-01","대우", 22);

-- itemTbl(지점 데이터)에서 productTbl(본사 데이터)보다 수량이 같은 제품(목록)을 가져와라.
SELECT  productName, company,  cost, amount  FROM mysql.productTbl;
SELECT  itemName, company,  cost, amount  FROM itemTbl;
SELECT  itemName, company,  cost, amount  FROM itemTbl
WHERE itemTbl.amount =
ANY(
		SELECT  amount 
		FROM mysql.productTbl
        );

SELECT  itemName, company,  cost, amount  FROM itemTbl
ORDER BY amount DESC;

-- Q) 뭐가 문제일까?  위의 쿼리를 cost기준으로 DESC 했는데 
--     결과 순서가 삼성 -> 대우 -> LG 순으로 출력되었다.
SELECT  itemName, company,  cost, amount  FROM itemTbl
ORDER BY cost DESC;

desc mysql.buyTbl;

INSERT INTO mysql.buyTbl VALUES("홍길동", "냉장고", 5, 2);
INSERT INTO mysql.buyTbl VALUES("홍길동", "컴퓨터", 10, 3);
INSERT INTO mysql.buyTbl VALUES("고길동", "세탁기", 20, 1);
INSERT INTO mysql.buyTbl VALUES("고길동", "냉장고", 5, 1);
INSERT INTO mysql.buyTbl VALUES("홍길동", "세탁기", 20, 5);

SELECT  userName, prodName, price, amount  FROM mysql.productTbl;

SELECT * FROM buyTbl;
SELECT userName, SUM(amount) AS '제품총 갯수' FROM buyTbl
 GROUP BY userName;
SELECT userName, SUM(prise) 총금액 FROM buyTbl
 GROUP BY userName;


-- 테이블 컬럼 수정 추가시 (change -> add)
-- ALTER TABLE 테이블명 CHANGE  COLUMN 필드명 필드타입
ALTER TABLE mysql.buyTbl MODIFY userName VARCHAR(30);
ALTER TABLE mysql.buyTbl MODIFY prodName VARCHAR(30);
desc mysql.buyTbl;

ALTER TABLE mysql.userTbl MODIFY userName VARCHAR(30);
INSERT INTO mysql.userTbl VALUES("홍길동", 900, "활빈", "01012345678");
INSERT INTO mysql.userTbl VALUES("고길동", 2000, "쌍문", "01098765432");
SELECT * FROM mysql.userTbl;

select * from mysql.buyTbl;
desc mysql.buyTbl;
ALTER TABLE mysql.buyTbl CHANGE prise price INT;

SELECT userName, SUM(price) 총금액 FROM buyTbl
 GROUP BY userName;
 
SELECT userName, prodName, SUM(price) 총금액 FROM buyTbl
 GROUP BY userName, prodName HAVING userName LIKE '홍%';
 
SELECT * FROM mysql.buyTbl;
 
SELECT userName, prodName, SUM(price) 총금액 FROM buyTbl
 GROUP BY userName, prodName WITH ROLLUP;






-- VARCHAR, CHAR - mysql은 접두사로 전체 데이터 사이즈를 표기, 
-- (숫자)는 문자갯수를 의미하며 크기가 255바이트이내이면 접두사는 1byte이고 숫자에 포함되지 않음
-- (숫자)는 문자갯수를 의미하며 크기가 256바이트이상이면 접두사는 2byte이다.
CREATE TABLE vc (v VARCHAR(4), c CHAR(4));
INSERT INTO vc VALUES ('ab  ', 'ab  ');
INSERT INTO vc VALUES ('abcd', 'abcd');
INSERT INTO vc VALUES ('가나다라', '가나다라');
SELECT CONCAT('(', v, ')'), CONCAT('(', c, ')') FROM vc;

ALTER TABLE mysql.buyTbl CHANGE  price  prise  INT;
desc mysql.buyTbl ;
-- ---------------------------------------------------------------
ALTER TABLE vc MODIFY v VARCHAR(200);
INSERT INTO vc VALUES ('가나다라마가나다라마가나다라마가나다라마가나다라마가나다라마가나다라마가나다라마가나다라마가나다라마가나다라마가나다라마가나다라마가나다라마가나다라마가나다라마가나다라마가나다라마가나다라마가나다라마가나다라마가나다라마가나다라마가나다라마가나다라마가나다라마가나다라마가나다라마가나다라마가나다라마가나다라마가나다라마가나다라마가나다라마가나다라마가나다라마가나다라마가나다라마가나다라마가나다라마', '가나다라');
commit;

desc itemTbl; -- PK
desc mysql.productTbl; -- null
desc mysql.buyTbl; -- FK

CREATE TABLE productTbl1
(SELECT * FROM productTbl);
desc productTbl1;
select * from productTbl1;
DELETE FROM productTbl1;
-- primary key 추가하기
ALTER  TABLE  productTbl1  
    ADD  seq   INT  NOT NULL  AUTO_INCREMENT  PRIMARY KEY FIRST;
desc productTbl1;

INSERT INTO productTbl1 VALUES("컴퓨터", 10, "2021-01-01", "삼성", 17, NULL);
INSERT INTO productTbl1 VALUES("세탁기", 20, "2022-09-01","LG", 3, NULL);
INSERT INTO productTbl1 VALUES("냉장고", 5, "2023-02-01","대우", 22, NULL);

select * from productTbl;
select * from itemTbl;
INSERT INTO itemTbl VALUES(1, "컴퓨터1", 8, "2021-01-01", "삼성", 0);
INSERT INTO itemTbl VALUES(2, "세탁기1", 25, "2022-09-01","LG", 30);
INSERT INTO itemTbl VALUES(3, "냉장고1", 5, "2023-02-01","대우", 22);
INSERT INTO productTbl 
           (productName, cost, makeDate, company, amount ) 
SELECT itemName , cost, makeDate, company, amount FROM itemTbl;

SET @var4 = '반재현 화이팅'; -- Context(Session)에 세팅
SELECT @var4, itemName FROM itemTbl,sys;
select * from productTbl;
UPDATE productTbl SET productName = '고급 세탁기'  WHERE  productName = '세탁기1' ;
UPDATE productTbl SET productName = '고급 냉장고'  WHERE  productName = '냉장고1' ;
UPDATE productTbl SET productName = '고급 컴퓨터'  WHERE  productName = '컴퓨터1' ;

SELECT CAST(AVG(amount) AS SIGNED INTEGER) AS '평균 구매 개수' FROM buytbl;

SELECT CONVERT(AVG(amount), SIGNED INTEGER) AS '평균 구매 개수' FROM buytbl;

SELECT '10A' + '200';

SELECT 0 = 'MEGA2'; -- db의 =는 APP개발의 ==와 같음

SELECT IF (100>200, '참이다', '거짓이다') ;

SELECT CASE (SELECT CAST(AVG(amount) AS SIGNED INTEGER) AS '평균 구매 개수' FROM buytbl)
			WHEN 1 THEN '일'
            WHEN 5 THEN '오'
            WHEN 10 THEN '십'
            ELSE '모름'
		END AS 'CASE연습';
            
SELECT ASCII('A'), CHAR(65);
SELECT productName, BIT_LENGTH(productName) FROM productTbl ;
SELECT productName, CHAR_LENGTH(productName) FROM productTbl ;
SELECT productName, LENGTH(productName) FROM productTbl ;

SELECT CONCAT_WS('-', '2025', '5', '14');

SELECT INSERT ('ABCDEFGHI', 3, 4, '@@@@'), INSERT ('ABCDSTUXYZ', 3, 2, '@@@@');

SELECT LPAD('HELLO', 10, '_'), RPAD('HELLO', 10, '_');
SELECT LTRIM('       HELLO        '), RTRIM('       HELLO        ');
SELECT TRIM('       HELLO        '), TRIM( BOTH   'L'    FROM    '   HELLO        '); -- 'L'이 처음이나 끝에 있지 않다..
SELECT TRIM('       HELLO        '), TRIM( BOTH   'O'    FROM    '   HELLO   '); -- 'O'의 뒤에 공백문자가 있음.
SELECT TRIM('       HELLO        '), TRIM( BOTH   'O'    FROM    'HELLO');
DESC usertbl;
select * from  usertbl;
select * from  buytbl;

INSERT INTO erpdb.test VALUES(1, "홍길동", 01012345678);
select * from erpdb.test;