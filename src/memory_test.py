import os 
import time 
 
print("PID:", os.getpid(), flush=True) 
 
data = [] 
 
for i in range(5): 
    # Выделяем блок 10 МиБ 
    block = bytearray(10 * 1024 * 1024) 
 
    # Записываем по одному байту в каждую страницу (4096 байт), 
    # чтобы страницы действительно попали в RAM 
    for j in range(0, len(block), 4096): 
        block[j] = 1 
 
    data.append(block) 
    print(f"Выделено {(i + 1) * 10} МиБ", flush=True) 
    time.sleep(5) 
 
print("Ожидание 20 секунд...", flush=True) 
time.sleep(20) 
