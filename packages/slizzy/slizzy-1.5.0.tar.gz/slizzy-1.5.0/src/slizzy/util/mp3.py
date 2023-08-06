import requests
from hsaudiotag import mp4
from io         import BytesIO

from . import types, bytes


def fetch_info(url):
  """Get the bitrate and the duration from the mp3 header. 
  This will only work with tagless mp3 files."""
  # The first 512 bytes are sufficient for extracting the metadata:
  page = requests.get(url, headers = { "Range" : "bytes=0-512" })

  if page.status_code not in [ 200, 206 ]: # 206 = partial content
    raise requests.exceptions.HTTPError("http code " + str(page.status_code) + ".")

  with BytesIO(page.content) as bs:
    mp3 = mp4.File(bs)
    
    return types.Obj(
      duration = mp3.duration,
      bitrate  = mp3.bitrate
    )

  
def estimate_bitrate_from_size(size_in_mb, duration_in_secs) :
    # 1 byte = 8 bits; 1 Kb = 1000 bits
    return ((bytes.to_B(size_in_mb) * 8) / 1000) / duration_in_secs
