import requests
import sys
import hashlib
from nanoid import generate, resources

def get_text_checksum(text):
    return hashlib.md5(text.encode()).hexdigest()

if(len(sys.argv)==3):
    ip = sys.argv[1]
    port = sys.argv[2]
    response = requests.get(f'http://{ip}:{port}')
    original_checksum = response.headers['checksum']
    file_content = response.text
    if original_checksum==get_text_checksum(file_content):
        filename = generate()
        f = open(f'clientdata/{filename}', 'a')
        f.write(str(file_content))
        f.close()
        print(f'Success! File {filename} was created')
        print('Checksum is correct!')
    else:
        print('Checksum is wrong!')

    