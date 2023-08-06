<h1 align="center" style="font-size: 3rem;">
tiktok-api
</h1>
<p align="center">
<em>TikTok Web Api and Bot.</em></p>
<p>

   ![PyPI](https://img.shields.io/pypi/v/tiktok-api.svg) ![](https://img.shields.io/pypi/dm/tiktok-api.svg) 

</p></p>
<h2>Install with pip:</h2><p>

pip install tiktok-api
<p>

## Quickstart
```python
from tiktokapi import bot

tiktok = bot.Bot()
tiktok.download_user_videos("maskofshiva")

```
<p>
<h2>Endpoints</h2><p>
api.get_user_videos(username)<p>
api.get_video_url(video)<p>
api.get_comment_count(video)<p>
api.get_likes_count(video)<p>
api.get_comment_count(video)<p>
api.download_user_video(video_url)<p>
