# 간단한 네트워크 패킷 스니퍼

from scapy.all import sniff, IP, TCP, ICMP
# import lib.mymodule
import lib.mymodule2

# 패킷이 캡쳐될때마다 호출되는 함수
# 여기서 패킷의 헤더 정보를 꺼내봄
def process_packet(packet):

    # 1. IP 레이어가 있는지 확인
    # 네트워크에는 IP가 없는 패킷도 존재할 수 있음 - 주의 요망!
    if packet.haslayer(IP):

        # IP 헤더에서 출발지/도착지 IP 주소 추출 (프로토콜 번호도 함께)
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        proto_num = packet[IP].proto   # TCP:6, UDP:17

        # print(ip_src, ip_dst, proto_num)

        # 2. TCP 레이어가 있는지 확인
        if packet.haslayer(TCP):

            # TCP 헤더에서 출발지/도착지 포트번호 추출
            port_src = packet[TCP].sport
            port_dst = packet[TCP].dport

            #print(port_src, port_dst, proto_num)
            print(f"=============================")
            print(f"[TCP 패킷 감지!!]")
            print(f"누가   - {ip_src}:{port_src}")
            print(f"어디로  - {ip_dst}:{port_dst}")
            print(f"[TCP 패킷 감지!!]")
            print(f"=============================\n")

        else:
            # IP 패킷이지만 TCP패킷이 아닌 경우 (UDP, ICMP등)
            print(f"[기타 IP패킷] {ip_src} -> {ip_dst} ({proto_num})")

        if ICMP in packet:
            print(f"Ping이 감지되었습니다!!")

# 메인 실행 부분 - 프로그램의 시작점(실행 진입점)
# 현재 파이썬 파일은 직접 호출했을때만 실행되게 하고
# import 했을때는 자동으로 실행되지 않게 하기 위한 코드
if __name__ == "__main__":
    print(">>> 패킷 감시를 시작합니다... (중지는 Ctrl + C)")

    # sniff  : 패킷을 낚아채는 함수
    # filter : 낚아챌 패킷 지정
    # prn    : 패킷을 잡을때마다 호출할 함수 지정
    # store  : 잡은 패킷을 메모리에 저장하지 않음 (메모리 부족 방지)
    #sniff(filter="ip", prn=process_packet, store=0)
    sniff(prn=process_packet, store=0)