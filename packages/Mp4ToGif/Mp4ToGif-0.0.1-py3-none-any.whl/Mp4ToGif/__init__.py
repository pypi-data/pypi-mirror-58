#Mp4ToGif - by Erlend/MasterErlend (c) 2019

from colorama import init
from colorama import Fore, Back, Style
import imageio
import os
import sys
from PIL import Image, ImageSequence

init()

def silent_GifCreator(clippath):
   OP = os.path.splitext(clippath)[0] + '.gif'
   R = imageio.get_reader(clippath)
   fps = R.get_meta_data()['fps']
   W = imageio.get_writer(OP, fps=fps)

   for image in R :
      W.append_data(image)
   W.close()

   size = 320, 240

   im = Image.open(OP)
   frames = ImageSequence.Iterator(im)

   def thumbnails(frames):
       for frame in frames:
           thumbnail = frame.copy()
           thumbnail.thumbnail(size, Image.ANTIALIAS)
           yield thumbnail

   frames = thumbnails(frames)

   # Save output
   om = next(frames) # Handle first frame separately
   om.info = im.info # Copy sequence info
   om.save(OP, save_all=True, append_images=list(frames))

def gif(ClipPath):
   slient_GifCreator(ClipPath)

try:
   clip = os.path.abspath(sys.argv[1])
   gif(clip)
except:
   pass
