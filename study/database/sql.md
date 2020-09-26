# SQL

## Command

### DDL: Data Definition Language

- `CREATE`, `DROP`, `ALTER`, `RENAME`, `TRUNCATE`, `COMMENT`

### DML: Data Manipulation Language

- `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `MERGE`, `CALL`, `EXPLAIN PLAN`, `LOCK TABLE`

### DCL: Data Control Language

- `GRANT`, `REVOKE`

### TCL: Transaction Control Language

- `COMMIT`, `ROLLBACK`, `SAVEPOINT`



## Basic use of commands

### SELECT

```SQL
SELECT column1, column2 FROM datatable;
SELECT DISTINCT * FROM datatable;
SELECT * FROM datatable WHERE column1 > 10 OR NOT(column2 > 10);
SELECT * FROM datatable WHERE column1 LIKE "pytho%";
SELECT * FROM datatable WHERE column1 IN ("python", "java", "c");
SELECT column1 "Alias1", column2 "Alias2" FROM datatable;
```



DESC 테이블명; 테의블 정의 보기

SELECT

SELECT * FROM 테이블명 WHERE 필드='조건' AND 필드2='조건2'
SELECT 필드1, 필드2, 필드3 FROM 테이블명
SELECT * FROM TAB; 존재하는 모든 테이블 보기
SELECT DISTINCT 필드1 FROM 테이블명; 중복제거하기
SELECT 필드1 FROM 테이블 WHERE 필드2 BETWEEN 00 AND 00; //00부터 00사이에서
SELECT 필드1 FROM 테이블 WHERE 필드2 IN (00, 00); //00과 00중에서
SELECT 필드1 FROM 테이블 WHERE 필드2 LIKE '%단어%';
SELECT 필드1 FROM 테이블 WHERE 필드2 IS NULL; or NoT IS NULL


UPDATE

UPDATE 테이블명 SET 필드='값', 필드2='값', 필드3='값' WHERE 필드 LIKE '조건'

INSERT

INSERT INTO 테이블명(필드1, 필드2) VALUES ('값', '값' );

비교연산자 : >, >=, <, <=, =, <>(not equal)

DROP TABLE 테이블명;

CREATE TABLE 테이블명 (
   필드명 타입 조건,
   id varchar2(15) primary key,
   pass varchar(15) not null,
   no number(5)
)

시퀀스 생성 : CREATE SEQUENCE 시퀀스이름
          increment by 1
          start with 1
          nomaxvalue
          nocycle
          nocache;

외래키 생성 : ALTER TABLE 테이블명 ADD ( FOREIGN KEY (필드) REFERENCES 테이블명2);

칼럼 수정 : ALTER TABLE 테이블명 MODIFY (필드 타입);

컬럼 추가 : ALTER TABLE 테이블명 ADD ( 필드이름 필드타입 );

칼럼 리네임 : ALTER TABLE 테이블명 RENAME COLUMN 컬럼이름 TO 새이름;

Null값 처리하기 : SELECT isNULL(필드, '0') FROM 테이블

방금 인서트한 자동증가값 ID 가져오기 : SELECT @@IDENTITY (현재 세션에서만 사용가능)
현재 테이블의 가장큰 큰큰값 가져오기 : SELECT IDENT_CURRENT('테이블명')
수행된 SQL문에 의해 영향받은 행의 수 : SELECT @@ROWCOUNT

날짜 계산하기 : SELECT * FROM 테이블명 WHERE DATEADD(DAY, CONVERT(INT, 컬럼명), 날짜컬럼) > getdate()

테이블 정보보기 : EXEC sp_help 테이블
컬럼 정보보기 : EXEC sp_columns 테이블

앨리어스 사용 : SELECT 필드 AS A FROM 테이블 (별칭에 특수문자 있으면 [] 사용]

주석 : -- or /* */

변수의 선언 : DECLARE @변수명 자료형, @변수명 자료형
변수 할당 : SET @변수명 = 값
변수값 가져오기 : SELECT @변수명

일부분만 가져오기 : SELETC TOP 5 컬럼 FROM 테이블

범위정하기 SELECT 컬럼 FROM 테이블 WHERE 컬럼 BETWEEN 10 AND 20
        SELECT 컬럼 FROM 테이블 WHERE 컬럼 IN ('aaa', 'bbb', 'ccc')

패턴매칭 : SELECT 컬럼 FROM 테이블 WHERE 컬럼 LIKE '%제목%"
        _ : 어떤것이든 한 문자
        % : 없거나 아무 글자오거나
        [] : []안에 있는 글자들 - [b-f]
        [^] : ^다름에 있는 글자를 제외한 다른 것

중복제거 : SELECT DISTINCT 컬럼 FROM 테이블

GROUP BY : SELECT 컬럼1, sum(컬럼2) FROM 테이블 WHERE 조건 GROUP BY 컬럼1 HAVING sum(컬럼2) >= 30
(계산함수가 반드시 있어야 한다, GROUP BY ALL을 사용하면 WHERE제외된것 도 포함)

이너조인 : SELECT 컬럼 FROM 테이블 INNER JOIN 테이블 ON 컬럼=컬럼
아웃터조인 : SELECT 컬럼 FROM 테이블 LEFT OUTER JOIN 테이블 ON 컬럼=컬럼
         (어느한쪽의 데이터를 모두 가져온다.)

IN : SELECT 컬럼 FROM 테이블 WHERE 컬럼2 IN ( SELECT 컬럼2 FROM 테이블 )
   (IN안의 하위질의는 DISTINCT가 붙은 것으로 동작)
EXISTS : SELECT 컬럼1 FROM 테이블 WHERE EXISTS ( SELECT * FROM 테이블 WHERE 조건 )
       (EXISTS는 하위쿼리가 어떤 결과라도 돌려지면 참)

임시테이블 만들기 : SELECT INTO SELECT * INTO 새테이블명 FROM 테이블 (다른세션에서도 가능, DROP해야 삭제됨)
              SELECT INTO SELECT * INTO #새테이블명 FROM 테이블 (해당세션에서만 가능, 세션끊어지면 삭제됨)
              SELECT INTO SELECT * INTO ##새테이블명 FROM 테이블 (다른세션에서도 가능, 세션끊어지면 삭제됨)

UNION : SELECT 컬럼1, 컬럼2 FROM 테이블
      UNION
      SELECT 컬럼1, 컬럼2 FROM 테이블
      (UNION은 컬럼의 자료형과 순서가 맞아야 한다. 중복데이터는 제거되며 UNION ALL을 하면 중복데이터도 가져온다.)

컬럼 추가 : ALTER TABLE 테이블명 ADD 새컬럼 VARCHAR(10) NULL
컬럼 변경 : ALTER TABLE 테이블명 ALTER COLUMN 컬럼 VARCHAR(10) NULL
컬럼 삭제 : ALTER TABLE 테이블병 DROP COLUMN 컬럼

삭제 : DELETE FROM 테이블명 WHERE 조건

업데이트 : UPDATE 테이블 SET 컬럼 = 값 WHRER 조건

트랜잭션 : BEGIN TRAN
        ROLLBACK
        COMMIT




덧) SELECT에 왠만하면 * 는 사용하지 않는다.

덧) WHERE절에서 연산자의 왼쪽은 가동하지 않는다. 컬럼을 가공하면 색인을 사용할 수 없다.
    WHERE 컬럼 * 3 < 10 말고 WHERE 컬럼 < 10 / 3 을 사용하자





select A.ID as PLACE_ID, A.NAME, count(*) from PLACES as A left outer join PLACES_REVIEWS as B group by A.ID order by A.ID