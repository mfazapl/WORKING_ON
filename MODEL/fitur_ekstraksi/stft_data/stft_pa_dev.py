import os
import matplotlib.pyplot as plt
import librosa

data=r"E:\pa_dev_dataset_wav"
output_file=r"E:\stft"


if not os.path.isdir(output_file):
    os.path.join(output_file)

list_audio=os.listdir(data)
for filename in list_audio:
    audio_path= os.path.join(data, filename)

    if audio_path.endswith('.wav'):
        y, sr=librosa.load(audio_path, duration=4)
        chroma_stft= librosa.feature.chroma_stft(y=y, sr=sr)
        plt.figure(figsize=(10,4))
        librosa.display.specshow(chroma_stft, y_axis='chroma', x_axis='time', sr=sr)
        plt.colorbar()
        plt.title(f'Chroma STFT - {filename}')
        plt.tight_layout()

        output_path=os.path.join(output_file, f"{os.path.splitext(filename)[0]}.png")
        plt.savefig(output_path)
        plt.close()

        print(f"gambar disimpan: {output_path}")
