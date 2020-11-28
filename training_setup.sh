#!/bin/sh

cd Tensorflow/models/research/object_detection
python3 setup.py build
python3 setup.py install

pip3 install pillow lxml Cython contextlib2 jupyter matplotlib pandas opencv-python tf_slim pycocotools lvis

export PYTHONPATH=/home/leonsick/Tensorflow/models

echo "Configuration complete. Start training with: python3 model_main.py --logtostderr -train_dir=training/ --pipeline_config_path=training/ssd_mobilenet_v2_quantized_300x300_coco.config"