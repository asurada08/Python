import psutil

curr_sent = 0
curr_recv = 0

prev_sent = 0
prev_recv = 0

# 1초에 1번씩 반복해 cpu 사용량, 사용 가능한 메모리, n/w 사용량 출력
while True:
    cpu_p = psutil.cpu_percent(interval=1)  # 1초 동안
    print(f'cpu 사용량 : {cpu_p}%')

    memory = psutil.virtual_memory()
    memory_avail = round(memory.available / 1024**3, 1)  # 사용가능한 메모리
    print(f'사용 가능한 메모리 ; {memory_avail}GB')

    net = psutil.net_io_counters()  # 네트워크 전송, 수신 크기
    curr_sent = net.bytes_sent / 1024**2
    curr_recv = net.bytes_recv / 1024**2

    sent = round(curr_sent-prev_sent, 1)  # 현재 측정 값-이전 측정한 값을 빼면 1초 동안 보내는 데이터 구해짐
    recv = round(curr_recv-prev_recv, 1)  # 받는 데이터 구하기

    print(f'보내기 : {sent}MB / 받기 : {recv}MB')

    prev_sent = curr_sent  # 이전 값에 현재 값을 저장, 이전 값이 있어야 1초 동안 얼마 만큼 전송 하고, 수신 하는지 계산할 수 있음
    prev_recv = curr_recv
