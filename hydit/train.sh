export HOST_GPU_NUM=8
# 当前机器ip
#export LOCAL_IP=${ip1}
# 多节点机器ip，逗号隔开
#export NODE_IP_LIST="${ip1}:8,${ip2}:8"
# 机器节点个数
export NODES=1
export NODE_NUM=$((${NODES} * ${HOST_GPU_NUM}))

#export NCCL_DEBUG=WARN
# export TF_CPP_MIN_LOG_LEVEL=3
export DS_ACCELERATOR=musa
export LOGLEVEL="INFO"
export MUSA_EXECUTION_TIMEOUT=20000000
export MUSA_VISIBLE_DEVICES="0,1,2,3,4,5,6,7"
export MUSA_KERNEL_TIMEOUT=3200000
export MCCL_PROTOS=2
export MCCL_CHECK_POINTERS=0
export OMP_NUM_THREADS=4
export MCCL_ALGOS=1
# export MUDNN_LOG_LEVEL=INFO

export MCCL_BUFFSIZE=20971520
export MUSA_BLOCK_SCHEDULE_MODE=1
export MCCL_IB_GID_INDEX=3
export MCCL_NET_SHARED_BUFFERS=0
export MCCL_IB_TC=122
export MCCL_IB_QPS_PER_CONNECTION=16
export MUSA_LAUNCH_BLOCKING=0
export DS_BUILD_OPS=0
export DS_SKIP_CUDA_CHECK=1
export HF_ENDPOINT=https://hf-mirror.com
export WANDB_MODE=disabled

CURRENT_DIR=$(pwd)
PARRENT_DIR=$(dirname "$PWD")
export PYTHONPATH=${PARRENT_DIR}:${PYTHONPATH}


task_flag="dit_g2_full_1024p"                                 # the task flag is used to identify folders.
#resume_module_root=./ckpts/t2i/model/pytorch_model_distill.pt # checkpoint root for model resume
#resume_ema_root=./ckpts/t2i/model/pytorch_model_ema.pt      # checkpoint root for ema resume
resume_module_root=/data/caizhi/ckpts/t2i/model/pytorch_model_module.pt # checkpoint root for model resume
resume_ema_root=/data/caizhi/ckpts/t2i/model/pytorch_model_ema.pt      # checkpoint root for ema resume
index_file=/data/caizhi/dataset/porcelain/jsons/porcelain.json             # index file for dataloader
results_dir=./log_EXP                                         # save root for results
batch_size=1                                                  # training batch size
image_size=1024                                               # training image resolution
grad_accu_steps=1                                             # gradient accumulation
warmup_num_steps=0                                            # warm-up steps
lr=0.0001                                                     # learning rate
ckpt_every=9999999                                            # create a ckpt every a few steps.
ckpt_latest_every=9999999                                     # create a ckpt named `latest.pt` every a few steps.
ckpt_every_n_epoch=2                                          # create a ckpt every a few epochs.
epochs=8                                                      # total training epochs


sh $(dirname "$0")/run_g.sh \
    --task-flag ${task_flag} \
    --noise-schedule scaled_linear --beta-start 0.00085 --beta-end 0.018 \
    --predict-type v_prediction \
    --uncond-p 0 \
    --uncond-p-t5 0 \
    --index-file ${index_file} \
    --random-flip \
    --lr ${lr} \
    --batch-size ${batch_size} \
    --image-size ${image_size} \
    --global-seed 999 \
    --grad-accu-steps ${grad_accu_steps} \
    --warmup-num-steps ${warmup_num_steps} \
    --use-fp16 \
    --extra-fp16 \
    --results-dir ${results_dir} \
    --resume \
    --resume-module-root ${resume_module_root} \
    --resume-ema-root ${resume_ema_root} \
    --epochs ${epochs} \
    --ckpt-every ${ckpt_every} \
    --ckpt-latest-every ${ckpt_latest_every} \
    --ckpt-every-n-epoch ${ckpt_every_n_epoch} \
    --log-every 10 \
    --use-zero-stage 2 \
    --deepspeed \
    --gradient-checkpointing \
    --cpu-offloading \
    "$@"
    #--use-flash-attn \
