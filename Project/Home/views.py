from django.shortcuts import render
import matplotlib.pyplot as plt
# import sounddevice as sd
from scipy.fftpack import fft
from scipy.io import wavfile as wav
import numpy as np
import urllib, io, base64
from pydub import AudioSegment

def home(request):
    plt.close("all")
    if(request.method=='POST'):
        file=request.FILES['data']
        rate, data = wav.read(file)
        fft_out = fft(data)

        plt.plot(data, np.abs(fft_out))

       
        fig=plt.gcf()
        buf=io.BytesIO()
        fig.savefig(buf,format='png')
        buf.seek(0)
        string =base64.b64encode(buf.read())
        uri=urllib.parse.quote(string)
        print(uri)
        return render(request,"Home/form.html",{'data':uri})
        
    else:
        return render(request,"Home/form.html",{'data':None})