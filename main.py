import os
import curses
import math
import subprocess
from colorama import init, Fore, Style

# Inisialisasi colorama
init(autoreset=True)

def install_dependencies():
    """Fungsi untuk menginstal dependensi yang diperlukan."""
    dependencies = ["colorama"]
    for package in dependencies:
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        except subprocess.CalledProcessError:
            print(Fore.RED + f"Gagal menginstal paket: {package}")
            sys.exit(1)

def clear_terminal():
    """Fungsi untuk membersihkan terminal."""
    # Windows
    if os.name == 'nt':
        os.system('cls')
    # Mac dan Linux
    else:
        os.system('clear')

def add(x, y):
    """Fungsi untuk menambahkan dua angka."""
    return x + y

def multiply(x, y):
    """Fungsi untuk mengalikan dua angka."""
    return x * y

def divide(x, y):
    """Fungsi untuk membagi dua angka."""
    if y == 0:
        return "Error: Division by zero is not allowed."
    else:
        return x / y

def percentage(x, y):
    """Fungsi untuk menghitung persentase x dari y."""
    return (x / y) * 100

def exponent(x, y):
    """Fungsi untuk menghitung eksponen."""
    return x ** y

def square_root(x):
    """Fungsi untuk menghitung akar kuadrat."""
    return math.sqrt(x)

def display_menu(stdscr, menu, title):
    curses.curs_set(0)
    stdscr.clear()
    stdscr.refresh()

    # Inisialisasi warna
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)  # Warna untuk pilihan terpilih
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)  # Warna untuk pilihan tidak terpilih

    current_row = 0

    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, title, curses.color_pair(2))
        
        for idx, row in enumerate(menu):
            x = 2
            y = idx + 2
            if idx == current_row:
                stdscr.addstr(y, x, row, curses.color_pair(1))
            else:
                stdscr.addstr(y, x, row, curses.color_pair(2))
        
        key = stdscr.getch()

        if key == curses.KEY_UP and current_row > 0:
            current_row -= 1
        elif key == curses.KEY_DOWN and current_row < len(menu) - 1:
            current_row += 1
        elif key == ord('\n'):
            return current_row
        
        stdscr.refresh()

def calculator():
    history = []

    def run_calculator(choice):
        clear_terminal()
        result = None
        error = None
        if choice == 0:
            print("Ini adalah menu Penjumlahan")
            try:
                num1 = float(input("Angka pertama: "))
                num2 = float(input(f"{num1} akan ditambahkan dengan: "))
                result = add(num1, num2)
                print(Fore.GREEN + f"Hasil: {num1} + {num2} = {result}")
                history.append(f"{num1} + {num2} = {result}")
            except ValueError:
                error = "Input tidak valid, mohon masukkan angka."
                print(Fore.RED + error)

        elif choice == 1:
            print("Ini adalah menu Perkalian")
            try:
                num1 = float(input("Angka pertama: "))
                num2 = float(input(f"{num1} akan dikalikan dengan: "))
                result = multiply(num1, num2)
                print(Fore.GREEN + f"Hasil: {num1} x {num2} = {result}")
                history.append(f"{num1} x {num2} = {result}")
            except ValueError:
                error = "Input tidak valid, mohon masukkan angka."
                print(Fore.RED + error)

        elif choice == 2:
            print("Ini adalah menu Pembagian")
            try:
                num1 = float(input("Angka pertama: "))
                num2 = float(input(f"{num1} akan dibagi dengan: "))
                result = divide(num1, num2)
                if isinstance(result, str):  # Jika hasil adalah pesan error
                    error = result
                    print(Fore.RED + error)
                else:
                    print(Fore.GREEN + f"Hasil: {num1} / {num2} = {result}")
                    history.append(f"{num1} / {num2} = {result}")
            except ValueError:
                error = "Input tidak valid, mohon masukkan angka."
                print(Fore.RED + error)

        elif choice == 3:
            print("Ini adalah menu Persentase")
            try:
                num1 = float(input("Angka pertama: "))
                num2 = float(input(f"{num1} adalah persentase dari: "))
                result = percentage(num1, num2)
                print(Fore.GREEN + f"Hasil: {num1} adalah {result}% dari {num2}")
                history.append(f"{num1} adalah {result}% dari {num2}")
            except ValueError:
                error = "Input tidak valid, mohon masukkan angka."
                print(Fore.RED + error)

        elif choice == 4:
            print("Ini adalah menu Eksponen")
            try:
                num1 = float(input("Angka pertama: "))
                num2 = float(input(f"{num1} pangkat: "))
                result = exponent(num1, num2)
                print(Fore.GREEN + f"Hasil: {num1} ^ {num2} = {result}")
                history.append(f"{num1} ^ {num2} = {result}")
            except ValueError:
                error = "Input tidak valid, mohon masukkan angka."
                print(Fore.RED + error)

        elif choice == 5:
            print("Ini adalah menu Akar Kuadrat")
            try:
                num1 = float(input("Ketik akar dari <angka>: "))
                result = square_root(num1)
                print(Fore.GREEN + f"Hasil: akar dari {num1} = {result}")
                history.append(f"akar dari {num1} = {result}")
            except ValueError:
                error = "Input tidak valid, mohon masukkan angka."
                print(Fore.RED + error)

        elif choice == 6:
            print("Riwayat Perhitungan:")
            for record in history:
                print(record)

    menu = [
        "1. Penjumlahan",
        "2. Perkalian",
        "3. Pembagian",
        "4. Persentase",
        "5. Eksponen",
        "6. Akar Kuadrat",
        "7. Riwayat Perhitungan"
    ]

    while True:
        choice = curses.wrapper(display_menu, menu, "Welcome to Hanna Calculators\nPilih operasi:")
        run_calculator(choice)

        next_calculation = input("Ingin melakukan perhitungan lagi? (ya/tidak): ")
        if next_calculation.lower() != 'ya':
            break

if __name__ == "__main__":
    install_dependencies()
    calculator()
