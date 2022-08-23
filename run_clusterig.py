if [ "$#" -ne 4 ]
then
  echo "Usage: ./run_clustering.sh [input_file] [num_thread] [tag] [message]"
  exit 0
fi

input_file=$1
num_thread=$2

tag=$3

message=$4

./03_clustering/coarse $input_file $num_thread > 03_clustering/coarse_out_${tag}
./03_clustering/fine $input_file $num_thread < 03_clustering/coarse_out_${tag} > 03_clustering/fine_out_${tag}


python message_send.py $message
