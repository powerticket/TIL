# Docker

Docker는 리눅스의 응용 프로그램들을 소프트웨어 컨테이너(시스템의 모든 프로세스와 격리된 하나의 프로세스) 안에 배치시키는 일을 자동화하는 오픈 소스 프로젝트이다.



## Command

docker <command> -<option> <image>



### run

도커 파일을 실행한다. 이미지가 없을 경우 자동 pull 후에 실행한다.



#### Option

##### `-d`

백그라운드에서 컨테이너를 실행한다.

##### `-p host_port:container_port`

호스트와 컨테이너의 포트를 매핑한다.