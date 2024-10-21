import os
import subprocess

input_file= r"C:\Users\ASUS\Downloads\DATASET\PA\ASVspoof2019_PA_eval\flac"
output_file=r"E:\pa_eval_dataset_wav"

if not os.path.exists(output_file):
    os.makedirs(output_file)

for filename in os.listdir(input_file):
    if filename.endswith('.flac'):
        input_path= os.path.join(input_file, filename)
        output_path= os.path.join(output_file, filename.replace('.flac','.wav'))
        subprocess.run(["ffmpeg", "-i", input_path, output_path])

print('Konversi Selesai!')