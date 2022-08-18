python 04_training/train_baseline.py [dataset]
=>model_tag_4096_2048_1e-05.torchsave 형식으로 파일 생성됨

python 04_training/train_hashlayer_gh.py [trained_model] [dataset] 128 1 0.001 0.05
=> 파일 이름에 클러스터의 수를 추가하도록 수정할 것

python 04_training/model_converter_gh.py [trained_model] [data_set]
=> 이부분에서 파일 이름으로 클러스터의 수를 받을 수 있도록 수정할 것
