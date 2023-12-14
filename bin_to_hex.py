import binascii

def bin_to_hex(input_file, output_file):
    with open(input_file, 'rb') as bin_file, open(output_file, 'w') as hex_file:
        data = bin_file.read()
        hex_data = binascii.hexlify(data).decode('utf-8')
        hex_lines = [hex_data[i:i+32] for i in range(0, len(hex_data), 32)]
        for line in hex_lines:
            hex_file.write(f':{line.upper()}\n')

if __name__ == "__main__":
    input_file = input("Введите имя входного файла: ")
    output_file = input("Введите имя выходного файла : ")
    bin_to_hex(input_file, output_file)
