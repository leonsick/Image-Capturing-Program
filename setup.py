import os
import argparse

#classes = args.classes
#img_classes = [img_classes + img_class + " " for img_class in classes]

os.system('pip3 install virtualenv')
os.system('python3 -m virtualenv icp-env')
os.system('source icp-env/bin/activate')
os.system('pip3 install -r requirements.txt')

os.system('bash setup_folder_structure.sh')
