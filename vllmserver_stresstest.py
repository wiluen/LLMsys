import subprocess
import time
import os

for i in range(2):  # 迭代 10 次，假设你需要执行 10 次
    print(f"Starting iteration {i + 1}")

    # 启动 a.py 作为子进程
    process = subprocess.Popen(["vllm", "serve","llm/llama/Meta-Llama-3-8B-Instruct"])

    # 模拟一些处理，在 a.py 运行的同时
    time.sleep(40)  # 假设 a.py 运行 5 秒钟后要被中断
    print('vllm ready')
    process_b = subprocess.Popen(["python", "llm/vllm_benchmark.py", "--num_requests", "200", "--concurrency", "50", "--output_tokens", "100", "--vllm_url", "http://localhost:8000/v1", "--api_key", "EMPTY"])

    # 等待 b.py 运行完成
    process_b.wait()  # 这里我们等待 b.py 执行结束后再继续

    # 再让 a.py 运行几秒
    time.sleep(3)

    # 中断 a.py 进程
    print(f"Terminating vllm in iteration {i + 1}")
    process.terminate()  # 向 a.py 发送 SIGTERM 信号，优雅结束进程

    # 如果 a.py 没有响应，可以使用 kill() 强制结束
    try:
        process.wait(timeout=3)  # 等待 3 秒钟让 a.py 退出
    except subprocess.TimeoutExpired:
        print("a.py did not exit gracefully, killing the process")
        process.kill()  # 强制结束 a.py


    print(f"Finished iteration {i + 1}\n,wait for 10s ")
    time.sleep(10)
    
