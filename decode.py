import json

content = json.load(open('compressed.zzq'))
diction = content["dict"]
file = content["file"]

def decode(dicttion, file):
  keys = diction.keys()
  raw_aricle = ''
  tmp = ''
  for char in file:
    tmp += char 
    if tmp in keys:
      raw_aricle += diction[tmp]
      tmp = ''
  return raw_aricle

print(decode(diction, file))
