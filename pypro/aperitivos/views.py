from django.shortcuts import render


def video(request, slug):
    videos = {
       'motivacao':{'titulo': 'Video Aperitivo: Motivação','vimeo_id':'331370698?h=0d1c5cc83e'},
        'instalacao-windwos':{'titulo':'Instalação Windwos', 'vimeo_id':'108059039?h=6008521d8d'},
    }
    video = videos[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})
