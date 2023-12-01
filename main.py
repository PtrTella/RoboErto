
import random
import subprocess
import multiprocessing
import coreography
import sys
import os
import music_detection as md
import glob, os



def songpl(song, dur, ip, port):
    print("Play song!")
    os.chdir('..')
    os.chdir('..')
    os.chdir(os.getcwd())
    python2_command= f"python2 -m music_play {song} {dur} {ip} {port}"
    subprocess.run(python2_command.split(), stdout=subprocess.PIPE)

def dance(moves, robot_ip, robot_port):
    print("Dance!")
    os.chdir('..')
    os.chdir('..')
    os.chdir(os.path.join(os.getcwd(), "NaoMoves"))
    
    for move in moves:
        python2_command= f"python2 -m {move.name} {robot_ip} {robot_port}"
        print("Move: {}".format(move.name), flush=True)
        subprocess.run(python2_command.split(), stdout=subprocess.PIPE)

def main():
    robot_ip = input("Insert Robot IP: ") or "127.0.0.1"
    print(robot_ip)
    robot_port = input("Insert Robot Port: ") or "9559"

    list_songs = []
    os.chdir(os.getcwd() + "/Music")
    print()
    print("AVAILABLE SONGS:")
    i=1
    for file in glob.glob("*.wav"):
        list_songs.append(file)
        print(i, ":", file)
        i+=1

    song = list_songs[int(input("\n Which song would you like to play? Choose the number: ") or random.randint(1, len(list_songs))) - 1]
    dur= int(input("\n Set the duration of the choreography (in seconds): ") or 120)
    print("\n You chose the song || " + song + " || NAO will dance for:  ", dur, " seconds!")

    # --------------------------------------------------------------# ADDED
    # Select a random song and analyze the amplitude
    analyzed_song = md.analyze_music(song)
    # --------------------------------------------------------------# ADDED
    moves = coreography.search_coreography(analyzed_song, dur)
    process1 = multiprocessing.Process(target=songpl, args=(song, dur, robot_ip, robot_port))
    process2 = multiprocessing.Process(target=dance, args=(moves , robot_ip, robot_port))
    process1.start()
    process2.start()
    process2.join()
    process1.terminate()




if __name__ == '__main__':
    main()
