import requests
import m3u8
url = "https://vodhlsweb-vh.akamaihd.net/i/songs/46/4013546/35481194/35481194_96.mp4/master.m3u8?set-akamai-hls-revision=5&hdnts=st=1617832575~exp=1617846975~acl=/i/songs/46/4013546/35481194/35481194_96.mp4/*~hmac=d4721dcda024bfb53ece15b32bc44e48993f1179e3d1ddd5cda88ef85d60c186"

r = requests.get(url)
# print(r.text)
m3u8_master = m3u8.loads(r.text)

playlist_url = m3u8_master.data['playlists'][0]['uri']
r = requests.get(playlist_url)
playlist = m3u8.loads(r.text)
r = requests.get(playlist.data['segments'][0]['uri'])
with open ('song.ts','wb') as f :
    for segment in playlist.data['segments']:
        url = segment['uri']
        r = requests.get(url)
        f.write(r.content)
print('downloaded!')
