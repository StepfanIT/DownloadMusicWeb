import os
import json
import tempfile
import yt_dlp
from django.http import JsonResponse, FileResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.shortcuts import render

ffmpeg_path = r"D:\ffmpeg-master-latest-win64-gpl-shared\bin"
os.environ["PATH"] += os.pathsep + ffmpeg_path

def index(request):
    return render(request, 'index.html')

@require_POST
@csrf_exempt
def download(request):
    try:
        data = json.loads(request.body)
        url = data.get('url')
        quality = data.get('quality')

        if not url or not quality:
            return JsonResponse({'error': 'Недостатньо даних'}, status=400)

        file_path = handle_download(url, quality)
        return FileResponse(open(file_path, 'rb'), as_attachment=True, filename=os.path.basename(file_path))
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def handle_download(url, quality):
    quality_map = {
        'high': '320',
        'medium': '192',
        'low': '128'
    }

    bitrate = quality_map.get(quality, '192')

    temp_dir = tempfile.mkdtemp()
    output_path = os.path.join(temp_dir, 'track.%(ext)s')

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_path,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': bitrate,
        }],
        'quiet': True,
        'noplaylist': True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    mp3_file = [f for f in os.listdir(temp_dir) if f.endswith('.mp3')][0]
    return os.path.join(temp_dir, mp3_file)
