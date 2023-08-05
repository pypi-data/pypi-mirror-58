#!/usr/bin/env python3

from urllib.request import urlopen
from urllib.error import HTTPError
from time import sleep

from pirc522 import RFID

def loop(host, player_id):
  rdr = RFID()

  old_playlist_name = None
  while True:
    rdr.wait_for_tag()
    (error, tag_type) = rdr.request()
    if not error:
      (error, uid) = rdr.anticoll()
      if not error:
        playlist_name = "-".join(str(i) for i in uid)
        if playlist_name == old_playlist_name:
          print("Playlist unchanged")
          sleep(2)
          continue
        old_playlist_name = playlist_name
        print(playlist_name)
        try:
          url = "http://{}/status?p0=playlist&p1=resume&p2={}&player={}".format(host, playlist_name, player_id)
          print(url)
          f = urlopen(url)
          print(f)
        except HTTPError as e:
          if e.code != 404:
            raise e
    sleep(2)
  # Calls GPIO cleanup
  rdr.cleanup()

def main():
  import sys
  print(len(sys.argv))
  if len(sys.argv) != 3:
    print("Usage: rfid-squeezectl.py lms_host:port player_id", file=sys.stderr)
    print("Example: rfid-squeezectl.py music:9000 b8:27:eb:d0:cc:13", file=sys.stderr)
    sys.exit(1)
  else:
    loop(*sys.argv[1:])

if __name__ == "__main__":
  main()