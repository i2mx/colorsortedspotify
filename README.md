# Color Sorted Spotify

## Table of Contents

- [About](#about)
- [Usage](#usage)

## About <a name = "about"></a>
A python script to quickly sort your spotify playlist by color.

## Usage <a name = "usage"></a>
If you want to run this install the dependencies in requirements.txt then just run main.py.

If you want to change the code to sort by some other parameter such as name length or anything else it, just change h in this of code to another parameter which can be calculated per track.

```py
urllib.request.urlretrieve(image_url, "image.jpg")

r,g,b = ColorThief("image.jpg").get_color()
h,s,v = colorsys.rgb_to_hsv(r,g,b)

insert_index = bisect.bisect(sorted_list, h)
sp.playlist_reorder_items(id, i, insert_index)
bisect.insort(sorted_list, h)
```

The code isn't very well written, it could be better if I didn't download the images to disk and I ran the processes asynchronously but it doesn't really matter because it's fast enough for spotify, and it will only take a few second and maybe one minute max. 
