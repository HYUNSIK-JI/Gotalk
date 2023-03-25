# 프로젝트: Gotalk

## 1. 요구 사항

1) 실시간 채팅이 가능 할것
2) 채팅 내용이 db에 저장 될 것
3) 익명일때도 이전 채팅 내역을 볼 수 있을 것 (부가적인 사항)
4) 차단한 자의 메시지는 볼 수 없다.

## 2. 프로젝트 목적

1) 앱으로도 전환 (플레이스토어 등록) -> 무조건 프론트
2) Redis, 웹 소켓, 통신, 도커, 클래스 등 학습

## 3. 사용 기술

1) 우선 DJango template 으로 진행 -> 리액트 와 연동
2) Docker
3) Django
4) WebSocket
5) MySQL
6) Redis

## 4. ERD


## 5. 개발 이슈
1. nginx 설정 이후 socket 연결 끊김 (2023-03-21) -> 원인 : CORS, 문제 해결: nginx 설정 CORS 설정 추가
2. 
3.
4.
5.
6.

## 6.구조도
![image](https://user-images.githubusercontent.com/59475851/226532602-435d4077-d8f0-4a77-965a-23c561fc77e3.png)
