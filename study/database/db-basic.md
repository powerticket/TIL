# Database

체계화된 데이터의 모임으로, 여러 사람이 공유하고 사용할 목적으로 통합 관리되는 정보들이다.



## 특성

- 데이터 중복 최소화

- 데이터 무결성

- 데이터 일관성

- 데이터 독립성

- 데이터 표준화

- 데이터 보안 유지



## Schema

데이터베이스에서 자료의 구조, 표현방법, 관계 등을 정의한 구조

| Column | datatype |
| ------ | -------- |
| id     | INT      |
| age    | INT      |
| phone  | TEXT     |
| email  | TEXT     |



### Table

데이터 열과 레코드(행)의 집합

| id   | name | age  | phone         | email     |
| ---- | ---- | ---- | ------------- | --------- |
| 1    | kim  | 31   | 010-1234-5678 | a@abc.com |
| 2    | park | 43   | 010-8765-4321 | b@bcd.com |



## SQL

> Structured Query Language

관계형 데이터베이스 관리시스템(RDBMS)의 데이터를 관리하기 위해 설계된 특수 목적의 프로그래밍 언어이다.



### DDL

> Data Definition Language

- `CREATE`: Table 생성
- `DROP`: Table 삭제
- `ALTER`: Table 변경



### DML

> Data Manipulation Language

- `INSERT`: 데이터 저장

- `UPDATE`: 데이터 수정

- `DELETE`: 데이터 삭제

- `SELETCT`: 데이터 조회



### DCL

> Data Control Language

- `GRANT`
- `REVOKE`
- `COMMIT`
- `ROLLBACK`



## [SQLite](https://www.sqlite.org/)

### Installation

#### Download

##### Precompiled Binaries for Windows

64-bit DLL (x64) for SQLite version 3.33.0.

A bundle of command-line tools for managing SQLite database files, including the [command-line shell](https://www.sqlite.org/cli.html) program, the [sqldiff.exe](https://www.sqlite.org/sqldiff.html) program, and the [sqlite3_analyzer.exe](https://www.sqlite.org/sqlanalyze.html) program.



#### Settings

sqlite 폴더를 생성하여 다운받아 압축을 푼 파일을 전부 넣고, `C:\sqlite`로 이동

환경 변수 `Path`에 `C:\sqlite`를 추가

cmd에서 `sqlite3` 또는 git bash에서 `winpty sqlite3`로 실행 확인



### Command

#### DB 파일 생성 및 샘플 조회

db_name으로 된 sqlite3 파일을 생성하고 조작한다.

```bash
$ sqlite3 db_name.sqlite3
```



csv 파일을 examples로 추가하고 모든 행을 조회한다.

```sqlite
sqlite> .mode csv
sqlite> .import sample.csv examples
sqlite> SELECT * FROM examples;
sqlite> .headers on
sqlite> SELECT * FROM examples;
sqlite> .mode column
sqlite> SELECT * FROM examples;
```



#### `CREATE`: Table 생성

```sqlite
sqlite> CREATE TABLE classmates (
   ...> id INTEGER PRIMARY KEY,
   ...> name TEXT
   ...> );
sqlite> .tables
sqlite> .schema classmates
```



#### `DROP`: Table 삭제

```sqlite
sqlite> DROP TABLE classmates;
sqlite> .tables
```



#### `ALTER`: Table 변경

```sqlite
sqlite> ALTER TABLE articles RENAME TO news;
sqlite> ALTER TABLE news
   ...> ADD COLUMN created_at TEXT NOT NULL DEFAULT 1;
```



#### `INSERT`: Data 추가

```sqlite
sqlite> INSERT INTO classmates (name, age)
   ...> VALUES ('홍길동', 23);
sqlite> SELECT * FROM classmates;
sqlite> INSERT INTO classmates (name, age, address)
   ...> VALUES ('홍길동', 30, '서울');
sqlite> SELECT * FROM classmates;
sqlite> INSERT INTO classmates
   ...> VALUES ('홍길동', 31, '부산');
sqlite> SELECT * FROM classmates;
sqlite> INSERT INTO classmates
   ...> VALUES ('홍길동', 30, '서울'), ('김철수', 23, '대전');
sqlite> SELECT * FROM classmates;
sqlite> SELECT rowid, * FROM classmates;
```

```sqlite
sqlite> CREATE TABLE classmates (
   ...> id INTEGER PRIMARY KEY,
   ...> name TEXT NOT NULL,
   ...> age INT NOT NULL,
   ...> address TEXT NOT NULL
   ...> );
sqlite> INSERT INTO classmates
   ...> VALUES (1, '홍길동', 31, '부산');
sqlite> INSERT INTO classmates (name, age, address)
   ...> VALUES ('홍길동', 23, '서울');
sqlite> SELECT * FROM classmates;
```



#### `SELECT`: Data 조회

```sqlite
sqlite> SELECT * FROM classmates;
sqlite> SELECT rowid, * FROM classmates;
sqlite> SELECT name, age FROM classmates;
sqlite> SELECT rowid, name FROM classmates LIMIT 2;
sqlite> SELECT rowid, name FROM classmates LIMIT 1 OFFSET 2;
sqlite> SELECT rowid, name FROM classmates WHERE address='서울';
sqlite> SELECT DISTINCT age FROM classmates;
```



#### `DELETE`: Data 삭제

```sqlite
sqlite> DELETE FROM classmates WHERE rowid=4;
sqlite> SELECT * FROM classmates;
```



#### `UPDATE`: Data 수정

```sqlite
sqlite> UPDATE classmates SET name='홍길동', address='제주도'
   ...> WHERE rowid=4;
sqlite> SELECT rowid, * FROM classmates;
```



### Etc Function

```sqlite
sqlite> SELECT COUNT(*) FROM users;
sqlite> SELECT AVG(age) FROM users;
sqlite> SELECT first_name, MAX(balance) FROM users;
```



#### LIKE(wild cards)

- `_`: 반드시 한 자리의 문자가 있어야 한다.
- `%`: 있을 수도 있고, 없을 수도 있다.

| 사용 예시    | 의미                           |
| ------------ | ------------------------------ |
| 2%           | 2로 시작하는 값                |
| %2           | 2로 끝나는 값                  |
| %2%          | 2가 들어가는 값                |
| _2%          | 두번 째가 2로 시작하는 값      |
| 1___         | 1로 시작하고 4자리인 값        |
| 2\_%\_%/2__% | 2로 시작하고 적어도 3자리인 값 |

```sqlite
sqlite> SELECT * FROM users WHERE age LIKE '2_';
sqlite> SELECT * FROM users WHERE
   ...> phone LIKE '02-%'
sqlite> SELECT * FROM users WHERE first_name LIKE '_준';
```



#### ORDER BY

```sqlite
sqlite> SELECT * FROM users ORDER BY age;
```

##### Option

- `ACS`: 오름차순(기본값)
- `DESC`: 내림차순



#### GROUP BY

```sqlite
sqlite> SELECT last_name, COUNT(*)
   ...> FROM users
   ...> GROUP BY last_name;
```





## 참고

[https://www.sqlitetutorial.net/](https://www.sqlitetutorial.net/)