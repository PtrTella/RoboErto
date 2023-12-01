# Import utilities

import pydub
import os 
import scipy.io.wavfile
import numpy as np 


# Analyze the selected song and plot the amplitudes in order to show how the intensity change into the song.
# The function returns the list of intensity per second of the song

def analyze_music(song):
    wav = pydub.AudioSegment.from_wav(os.getcwd() + "/" + song)
    wav_mono = wav.set_channels(1)
    os.chdir(os.getcwd() + "/Music_Mono")
    wav_mono.export(os.getcwd() + "/" + "_MONO_" + song[:-3] + "wav", format="wav")
    rate, audData = scipy.io.wavfile.read(os.getcwd() + "/" + "_MONO_" + song[:-3] + "wav")


    duration = len(audData) / float(rate)

    # INTENSITY ANALYSIS
    list_interval_intensity = []
    for i in range(int(duration)):
        list_interval_intensity.append((np.sum(abs(audData[i*rate:((i+1)*rate)+1]).astype(float)))/rate)
    max_interval = max(list_interval_intensity)
    list_interval_intensity_percent = []

    for el in list_interval_intensity:
        list_interval_intensity_percent.append((el*100)/max_interval)

    print("Intensity analysis completed!")
    
    return list_interval_intensity_percent


