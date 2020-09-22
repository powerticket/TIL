# Docker

Docker는 리눅스의 응용 프로그램들을 소프트웨어 컨테이너 안에 배치시키는 일을 자동화하는 오픈 소스 프로젝트이다.



## Command

### `docker images`

Docker의 이미지 리스트를 확인한다.



### `docker rm container_name`

특정 container를 삭제한다.

#### Option

`-f`: 강제 삭제



### `docker rmi container_name`

특정 image를 삭제한다.

#### Option

`-f`: 강제 삭제



### `docker ps`

container 리스트 확인

#### Option

`-a`: 모든 container를 보여준다.(기본값은 현재 실행중인 container만 보여준다.)

