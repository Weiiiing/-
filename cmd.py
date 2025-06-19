import os
import subprocess

def set_environment_variables():
    os.environ["CUDA_VISIBLE_DEVICES"] = "0"

def run_training():
    command = [
        "torchrun",
        "--nproc-per-node", "1",
        "--master-port", "9990",
        "src/train.py",
        "--stage", "sft",
        "--deepspeed", "./examples/deepspeed/ds_z2_config.json",
        "--model_name_or_path", "/home/zhangwei/zzx_llamafactory/LLaMA-Factory/Xunzi-Qwen1.5-7B_chat",
        "--do_train",
        "--dataset", "idiom_train",
        "--output_dir", "./model_output/idiom",
        "--finetuning_type", "lora",
        "--lora_target", "all",
        "--template", "qwen",
        "--overwrite_cache",
        "--overwrite_output_dir",
        "--cutoff_len", "1024",
        "--per_device_train_batch_size", "8",
        "--lr_scheduler_type", "cosine",
        "--logging_steps", "10",
        "--save_steps", "2000",
        "--save_total_limit", "5",
        "--learning_rate", "1e-4",
        "--num_train_epochs", "5",
        "--plot_loss",
        "--fp16",
        "--preprocessing_num_workers", "16"
    ]


    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print(f"训练脚本执行失败: {e}")

if __name__ == "__main__":
    set_environment_variables()
    run_training()