import os
import subprocess

input_folder=r"C:\Users\ASUS\Downloads\DATASET\PA\ASVspoof2019_PA_dev\flac"
output_folder=r"C:\Users\ASUS\OneDrive\Desktop\MODEL\data_model\pa_dev_dataset_wav"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.endswith('.flac'):
        input_path= os.path.join(input_folder, filename)
        output_path= os.path.join(output_folder, filename.replace('.flac','.wav'))

        subprocess.run(["ffmpeg","-i",input_path,output_path])

print('Konversi Selesai')
