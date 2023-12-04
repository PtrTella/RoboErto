import os
import glob
import random
import subprocess
import multiprocessing
import sys
import coreography

import numpy as np
import scipy.io.wavfile as wav



def songpl(song, dur, ip, port):
    print("Play song!")
    python2_command= f"python2 music_play.py {song} {dur} {ip} {port}"
    subprocess.run(python2_command.split(), stdout=subprocess.PIPE)

def dance(moves, robot_ip, robot_port):
    print("Dance!")
    path = os.path.join(os.getcwd(), f"NaoMoves{os.path.sep}")
    for move in moves:
        python2_command= f"python2 {path}{move.name}.py {robot_ip} {robot_port}"
        print("Move: {}".format(move.name), flush=True)
        subprocess.run(python2_command.split(), stdout=subprocess.PIPE)


# Analyze the selected song and plot the amplitudes in order to show how the intensity change into the song.
# The function returns the list of intensity per second of the song
def analyze_music(song):
    # Read the song
    rate, audData = wav.read(os.getcwd() + "/Music" + "/" + song)
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



def main():
    robot_ip = input("Insert Robot IP: ") or "127.0.0.1"
    print(robot_ip)
    robot_port = input("Insert Robot Port: ") or "9559"
    print(robot_port)

    list_songs = []
    print("AVAILABLE SONGS:")
    for index, file in enumerate(glob.glob("*.wav", root_dir=(os.getcwd() + "/Music"))):
        list_songs.append(file)
        print(index, ":", file)

    song = list_songs[int(input("\n Which song would you like to play? Choose the number: ") or random.randint(0, len(list_songs)-1))]
    dur= int(input("\n Set the duration of the choreography (in seconds): ") or 120)

    print("\n You chose the song || " + song + " || NAO will dance for:  ", dur, " seconds!")

    # Select a random song and analyze the amplitude
    analyzed_song = analyze_music(song)
    
    # Let's dance
    moves = coreography.search_coreography(analyzed_song, dur)
    
    process1 = multiprocessing.Process(target=songpl, args=(song, dur, robot_ip, robot_port))
    process2 = multiprocessing.Process(target=dance, args=(moves , robot_ip, robot_port))
    process1.start()
    process2.start()
    process2.join()
    process1.terminate()
    process2.terminate()

    try:
        sys.stdout.close()
    except:
        pass

    try:
        sys.stderr.close()
    except:
        pass


if __name__ == '__main__':
    main()
