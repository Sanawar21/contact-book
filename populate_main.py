from time import sleep
from cryptography.fernet import Fernet

text = 'hello iam sanawar'
# fernet = Fernet(Fernet.generate_key())
# enc = fernet.encrypt(text.encode())
# dec = fernet.decrypt(enc).decode()


# print(f'{type(enc) = }')
# print(f'{type(dec) = }')

fernet = Fernet(Fernet.generate_key())

def dencrypt(data, key):
  fernet = Fernet(key)
  if isinstance(data, str):
    return fernet.encrypt(data.encode())
  elif isinstance(data, bytes):
    return fernet.decrypt(data).decode()
  else:
    data = str(data)
    return fernet.encrypt(data.encode())

text = 'ali@#$%$#*&^0321223212\n'\
        'papa@#$%$#*&^032123123\n'\
        'mama@#$%$#*&^012312223123\n'\
        'mamu@#$%$#*&^04124134134\n'\
        'muhammad sanawar@#$%$#*&^03150220748\n'
texts = text.split('\n')
key = fernet.generate_key()


def read(key):
  with open('data2.txt', 'r') as file:
    lines = file.readlines()
    new_lines = []
    for line in lines:
      line = line.encode()
      new = dencrypt(line, key)
      new_lines.append(new)
    return new_lines

def write(data: list, key):
  with open('data2.txt', 'w') as file:
    for line in data: file.write((dencrypt(line, key).encode())+'\n')

# write(texts, key)
print(read(key))
# print(type(fernet.generate_key()))
# print(b'line'.decode())