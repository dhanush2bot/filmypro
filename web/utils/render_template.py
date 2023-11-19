async def render_page(message_id):
    file_name, mime_type = await fetch_properties(message_id)
    src = urllib.parse.urljoin(URL, str(message_id))
    audio_formats = ['audio/mpeg', 'audio/mp4', 'audio/x-mpegurl', 'audio/vnd.wav']
    video_formats = ['video/mp4', 'video/avi', 'video/ogg', 'video/h264', 'video/h265', 'video/x-matroska']
    heading = ''  # Define heading here
    if mime_type.lower() in video_formats:
        async with aiofiles.open('web/template/req.html') as r:
            heading = 'Watch {}'.format(file_name)
            tag = mime_type.split('/')[0].strip()
            html = (await r.read()).replace('tag', tag) % (heading, file_name, src)
    elif mime_type.lower() in audio_formats:
        async with aiofiles.open('web/template/req.html') as r:
            heading = 'Listen {}'.format(file_name)
            tag = mime_type.split('/')[0].strip()
            html = (await r.read()).replace('tag', tag) % (heading, file_name, src)
    else:
        async with aiofiles.open('web/template/dl.html') as r:
            async with aiohttp.ClientSession() as s:
                async with s.get(src) as u:
                    file_size = get_size(u.headers.get('Content-Length'))
                    html = (await r.read()) % (heading, file_name, src, file_size)
    return html
