import sys
import requests
import pyaudio
import wave
import keyboard
import io

'''
mp3, aac, ac3, ogg, flac, wav
'''
client_id = ""
client_secret = ""
lang = "Kor" # 언어 코드 ( Kor )
# url = "https://naveropenapi.apigw-pub.fin-ntruss.com/recog/v1/stt?lang=" + lang
url = "https://naveropenapi.apigw.ntruss.com/recog/v1/stt?lang=" + lang

# 설정
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
WAVE_OUTPUT_FILENAME = "output.wav"

# pyaudio 객체 생성
audio = pyaudio.PyAudio()

# 녹음할 준비
frames = []

def start_recording():
    global frames
    frames = []
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)
    print("Recording... Press 's' to stop.")

    while True:
        if keyboard.is_pressed('s'):
            print("Stopped recording.")
            break
        data = stream.read(CHUNK)
        frames.append(data)

    stream.stop_stream()
    stream.close()

def save_to_variable():
    buffer = io.BytesIO()
    waveFile = wave.open(buffer, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()
    buffer.seek(0)
    return buffer.getvalue()



headers = {
    "X-NCP-APIGW-API-KEY-ID": client_id,
    "X-NCP-APIGW-API-KEY": client_secret,
    "Content-Type": "application/octet-stream"
}


print("Press 'r' to start recording.")
keyboard.wait('r')  # 'r' 키 입력 대기
start_recording()   # 's' 키 입력시 녹음 중지
audio_data = save_to_variable()


response = requests.post(url,  data=audio_data, headers=headers)
rescode = response.status_code
if(rescode == 200):
    print (response.text)
else:
    print("Error : " + response.text)



# pyaudio 종료
audio.terminate()

