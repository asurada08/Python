import psutil  # 컴퓨터 정보 라이브러리

cpu = psutil.cpu_freq()  # cpu 속도
print("cpu :", cpu)

cpu_core = psutil.cpu_count(logical=False)  # cpu 물리 코어 출력 수
print("cpu_core :", cpu_core)

memory = psutil.virtual_memory()  # 메모리 정보
print("memory :", memory)

disk = psutil.disk_partitions()  # 파티션 수
print("disk :", disk)

net = psutil.net_io_counters()  # 네트워크를 통해 보내고 받는 데이터량
print("net :", net)
