import simpleaudio
if __name__ == '__main__':
    wav_obj = simpleaudio.WaveObject.from_wave_file("maga_mitsuki_BGM.wav")
    play_obj = wav_obj.play()
    play_obj.wait_done()