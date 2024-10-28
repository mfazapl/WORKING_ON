import os
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np

data=r'E:\la_dev_dataset_wav'
output_data=r'E:\data_fitur_ekstraksi\poly_features\poly_features_la_dev'

if not os.path.isdir(output_data):
    os.makedirs(output_data)

list_data=os.listdir(data)

for filename in list_data:
    input_path=os.path.join(data, filename)

    if input_path.endswith('.wav'):
        y, sr= librosa.load(input_path, duration=5)
        S= np.abs(librosa.stft(y))**2

        poly_features=librosa.feature.poly_features(S, sr=sr, order=2)

        plt.figure(figsize=(10, 4))
        librosa.display.specshow(poly_features, x_axis='time', sr=sr)
        plt.colorbar()
        plt.title(f'Polynomial Features - {filename}')
        plt.tight_layout()

        output_path= os.path.join(output_data, f'{os.path.splitext(filename)}')
        plt.savefig(output_path)

        plt.close()

        print(f'Gambar berhasil disimpan: {output_path}')

