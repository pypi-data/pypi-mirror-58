import sys
import os
import re
import argparse

def has_ext(filename, ext):
  """
  >>> has_ext('test.mp3',['opus','mp3','aac'])
  True
  >>> has_ext('test.mp4',['opus','mp3','aac'])
  False
  >>> has_ext('test.opus.gz',['opus','mp3','aac'])
  False
  >>> has_ext('test.1.OPUS',['opus','mp3','aac'])
  True
  """

  return filename.split('.')[-1].lower() in ext

def is_audio(f): return has_ext(f, ['opus','mp3','aac','m4a','ogg'])
def is_video(f): return has_ext(f, ['mp4','avi','mov','mkv'])
def is_image(f): return has_ext(f, ['png','jpeg','jpg'])
def is_media(f): return is_audio(f) or is_video(f) or is_image()

def normalize(filename):
  """
  >>> normalize('Test 1.txt')
  'test-1.txt'
  >>> normalize('another-TEst_file.mp4')
  'another-test-file.mp4'
  >>> normalize('Linkin Park - In the End -.opus')
  'linkin-park-in-the-end.opus'
  >>> normalize('calvin&hobbes.pdf')
  'calvin-hobbes.pdf'
  >>> normalize('2019-10-11 07.08.09[family photo].jpg')
  '2019-10-11T070809-family-photo.jpg'
  >>> normalize('2010-01-12 03.04.05 some nature.jpg')
  '2010-01-12T030405-some-nature.jpg'
  >>> normalize('2010-01-12T030405-some-nature.jpg')
  '2010-01-12T030405-some-nature.jpg'
  """
  
  path = filename.split('/')[:-1]
  filename = filename.split('/')[-1]

  filename = filename.lower().replace('_','-').replace(' ','-').replace('–','-')

  d = re.search(
    "^"
    "(?P<year>\d{4})[\-]?"
    "(?P<month>\d{2})[\-]?"
    "(?P<day>\d{2})[Tt \-]?"
    "(?P<hour>\d{2})[\.\:\- ]?"
    "(?P<minute>\d{2})[\.\:\- ]?"
    "(?P<second>\d{2})[\.\:\- ]?",
    filename)

  if d:
      filename = filename.replace(d.group(0),
        f"{d['year']}-{d['month']}-{d['day']}T{d['hour']}{d['minute']}{d['second']}-")

  if is_audio(filename):
    filename = re.sub(r'[\(\[].*?[\)\]]','', filename) # Remove parentheticals

  filename = re.sub('[\[\(\)\]\-\&]+','-', filename)
  words = filename.split('-')

  filename = '-'.join(words)

  filename = re.sub(r'[\'\!\:\,]','', filename)

  filename = re.sub(r'-+\.+','.', filename)

  filename = re.sub(r'\-+','-', filename)

  return '/'.join(path + [filename])

def main():
    ap = argparse.ArgumentParser(description='Rename files to a standard format')
    ap.add_argument('files', nargs='+', help="List of files")
    args = ap.parse_args()

    for filename in args.files:
        os.rename(filename, normalize(filename))    
