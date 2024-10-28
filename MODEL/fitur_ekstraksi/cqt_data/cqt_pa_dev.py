import os
import librosa
import librosa.display
import matplotlib.pyplot as plt

data=r"E:\pa_dev_dataset_wav"
output_data=r"E:\data_fitur_ekstraksi\cqt\cqt_pa_dev"

if not os.path.isdir(output_data):
    os.makedirs(output_data)

list_data=os.listdir(data)
for filename in list_data:
    input_path=os.path.join(data, filename)

    if input_path.endswith('.wav'):
        y, sr=librosa.load(input_path, duration=5)
        chroma_cq= librosa.feature.chroma_cqt(y=y, sr=sr)

        plt.figure(figsize=(10,4))
        librosa.display.specshow(chroma_cq, y_axis='chroma', x_axis='time', sr=sr)
        plt.colorbar()
        plt.title(f'Chroma CQT- {filename}')
        plt.tight_layout()

        output_path=os.path.join(output_data, f"{os.path.splitext(filename)[0]}.png")
        plt.savefig(output_path)
        plt.close()

        print(f"gambar disimpan: {output_path}")