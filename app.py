import threading


# 定義22個資源, 將各代表一種肉品
resources = {
    'beef': [0] * 10,
    'pork': [0] * 7,
    'chicken': [0] * 5
}

# 定義5個互斥鎖, 將各代表一位員工
locks = [threading.Lock() for _ in range(5)]

# 定義一個函數來分配資源
def modify_resource(resource_type, resource_index):
    
    lock_index = resource_index % 5
    lock = locks[lock_index]
      
    # 獲取互斥鎖
    lock.acquire()

    # 進行資源挪動
    resources[resource_type][resource_index] += 1
    
    # 釋放互斥鎖
    lock.release()

# 創建多個執行緒來挪動共享資源
threads = []
for i in range(10):  # 牛肉 共享資源
    thread = threading.Thread(target=modify_resource, args=('beef', i))
    threads.append(thread)

for i in range(7):  # 豬肉 共享資源
    thread = threading.Thread(target=modify_resource, args=('pork', i))
    threads.append(thread)

for i in range(5):  # 雞肉 共享資源
    thread = threading.Thread(target=modify_resource, args=('chicken', i))
    threads.append(thread)

# 先建立執行緒，以開始動作
for thread in threads:
    thread.start()

# 等待所有執行緒完成
for thread in threads:
    thread.join()

print("All threads have finished.")
