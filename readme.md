cuda 12.4  python3.11

pip install vllm

pip install modelscope

export VLLM_USE_MODELSCOPE=True

modelscope download --model 'qwen/Qwen2-0.5B-Instruct' --local_dir '/home/wyl/llm/qwen/Qwen2-0.5B-Instruct'
 
vllm serve qwen/Qwen2-0.5B-Instruct

