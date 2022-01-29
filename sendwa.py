import pywhatkit as kit
a = input("Nomor Telepon : ")
b = input("Teks : ")
c = int(input("Jam : "))
d = int(input("Menit : "))
kit.sendwhatmsg(a, b, c, d)