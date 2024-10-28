import os
import librosa
import numpy as np
import librosa.display
import matplotlib.pyplot as plt

##data E:\la_dev_dataset_wav

data=r'E:\la_dev_dataset_wav'
output_data=r'E:\data_fitur_ekstraksi\melspectogram\melspectogram_la_dev'

if not os.path.isdir(output_data):
    os.makedirs(output_data)

list_data=os.listdir(data)

for filename in list_data:
    input_path= os.path.join(data, filename)

    if input_path.endswith('.wav'):
        y, sr= librosa.load(input_path, duration=5)
        mel_spect= librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128, fmax=14000)

        S_dB= librosa.power_to_db(mel_spect, ref=np.max)

        plt.figure(figsize=(10, 4))
        librosa.display.specshow(S_dB, x_axis='time', y_axis='mel', sr=sr)
        plt.colorbar(format='%+2.0f dB')
        plt.title(f'Mel-Spectogram = {filename}')

        output_path= os.path.join(output_data, f"{os.path.splitext(filename)[0]}.png")
        plt.savefig(output_path)

        plt.close()

        print(f'Gambar berhasil disimpan: {output_path}')