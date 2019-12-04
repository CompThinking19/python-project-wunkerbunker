import simpleaudio as sa

print('Using one word, type how you are feeling')
x = input()
if x == "happy":
#Cmaj
    filename = 'happy.wav'
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()
if x == "sad":
#Cmin
    filename = 'sad.wav'
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()
if x == "angry":
#Cdim7
    filename = 'angry.wav'
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()
if x == "surprised":
#CminMaj7
    filename = 'surprised.wav'
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()
if x == "triumphant":
#E/Dmaj9
    filename = 'triumphant.wav'
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()
if x == "melancholy":
#BMaj13
    filename = 'melancholy.wav'
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()
if x == "romantic":
#Cmaj7
    filename = 'romantic.wav'
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()
if x == "optimistic":
#C9
    filename = 'optimistic.wav'
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()
if x == "seinfeld":
#C9
    filename = 'seinfeld.wav'
    wave_obj = sa.WaveObject.from_wave_file(filename)
    play_obj = wave_obj.play()
    play_obj.wait_done()
