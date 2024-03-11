import threading

# 定義22個資源 
resources = [0] * 22


# 定義5個互斥鎖
locks = [threading.Lock() for _ in range(5)]

# 定義一個函數來分配資源
def modify_resource(resource_index):
    
    lock_index = resource_index % 5
    lock = locks[lock_index]
      
    # 獲取互斥鎖
    lock.acquire()

    # 進行資源挪動
    resources[resource_index] += 1
    
    # 釋放互斥鎖
    lock.release()

# 創建多個執行緒來挪動資源
threads = []
for i in range(22):  # 所有資源
    thread = threading.Thread(target=modify_resource, args=(i,))
    threads.append(thread)

# 先建立執行緒，以開始動作
for thread in threads:
    thread.start()

# 等待所有執行緒完成
for thread in threads:
    thread.join()

print("All threads have finished.")
