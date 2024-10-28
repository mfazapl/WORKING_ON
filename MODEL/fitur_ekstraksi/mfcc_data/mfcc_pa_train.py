import os
import librosa
import librosa.display
import matplotlib.pyplot as plt

data=r'E:\la_dev_dataset_wav'
output_data=r'E:\data_fitur_ekstraksi\mfcc\mfcc_la_dev'

if not os.path.isdir(output_data):
    os.path.makedirs(output_data)

list_data= os.listdir(data)

for filename in list_data:
    input_path= os.path.join(data, filename)
    
    if input_path.endswith('.wav'):
        y, sr= librosa.load(input_path, duration=5)
        mfcc= librosa.feature.mfcc(y=y, sr=sr)

        plt.figure(figsize=(10, 4))
        librosa.display.specshow(mfcc, x_axis='time', sr=sr)
        plt.colobar(format='%+2.0f dB')
        plt.title(f'MFCC - {filename}')
        plt.tight_layout()

        output_path= os.path.join(output_data, f'{os.path.splitext(filename)[0]}.png')
        plt.savefig(output_path)

        plt.close()

        print(f'Gambar berhasil disimpan {output_path}')