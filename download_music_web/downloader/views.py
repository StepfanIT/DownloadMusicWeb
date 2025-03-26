import os
import yt_dlp
from django.shortcuts import render, redirect
from django.http import FileResponse
from django import forms

os.makedirs("downloads", exist_ok=True)

class URLForm(forms.Form):
    url = forms.URLField(label='YouTube Link', required=True)

def index(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            file_path = download_audio(url)
            if not file_path:
                return render(request, 'index.html', {'form': form, 'error': "Не вдалося завантажити"})
            return redirect(f'/download/{os.path.basename(file_path)}')
    else:
        form = URLForm()
    return render(request, 'index.html', {'form': form})

def download_audio(url):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': 'downloads/%(title)s.%(ext)s',
            'noplaylist': True
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            return ydl.prepare_filename(info)
    except Exception as e:
        print(f"Помилка: {e}")
        return None

def download(request, filename):
    file_path = os.path.join("downloads", filename)
    return FileResponse(open(file_path, 'rb'), as_attachment=True)
