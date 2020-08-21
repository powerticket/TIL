# Git

> Git은 분산형버전관리시스템(DVCS : Distributed Version Control System)이다.
>
> 소스코드의 버전 및 이력을 관리할 수 있다.

|        working dir        |        staging area        |       local repo (.git)       |    remote repo (GitHub)     |
| :-----------------------: | :------------------------: | :---------------------------: | :-------------------------: |
| 로컬 PC에서 작업하는 공간 | `add`를 통해 이동하는 공간 | `commit`을 통해 이동하는 공간 | `push`를 통해 이동하는 공간 |



## 준비하기

윈도우에서 git을 활용하기 위해서 git bash를 설치한다.

git을 활용하기 위해서 GUI 툴인 `source tree`, `github desktop` 등을 활용할 수도 있다.

초기 설치를 완료한 이후에 컴퓨터에 author 정보를 입력한다.

```bash
$ git config --global user.name {user name}
$ git config --global user.email {user email}
```



## 로컬 저장소(repository) 활용하기

### 1. 저장소 초기화

```bash
$ git init
Initialized empty Git repository in {폴더 주소}/.git/
```

- `.git` 폴더(숨김 폴더)가 생성되며, 여기에 git과 관련된 모든 정보가 저장된다.
- git bash에 `(master)`라고 표시되는데, 이는 현재 폴더가 git으로 관리되고 있다는 뜻이며, `master` branch에 있다는 뜻이다.



### 2. `add`

`working directory`, 즉 작업 공간에서 변경된 사항을 이력으로 저장하기 위해서는 반드시 `staging area`를 거쳐야 한다.

```bash
$ git add {파일 or 폴더}
$ git add markdown.md # 파일
$ git add images/     # 폴더(/가 붙으면 폴더)
$ git add . 		  # 현재 디렉토리의 모든 파일과 폴더
```

- markdown.md 파일이 폴더에 새롭게 작성되었으나, 아직 git으로 관리되지 않고, `add` 되기 전 상태

```bash
$ git status
On branch master
No commits yet
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        markdown.md
nothing added to commit but untracked files present (use "git add" to track)
```

- markdown.md 파일이 `add` 후에 staging area로 올라간 상태

```bash
$ git add .
On branch master
No commits yet
Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   markdown.md
```



### 3. `commit`

commit은 **이력을 확정짓는 명령어**로, 해당 시점의 스냅샷을 기록한다.

commit 시에는 반드시 메시지를 작성해야 하며, **메시지는 변경사항을 알 수 있도록 명확하게 작성**한다.

```bash
$ git commit -m "마크다운 정리"
[master (root-commit) 6c84015] 마크다운 정리
 1 file changed, 170 insertions(+)
 create mode 100644 markdown.md
```

commit 이후에는 아래의 명령어를 통해 지금까지 작성된 commit 이력을 확인한다.

```bash
$ git log
commit 6c840158f44a51f40c02f08d226289d899a6c904 (HEAD -> master)
Author: edujason-hphk <edujason.hphk@gmail.com>
Date:   Fri Jul 17 14:17:22 2020 +0900
    마크다운 정리

$ git log --oneline
6c84015 (HEAD -> master) 마크다운 정리
```

commit은 해시값을 바탕으로 구분된다.



## 원격 저장소(remote repository) 활용하기

원격 저장소 기능을 제공하는 다양한 서비스 중에 `GitHub`을 기준으로 설명한다.



### 0. 준비사항

- GitHub에 repository 생성



### 1. 원격 저장소 등록

```bash
$ git remote add origin {github url}
```

- 원격 저장소로 origin이라는 이름으로 github url을 등록

```bash
$ git remote -v
origin  https://github.com/powerticket/TIL.git (fetch)
origin  https://github.com/powerticket/TIL.git (push)
```

- 등록된 원격 저장소를 보기 위해서는 아래의 명령어를 활용



### 2. `push` - 원격 저장소로 업로드

```bash
$ git push -u origin master
```

- `origin`이라는 이름의 원격 저장소로 commit 기록들을 업로드
- 변경사항이 생길 때마다, `add` - `commit` - `push`를 반복한다.
- `git push -u origin master`를 통해 한번 push하면 이 후에는 `git push`로 push가 가능해진다.



### 3. `pull` - 원격 저장소로부터 불러오기

```bash
$ git clone {url}
```

- 최초 불러오기 시에는, `clone` 명령어를 통해 불러온다.

```bash
$ git pull origin master
```

- `origin`이라는 이름의 원격 저장소로부터 새로운 commit 기록들을 불러온다.



## [.gitignore](https://www.toptal.com/developers/gitignore)

OS -> IDE -> Language -> Framwork -> venv 순으로 생성

최상위폴더에 .gitignore 파일 생성

기존 Repository에 새로운 .gitignore 적용 시 아래와 같이 적용

```
$ git rm -r --cached .
$ git add .
$ git commit -m "Apply .gitignore"
$ git push
```

