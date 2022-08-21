#!/bin/bash

if [ "$#" -ne 8 ]
then
  echo "Usage: ./run.sh [input_file] [num_thread] [tag] [hashSize] [which_dense] [lr] [alpha] [threshold]"
  exit 0
fi

input_file=$1
num_thread=$2

tag=$3

hashSize=$4
which_dense=$5
lr=$6
alpha=$7

threshold=$8

./03_clustering/coarse $input_file $num_thread > 03_clustering/coarse_out_${tag}
./03_clustering/fine $input_file $num_thread < 03_clustering/coarse_out_${tag} > 03_clustering/fine_out_${tag}

./04_training/dataset $input_file $tag < 03_clustering/fine_out_${tag}
cluster=$(find . -name "cluster_${tag}_*")
cluster_info="${cluster:2}"
python 04_training/train_baseline.py ${cluster_info}
model_name="model_${tag}_4096_2048_1e-05.torchsave"
python3 04_training/train_hashlayer_gh.py model/${model_name} ${cluster_info} ${hashSize} ${which_dense} ${lr} ${alpha}
hash_name="model_hash_${tag}_${hashSize}_4096_2048_${which_dense}_${lr}.torchsave"
python3 04_training/model_converter_gh.py model/${hash_name}

script_module="${hash_name}.pt"
./05_infer/DeepSketch ${input_file} model/${script_module} ${threshold}

python run_call.py
