import simpleaudio
import tkinter as tk

wav_obj = simpleaudio.WaveObject.from_wave_file("maga_mitsuki_BGM.wav")
play_obj = None
flag = True

def play():
    global wav_obj, flag, play_obj
    if flag:
        play_obj = wav_obj.play()
        flag = False

    if not play_obj.is_playing():
        flag = True
        play()
    
        
def stop():
    global flag, play_obj
    if not flag:
        flag = True
        play_obj.stop()

if __name__ == '__main__':
    frame = tk.Tk()
    frame.geometry('200x100')
    frame.title('player')
    btn0 = tk.Button(frame, text='play', command=play).pack()
    btn1 = tk.Button(frame, text='stop', command=stop).pack()
    frame.mainloop()