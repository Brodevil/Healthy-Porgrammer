import datetime
import time
from pygame import mixer


print("\n\t\t\t\tWelcome to our 'Health Programmer' Program\n\n")

presenet_time = datetime.datetime.now()
day_time = presenet_time.strftime('%H:%M:%S')
date = presenet_time.strftime('%D')
print(f"Todays Date is {date}, & Now Exactly time is {day_time},"
      f" \nAnd You start to work sir, I will remind you as per the time\n\n")


def play_on_loop(file, stop_sen, sentence):
    """

    :param file: its take the file name for playing music
    :param stop_sen: from this sencenten the music will stop
    :param sentence: This senctence will be prinked while input
    :return: this is fro all the contidion to playsound
    """
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        stop = input(sentence)
        if stop == stop_sen:
            mixer.music.stop()
            break
        else:
            print("Please Check your speeling\n")


def log_file(msg):
    """
    This function is to store the works of your activities
    :param msg: write in the file
    :return:
    """
    with open("mylogs.txt", "a") as f:
        f.write(f"{msg} : {datetime.datetime.now()}\n")


if __name__ == '__main__':
    water_time = time.time()
    eye_time = time.time()
    physical_time = time.time()
    water_zone = 20*60
    eye_zone = 30*60
    physical_zone = 40*60

    while True:
        if time.time() - water_time >= water_zone:
            play_on_loop("\nwater.mp3", "Drank", "Its time to drink water, Drank it and type 'Drank' to stop music\n")
            water_time = time.time()
            log_file("Abhinav Drank water at")
        if time.time() - eye_time >= eye_zone:
            play_on_loop("\nEyes.mp3", "Eydone", "Its time to do eyes Exercise , do it and type 'Eydone' to stop "
                                                 "music\n")
            eye_time = time.time()
            log_file("Abhinav's eyes relaxed at ")
        if time.time() - physical_time >= physical_zone:
            play_on_loop("\nphysical.mp3", "Exdone", "Its time to do exercise, do it and type 'Exdone' to stop music\n")
            physical_time = time.time()
            log_file("Abhinav done the exercise at")
