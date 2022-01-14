from flask import Flask, send_file
from nanoid import generate
import sys
import hashlib
KILO_BYTE = 1024
def save_generated_str():
    data = generate(size=KILO_BYTE)
    filename = generate()
    full_path = f'serverdata/{filename}'

    f = open(full_path, 'a')
    f.write(data)
    f.close()
    return full_path

def get_checksum(filename):
    return hashlib.md5(filename).hexdigest()

app = Flask(__name__)

@app.route('/')
def index():
    file_path = save_generated_str()
    checksum = get_checksum(open(file_path, 'rb').read())
    response = send_file(file_path)
    response.headers['checksum'] = checksum
    return response

if __name__ == '__main__':
    if(len(sys.argv)==2):
        port = sys.argv[1]
        print(sys.argv[1])
    else:
        port = 5000
    app.run(host='0.0.0.0', port=port)
