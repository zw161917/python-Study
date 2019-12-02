import urllib.request

url = "http://car3.autoimg.cn/cardfs/brand/50/g24/M05/65/E3/autohomecar__wKgHIVrhoquAegtYAAAQquXedpE849.jpg"
resqonse = urllib.request.Request(url)
resqueser = urllib.request.urlopen(resqonse)
date = resqueser.read()
with open("qiche.png",'wb') as f:
    f.write(date)