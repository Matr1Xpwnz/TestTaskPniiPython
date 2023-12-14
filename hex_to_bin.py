import binascii

def hex_to_bin(input_file, output_file):
    with open(input_file, 'r') as hex_file, open(output_file, 'wb') as bin_file:
        lines = hex_file.readlines()
        for line in lines:
            if line.startswith(':'):
                hex_data = line[1:-1] if len(line) % 2 == 0 else line[1:-2]
                hex_data = '0' + hex_data if len(hex_data) % 2 != 0 else hex_data
                bin_data = binascii.unhexlify(hex_data)
                bin_string = ''.join(f"{byte:08b}" for byte in bin_data)
                bin_file.write(bin_data)
                with open("binary_output.txt", "a") as bin_output_file:
                    bin_output_file.write(bin_string + "\n")  # Запись двоичного представления в файл

if __name__ == "__main__":
    input_file = input("Введите имя входного файла : ")
    output_file = input("Введите имя выходного файла: ")
    hex_to_bin(input_file, output_file)
