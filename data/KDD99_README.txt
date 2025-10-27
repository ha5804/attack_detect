📘 README — KDD Cup 1999 Dataset 요약

1️⃣ 데이터셋 개요

KDD Cup 1999 데이터셋은 네트워크 침입 탐지 시스템(NIDS) 연구를 위해 만들어진 대표적인 공개 데이터셋입니다.
DARPA Intrusion Detection Evaluation 프로그램에서 수집된 네트워크 트래픽 로그를 기반으로,
각 연결(connection)을 41개의 특징(feature)과 하나의 라벨(label)로 구성하였습니다.

총 Feature 수: 41개

Attack Type (목표 변수): DoS, Probe, R2L, U2R의 4개 대분류로 구성

------------------------------------------------------------
2️⃣ Feature 설명 (총 41개)

🧩 기본 연결 정보 (Basic Features)
1. duration — 연결이 지속된 시간(초 단위)
2. protocol_type — 사용된 프로토콜 종류 (예: tcp, udp, icmp)
3. service — 서비스 타입 (예: http, telnet, ftp 등)
4. flag — 연결의 상태를 나타내는 플래그 값 (예: SF, REJ 등)
5. src_bytes — 원본(Source)에서 목적지(Destination)로 보낸 바이트 수
6. dst_bytes — 목적지에서 원본으로 보낸 바이트 수
7. land — 연결의 출발지와 목적지가 같은 경우(0: 아니오, 1: 예)
8. wrong_fragment — 잘못된(fragmented) 패킷 조각의 개수
9. urgent — 긴급(urgent) 패킷의 개수

⚙️ 내용 기반 특징 (Content Features) — 패킷 내용 분석
10. hot — 시스템 호출 등 의심스러운 행동의 횟수
11. num_failed_logins — 로그인 실패 횟수
12. logged_in — 성공적으로 로그인했는지 여부 (0: 아니오, 1: 예)
13. num_compromised — 시스템 손상(compromise) 관련 횟수
14. root_shell — root shell을 획득한 여부 (0: 아니오, 1: 예)
15. su_attempted — 'su root' 명령 시도 여부
16. num_root — root 권한 명령 실행 횟수
17. num_file_creations — 파일 생성 관련 명령 실행 횟수
18. num_shells — 쉘 명령 실행 횟수
19. num_access_files — 접근(access) 관련 파일 참조 횟수
20. num_outbound_cmds — 외부로 나가는 FTP 명령 횟수 (항상 0으로 알려짐)
21. is_host_login — 호스트 기반 로그인 여부
22. is_guest_login — guest 계정 로그인 여부

📊 트래픽 기반 통계 (Traffic Features)

(A) 최근 2초 내 동일 호스트 기준
23. count — 같은 목적지(host)로의 최근 연결 횟수
24. srv_count — 같은 서비스로의 최근 연결 횟수
25. serror_rate — SYN 에러 발생 비율
26. srv_serror_rate — 같은 서비스 내 SYN 에러 비율
27. rerror_rate — REJ 에러 발생 비율
28. srv_rerror_rate — 같은 서비스 내 REJ 에러 비율
29. same_srv_rate — 동일 서비스 비율
30. diff_srv_rate — 다른 서비스로의 연결 비율
31. srv_diff_host_rate — 같은 서비스로의 다른 호스트 연결 비율

(B) 최근 100개의 연결 중 동일 호스트 기준
32. dst_host_count — 동일 목적지 호스트로의 최근 연결 횟수
33. dst_host_srv_count — 동일 목적지+서비스 조합으로의 연결 횟수
34. dst_host_same_srv_rate — 동일 서비스 비율
35. dst_host_diff_srv_rate — 다른 서비스 비율
36. dst_host_same_src_port_rate — 동일 출발 포트를 사용하는 연결 비율
37. dst_host_srv_diff_host_rate — 동일 서비스로 다른 호스트에 연결된 비율
38. dst_host_serror_rate — 동일 호스트에 대한 SYN 에러 비율
39. dst_host_srv_serror_rate — 동일 호스트+서비스의 SYN 에러 비율
40. dst_host_rerror_rate — 동일 호스트에 대한 REJ 에러 비율
41. dst_host_srv_rerror_rate — 동일 호스트+서비스의 REJ 에러 비율

------------------------------------------------------------
3️⃣ Label (목표 변수)

각 데이터는 normal 혹은 공격 유형 중 하나로 라벨링되어 있습니다.
원본 KDD99 데이터셋에서의 공격 유형은 총 22개이며, 우리의 training set에서는 다음과 같은 4개 그룹으로 구분됩니다.

대분류				예시 공격명				설명
DoS (Denial of Service)		smurf, neptune, back, teardrop	서비스 거부 공격
Probe (Scanning)			ipsweep, portsweep, satan		포트/호스트 스캔 공격
R2L (Remote to Local)		guess_passwd, ftp_write, imap	외부 사용자가 로컬 접근 시도
U2R (User to Root)		buffer_overflow, rootkit, perl		일반 사용자가 root 권한 탈취 시도

