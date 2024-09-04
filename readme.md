vllm的安装以及大模型的下载
cuda 12.4  python3.11

pip install vllm

pip install modelscope

export VLLM_USE_MODELSCOPE=True

modelscope download --model 'qwen/Qwen2-0.5B-Instruct' --local_dir '/home/wyl/llm/qwen/Qwen2-0.5B-Instruct'

modelscope download --model 'modelscope/Llama-2-7b-ms' --local_dir '/home/wyl/llm/llama/Llama2-7B' （chat模板有问题）

modelscope download --model 'LLM-Research/Meta-Llama-3-8B-Instruct' --local_dir '/home/wyl/llm/llama/Meta-Llama-3-8B-Instruct'
 
vllm serve qwen/Qwen2-0.5B-Instruct

## 使用docker配置一个nginx对多个vllm服务进行负载均衡
实现的效果是http://localhost:2345/v1转发到http://localhost:8100/v1和http://localhost:8101/v1的vllm server上
> docker run --name nginx-vllm-wyl -p 2345:2345 -v /home/wyl/nginx-docker/nginx.conf:/etc/nginx/nginx.conf:ro -d nginx
 
> docer stop nginx-vllm-wyl

> docer rm nginx-vllm-wyl

性能对比，吞吐和延迟变优（2vllm+nginx vs 2vllm）
"latency": {
    "average": 2.2517414530118307,
    "p50": 2.2815194129943848,
    "p95": 2.7434746980667115,
    "p99": 2.752342417240143
  },
  "tokens_per_second": {
    "average": 80.78628665792088,
    "p50": 77.74777688711912,
    "p95": 72.88945142991813,
    "p99": 72.1041806603181
  },
    "latency": {
    "average": 3.2588619311650593,
    "p50": 3.3435367345809937,
    "p95": 3.6779646635055543,
    "p99": 3.679928603172302
  },
  "tokens_per_second": {
    "average": 57.25673844837005,
    "p50": 56.136654720184424,
    "p95": 54.28792039649356,
    "p99": 51.8522781623398
  },
