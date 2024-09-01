cuda 12.4  python3.11
pip install vllm
pip install modelscope
export VLLM_USE_MODELSCOPE=True
vllm serve qwen/Qwen2-0.5B-Instruct
