import psutil

cpu = psutil.cpu_freq()
cpu_current_ghz = round(cpu.current / 1000, 2)  # 현재 cpu 속도
print(f'cpu 속도 : {cpu_current_ghz}GHz')

cpu_core = psutil.cpu_count(logical=False)
print(f'코어 : {cpu_core}개')

memory = psutil.virtual_memory()
memory_total = round(memory.total / 1024**3)
print(f'메모리 : {memory_total}GB')

disk = psutil.disk_partitions()
for p in disk:  # 디스크 크기 출력, 디스크 수 찾는 수 만큼 출력
    print(p.mountpoint, p.fstype, end='')
    du = psutil.disk_usage(p.mountpoint)
    disk_total = round(du.total / 1024**3)
    print(f'디스크크기 : {disk_total}GB')

# 네트워크를 통해 보내고 받은 데이터를 크기를 MB
# 단위로 출력, 전송, 수신 데이터는 누적 데이터 값 출력
net = psutil.net_io_counters()
sent = round(net.bytes_sent / 1024**2, 1)
recv = round(net.bytes_recv / 1024**2, 1)
print(f'보내기 : {sent}MB / 받기 : {recv}MB')
