<h1 align="center" style="font-size: 3rem;">
tiktok-api
</h1>
<p align="center">
<em>TikTok Web Api and Bot.</em></p>
<p>
<h2>Install with pip:</h2><p>

pip install tiktok-api
<p>

## Quickstart
```python
from tiktokapi import api

api = api.Api()

videos = api.get_user_videos("maskofshiva")

x = 1
for video in videos:
    print(video)
    video_urls = api.get_video_url(video)
    print(video_urls)
    try:
        api.download_user_video(video_urls, str(x))
    except Exception as e:
        print(e)
    print(api.get_meta_title(video))
    print(api.get_likes_count(video), "likes")
    print(api.get_comment_count(video), "comments")
    x += 1

```
<p>
<h2>Endpoints</h2><p>
api.get_user_videos(username)<p>
api.get_video_url(video)<p>
api.get_comment_count(video)<p>
api.get_likes_count(video)<p>
api.get_comment_count(video)<p>
api.download_user_video(video_url)<p>
