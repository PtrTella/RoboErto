from naoqi import ALProxy
import os
import sys
import time

def play_music(music_name, music_dur, ip, port):
    
    music_path = os.path.join(os.getcwd(), "Music", music_name)

    try:
        # Create proxy to ALAudioPlayer
        audioPlayerProxy = ALProxy("ALAudioPlayer", ip, port)

        # Play the file
        fileID = audioPlayerProxy.post.playFile(music_path, 0.5, 1.0)

        time.sleep(music_dur)

        audioPlayerProxy.stopAll()

    except Exception, e:
        sys.exit()


if __name__ == "__main__":
    robot_ip = "127.0.0.1"
    robot_port = 9559
    music_dur = 120
    song = "CreazyInLove.wav"

    print(len(sys.argv))
    if len(sys.argv) > 1:
        song = sys.argv[1]
    elif len(sys.argv) > 2:
        music_dur = int(sys.argv[2])
    elif len(sys.argv) > 3:
        robot_ip = sys.argv[3]
    elif len(sys.argv) > 4:
        robot_port = int(sys.argv[4])

    play_music(music_name=song, music_dur=music_dur, ip=robot_ip, port=robot_port)