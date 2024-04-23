import os

def process_file(input_file, output_folder):
    with open(input_file, 'rb') as f:
        dec = f.read()

    if dec.startswith(b'UnityFS'):
        deca = dec[:0x32]
        decb = dec[0x32:0x32 + 50]
        decc = dec[0x32 + 50:]
        key = decb[1]
        decd = bytes([decb[j] ^ key for j in range(50)])
        dec = deca + decd + decc

    output_file = os.path.join(output_folder, os.path.basename(input_file)[:-3] + '.ab')
    with open(output_file, 'wb') as f:
        f.write(dec)

def process_files_in_folder(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    for filename in os.listdir(input_folder):
        if filename.endswith('.ab'):
            input_file = os.path.join(input_folder, filename)
            process_file(input_file, output_folder)

input_folder = 'bundles'  
output_folder = 'output'  
process_files_in_folder(input_folder, output_folder)
