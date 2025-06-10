제가 만든 코드는 연락처 관리 프로그램입니다.
이 프로그램은 사용자가 터미널에서 간편하게 연락처를 추가, 검색, 수정, 삭제, 목록 확인을 할 수 있는 파이썬 기반 연락처 관리 소프트 웨어 입니다.
주요 기능으로는
1. 연락처 추가 : 이름과 전화번호를 입력해 연락처를 저장합니다.
2. 연락처 수정 : 기존 이름을 찾아 이름/전화번호 수정합니다.
3. 연락처 삭제 : 이름을 입력해 해당 연락처 삭제합니다.
4. 연락처 목록 : 저장된 모든 연락처 목록을 출력합니다.
5. 연락처 검색 : 이름을 입력하면 검색이 가능합니다.
<실행 방법>
1. 프로젝트 전체를 다운로드 합니다.
2. Python 3.x가 설치되어 있는지 확인합니다.
- [Python 공식 사이트](https://www.python.org/downloads/)에서 Python 설치
- Windows에서는 `chcp 65001`로 터미널 인코딩을 UTF-8로 바꿔야 한글이 정상 출력됨
- VSCode 사용 시, `settings.json`에 아래 코드 추가:
{
    "workbench.iconTheme": "material-icon-theme",
    "python.defaultInterpreterPath": "C:\\Users\\사용자이름파일\\anaconda3\\python.exe",
    "files.exclude": {
        "**/.git": false
    },
    "git.autofetch": true,

    "terminal.integrated.profiles.windows": {
      "Command Prompt": {
        "path": [
          "${env:windir}\\Sysnative\\cmd.exe",
          "${env:windir}\\System32\\cmd.exe"
        ],
        "args": ["/K", "chcp 65001"]
      }
    },
    "terminal.integrated.defaultProfile.windows": "Command Prompt"
}

3. 실행을 했을 때 OUTPUT말고 터미널로 이동합니다.
4. 한글이 깨진다면 터미널에 chcp 65001 를 입력합니다.(한글 안깨진다면 바로 5번으로 이동합니다.)
5. 입력 후 python project.py를 입력하고 실행하면 프로그램이 실행이 됩니다.
