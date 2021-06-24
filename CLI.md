# cli

## cli 란?

> Command Line Interface의 약자로, Command(명령어)를 활용하여 컴퓨터에게 일을 시키는 환경

- Command는 운영체제마다 프로그램마다 조금씩 다르다. macOS의 Terminal에서는 cal 명령어가 있지만 Windows Git Bash에는 없음!
- CLI의 핵심 개념은 경로(Path), 명령어(Command)

## 경로

- 파일이나 폴더의 고유한 위치를 나타내는 문자열 (주소)

- 운영체제에 따라서 다르게 표현된다.

  windows - `C:\\Users\\Document`

  macOS - `/Users/Document`

## command



### **cd**

- Change Directory
- 현재 워킹 디렉토리를 변경할 때 사용한다.
- `cd ..` 하면 부모 디렉토리로 이동 할 수 있다.
- `C:\\Users\\User\\바탕 화면` -> `C:\\Users\\User`

### **date**

```
Wed Jun 23 15:39:15     2021
```

- 지금 날짜가 나온다.
- 운영 체제마다 시간을 기록하는 방법이 다르기 때문에 실제와 약간 다를 수 있음

### **ls**

- 현재 워킹디렉토리의 폴더/파일 확인하기
- `ls -al` 을 활용하면 숨김 폴더와 자세한 정보를 알 수 있다.

### **touch**

- `touch a.txt` 형식으로 파일을 만들 수 있다.

### **mkdir**

- `mkdir 디렉토리이름` 형식으로 폴더를 만들 수 있다.
- 만약 폴더 이름(happy hacking)에 공백이 있다면? `mkdir happy hacking` 이라고 명령어를 사용하면 `happy` 와 `hacking` 2개의 폴더가 생긴다. 이를 방지하기 위해서는 따옴표를 사용해서 폴더 이름을 묶어줘야 한다. `mkdir 'happy hacking'`

### **Command 꿀팁**

- 과거 명령어 불러오기(위, 아래 방향키)
- 자동 완성(tab)
- `ctrl + a` 커서가 명령어 맨 앞으로 이동
- `ctrl + e` 커서가 명령어 맨 뒤로 이동
- `ctrl + w` 커서 앞에 단어 지워줌

