# Docker

Docker는 리눅스의 응용 프로그램들을 소프트웨어 컨테이너(시스템의 모든 프로세스와 격리된 하나의 프로세스) 안에 배치시키는 일을 자동화하는 오픈 소스 프로젝트이다.



## Command

docker <command> -<option> <image>



### `docker run <image-name>`

도커 파일을 실행한다. 이미지가 없을 경우 자동 pull 후에 실행한다.

#### Option

##### `-d`

백그라운드에서 컨테이너를 실행한다.

##### `-p <host-port>:<container-port>`

호스트와 컨테이너의 포트를 매핑한다.

##### `-it`

컨테이너가 지속적으로 상호작용하는 터미널 환경을 실행한다.

##### `-v`

볼륨을 마운트한다.



### `docker build <option> <Dockfile-path>`

해당 폴더 내의 Dockerfile을 읽고 어플리케이션을 빌드한다.

#### Dockerifle

```dockerfile
FROM node:12-alpine
WORKDIR /app
COPY . .
RUN yarn install --production
CMD ["node", "src/index.js"]
```

#### Option

##### `-t <image-name>`

빌드하는 이미지의 이름을 태그한다.



### `docker ps <option>`

컨테이너 리스트를 보여준다.

#### Option

##### `-a`

실행중이지 않은 컨테이너를 포함한 모든 컨테이너 리스트를 보여준다.



### `docker stop <container-id>`

실행중인 컨테이너를 중지시킨다.



### `docker rm <option> <container-id>`

컨테이너를 제거한다.

#### Option

##### `-f`

실행중인 컨테이너도 강제로 제거한다.



### `docker tag <local-image-name> <dockerhub-id/repo-name:tagname>`

docker image의 tag를 추가한다.



### `docker push <dockerhub-id/repo:tagname>`

docker hub에 이미지를 업로드한다.



### `docker exec <container-id> <command>`

해당 컨테이너 환경 안에서 커맨드를 실행한다.



### `docker volume <option>`

도커의 볼륨을 관리하는 명령어이다.

#### Option

##### `create <volume-name>`