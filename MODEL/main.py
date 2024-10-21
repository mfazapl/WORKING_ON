import streamlit as st
import pandas as pd
import matplotlib as mp
import numpy as np
from st_audiorec import st_audiorec

def recorded_audio():
    st.title('Voice Spoofing Detection')
    wav_audio_data = st_audiorec()
    if wav_audio_data is not None:
        col_playback , col_space = st.columns([0.58, 0.42])
        with col_playback:
             st.audio(wav_audio_data, format='audio/wav')

if __name__ == '__main__':
    recorded_audio()
