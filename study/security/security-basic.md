# Security

| Hacker  | Name                                                         |
| ------- | ------------------------------------------------------------ |
| Legal   | White-hat, Bug-bounty                                        |
| Illegal | Black-hat, Cyber-gang, Hacktivist                            |
| Middle  | Cyber-mercenaries, Script-kiddies, Grey-hat, Nationalist-hacker |



## Session Hijacking

​	Django 로그인 기능을 구현하면서 비연결성(Connectionsless), 무상태(Stateless)라는 특성을 가진 HTTP 프로토콜에서 로그인 상태를 유지하기 위한 도구인 Cookie와 Session에 대해서 배웠다. 로그인을 하면 서버에서 Session ID를 만들어 DB와 사용자의 Cookie에 저장하여 해당 사용자가 로그인 중임을 확인하는 것인데, 다른 유저의 브라우저에서 Session ID를 알아내게 되면 해당 인원의 권한으로 로그인을 할 수 있기에 보안상 문제가 있을 것 같다고 생각했다.

​	실제로 구글링 해본 결과, 해당 방식을 통해 시스템에 접근하는 Session Hijacking이라는 공격이 있었다.  Session hijacking이란 시스템에 접근할 수 있는 권한을 가진 Session을 가로채서 시스템의 자원이나 데이터를 사용하는 공격이다.



### Prevention

해당 공격을 막기 위한 방법에는 여러 가지가 있는데 Django에서 이미 지원하는 기능도 아닌 기능도 있다. 지원하는 기능은 Check 표시를 해두었다.

- [x] 긴 난수를 사용한 Session ID 생성
- [ ] 로그인 후 Session ID 재생성
- [ ] 사용자의 IP 주소, 접속 위치 등을 통한 2차 확인
- [ ] 매 요청마다 쿠키값 변경
- [ ] 웹 사이트 종료 시 자동 로그 아웃

