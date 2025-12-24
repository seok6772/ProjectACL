### 우분투에서 실행하기

+ 프로젝트 디렉토리 생성
```bash
    mkdir ~/projectACL
    cd ~/projectACL
```

+ 가상환경 생성
```bash
   sudo apt update
   sudo apt install -y python3.10-venv python3-pip
   
   python3 -m venv py310b
   source py310b/bin/activate
```

+ scapy 패키지 설치

```bash
   # 관리자 영역에 패키지 설치
   sudo python3 -m pip install scapy
```

+ 메인 애플리케이션
```bash 
    sudo vi ~/projectACL/main.py
```

+ 메인 애플리케이션 실행
```bash
    # 관리자로 실행
    sudo python3 main.py
```

### 우분투에 미니콘다 설치하기
+ 우분투에 파이썬을 설치하는 것은 다소 번거로움
+ 왜냐하면 소스를 내려받아 직접 컴파일 해야 하기 때문
+ 따라서, 미니콘다 배포파일을 다운로드해서 설치하는 것을 추천

```bash
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-py311_25.11.1-1-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm ~/miniconda3/miniconda.sh
conda --version
```

```bash
# 셸 설정파일을 편집기로 열기
vi ~/.bashrc

# 맨 마지막 줄에 다음 내용 추가
export PATH="$HOME/miniconda3/bin:$PATH"

# 변경사항 시스템에 적용
source ~/.bashrc

# 콘다 버젼 확인
conda --version

# 콘다 자동 base 환경 비활성화하고 확인
conda config --set auto_activate_base false
conda config --show auto_activate
```

### conda로 가상환경 생성
```bash
# 가상환경 생성전 다음 명령 먼저 실행 (최초 한번!)
conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/main
conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/r

# 그런 다음 아래 명령으로 가상환경 생성 및 활성화
conda create -y -n py311 python=3.11
source activate py311
```

```bash
pip install --upgrade pip
pip install scapy

mkdir ~/projectACL
cd ~/projectACL

vi main.py
sudo ~/miniconda3/envs/py311/bin/python main.py
```

```bash
# py311 가상 환경에서 나가기
conda deactivate
```