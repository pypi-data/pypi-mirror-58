import os
import re
import librosa
import noisereduce as nr
import numpy as np


def getX_a(audio_file, sample_rate, audio_start, depth_start, depth_end):
    # load audio data
    initial_difference = (depth_start - audio_start).total_seconds()
    duration = (depth_end - depth_start).total_seconds()
    segment_start = int(initial_difference * sample_rate)
    segment_end = int(min((initial_difference + duration) * sample_rate, len(audio_file) - 1))
    segment = audio_file[segment_start:segment_end]
    stft = np.abs(librosa.stft(segment, n_fft=512, hop_length=256, win_length=512))
    return np.mean(stft, axis=1)


def process_audio_data(audio_file, datetime_audio):
    raw_audio, sample_rate = librosa.load(audio_file)
    noisy_part = raw_audio[0:25000]
    nr_audio = nr.reduce_noise(audio_clip=raw_audio, noise_clip=noisy_part, verbose=False)
    return nr_audio, sample_rate, datetime_audio
