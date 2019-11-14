import json

class node():
  def __init__(self, value, left, right, name=''):
    self.value = value
    self.left = left
    self.right = right
    self.name = name

  def is_leaf(self):
    if self.left or self.right:
      return False
    return True

def tree(frequency):
  frequency = frequency[::-1]
  encode = {}
  root = ''
  for _, char in frequency[:-1]:
    encode[char] = root + '0'
    root += '1'
  encode[frequency[-1][1]] = root
  return encode

def value(n):
  if type(n) is node:
    return n.value
  return n[0]

def build_tree(frequency):
  '''
  最优编码数
  '''
  frequency = frequency[::-1]
  for _ in range(len(frequency)-1):
    left = frequency.pop()
    right = frequency.pop()
    left_value = value(left)
    right_value = value(right)
    tree_node = node(left_value+right_value, left, right, '')
    frequency.append(tree_node)
    frequency = sorted(frequency, key=value)[::-1]
  return frequency[0]

def search(tree, encode, strings):
  if type(tree) == tuple:
    encode[tree[1]] = strings
    return encode

  encode = search(tree.left, encode, strings+'0')
  encode = search(tree.right, encode, strings+'1')

  return encode

def huffman(frequency):
  tree = build_tree(frequency)
  encode = search(tree, {}, '')
  return encode

def check_compressed(raw_encode, new_encode, strings):
  raw = ''
  new = ''
  for char in strings:
    raw += raw_encode[char]
    new += new_encode[char]
  print(f"字符串原始编码长度：{len(raw)}")
  print(f"字符串压缩编码长度：{len(new)}")
  print(f"压缩比例为：{len(new)/len(raw)}")
  return new

def get_frequency(string):
  frequency = {}
  for char in string:
    if char in frequency.keys():
      frequency[char] += 1
    else:
      frequency[char] = 1
  frequency = [ (frequency[key], key) for key in frequency.keys()]
  frequency = sorted(frequency)
  return frequency

if __name__ == '__main__':
  file = 'raw.txt'
  raw_string = open(file).read()
  raw_encode = huffman(get_frequency(''.join([chr(i) for i in range(128)])))

  frequency = get_frequency(raw_string)

  encode = huffman(frequency)
  compressed = check_compressed(raw_encode, encode, raw_string)
  decode = {encode[key]: key for key in encode.keys()}
  json.dump({"dict":decode, "file":compressed}, open('compressed.zzq', 'w'))
  