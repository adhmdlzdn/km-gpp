# encoding: utf-8
# (c) 2021-2022, yn All rights reserved

# 1 - Import module
from datetime import datetime as dt
import time, os, sys


# 2 - Data, list, etc
usr = []
aby = []
now = dt.now()
date_time = now.strftime("%A, %d %b %Y (%H:%M:%S)")
clear = lambda : os.system("clear")


# 3 - Menu, Function, etc
# 3.1 - Restart program
def restart_program():
	os.system("cls")
	time.sleep(1)
	start()

# 3.2 - Start menu
def start():
	clear()
	b1()
	try:
		print("Diperbarui pada 27-10-21 (21:51)")
		print("Author		: yn")
		print("Github 		: https://github.com/myynxlazz")
		print("Bahasa		: Python versi 3")
		print("Deskripsi	: Just for fun")
		enter = input("[~] Tekan Enter untuk melanjutkan...")
	except KeyboardInterrupt:
		print("\n[!] Error : CTRL + C Terdeteksi... Menutup program..")
		time.sleep(2)
		exit()
	clear()
	user()

# 3.3 - Ask for name
def user():
	name = input("How do i call you? : ")
	if name.lower() == "fazila":
		bd = "22 Agustus 2004"
		aby.append(bd)
		tt = "Malang"
		aby.append(tt)
		ns = "SMK Telkom Malang"
		aby.append(ns)
		np = "adrian"
		aby.append(np)
	alt_name = "Catfish"
	alt_name2 = "lee.. lee.."
	response = input("Kalo aku panggil kamu {}, boleh ga? (y/n) ".format(alt_name))
	if response.lower() == "y":
		name = alt_name2
		usr.append(name)
		print("Asikk, mulai sekarang aku panggil kamu {}".format(name))
		time.sleep(2)
		loading()
	elif response.lower() == "n":
		usr.append(name)
		print("Nama yang bagus, {}!".format(name))
		time.sleep(2)
		loading()
	else:
		print("Yahh, gajelas nih. Yaudah kamu aku panggil {} aja".format(alt_name))
		name = alt_name
		usr.append(name)
		time.sleep(2)
		loading()

# 3.4 - Loading screen
def loading():
	clear()
	n = 100
	for i in range(n):
		time.sleep(0.05)
		sys.stdout.write("\r"+"Loading... Process "+str(i).format(n*100)+"%")
	clear()
	sys.stdout.write("\r"+"Loading... Finished\n")
	print("Selamat datang,", usr[0])
	time.sleep(2)
	clear()
	b1()
	menu()

# 3.5 - Menu
def menu():
	print("Diperbarui pada 27-10-21 (21:51)")
	print("Author		: yn")
	print("Github 		: https://github.com/myynxlazz")
	print("Bahasa		: Python versi 3")
	print("Versi		: 1.2")
	print("Time Now	:", date_time)
	print("(c) 2021-2022, yn All rights reserved")
	print("-------------------------------------")
	print("[$] Opsi :")
	print("	1. Tebak-tebakan")
	print("	2. Quiz")
	print("	3. Rekomendasi Film Untuk Mu")
	print("	8. About me")
	print("	9. Restart Program")
	print("	0. Keluar Program")
	try:
		opsi = input("[>] Pilihanmu : ")
		while True:
			if opsi == "1":
				time.sleep(1)
				tbk()
			elif opsi == "2":
				time.sleep(1)
				qz()
			elif opsi == "3":
				time.sleep(1)
				rf()
			elif opsi == "8":
				time.sleep(1)
				abt()
			elif opsi == "9":
				clear()
				time.sleep(1)
				restart_program()
			elif opsi == "0":
				clear()
				print("[!] Selamat tinggal, dadah :)")
				time.sleep(2)
				exit()
			else:
				print("[!] Error : Input yang dimasukkan tidak ada, silahkan pilih yang lain")
				time.sleep(1)
	except KeyboardInterrupt:
		print("\n[!] Error : CTRL + C Terdeteksi... Menutup program..")
		time.sleep(2)
		exit()

# 3.6 - Tebak-tebakan
def tbk():
	clear()
	b2()
	try:
		print("Time Now :", date_time)
		tb = input("\nSelamat datang di game Tebak-tebakan, silahkan tekan enter untuk melanjutkan...")
	except KeyboardInterrupt:
		print("\n[!] Error : CTRL + C Terdeteksi... Menutup program..")
		time.sleep(2)
		exit()
	clear()
	tb1()
# 3.6.1 - Pertanyaan
def tb1():
	tbkscore = 0
	question1 = print("1. Pohon pohon apa yang ditakuti negara? (hint : nikah)")
	response = input("Jawaban mu : ")
	if response.lower() == "pohuan maharani":
		print("Jawabanmu benar, lanjut\n\n")
		time.sleep(1)
		tbkscore = tbkscore + 2
	else:
		print("Salah, yang benar \"pohuan maharani\".\nChuaakkks. Maav, kamu kurang beruntung...\n\n")
		time.sleep(1)

	question2 = print("2. Sepatu, sepatu apa yang bisa dibuat masak? (hint : bikini bottom)")
	response = input("Jawaban mu : ")
	if response.lower() == "sepatula":
		print("Jawabanmu benar, lanjut\n\n")
		time.sleep(1)
		tbkscore = tbkscore + 2
	else:
		print("Salah, yang benar \"sepatula\".\nMaav, kamu kurang beruntung :(\n\n")
		time.sleep(1)

	question3 = print("3. Bahasa mandarinnya aneka macam sayur? (hint : edit video)")
	response = input("Jawaban mu : ")
	if response.lower() == "cap cay":
		print("Jawabanmu benar, lanjut\n\n")
		time.sleep(1)
		tbkscore = tbkscore + 2
	else:
		print("Salah, yang benar \"cap cay\".\nMaav, kamu kurang beruntung :(\n\n")
		time.sleep(1)

	question4 = print("4. Telor, telor apa yang diinjek tapi ngga pecah? (hint : jalan raya)")
	response = input("Jawaban mu : ")
	if response.lower() == "telortoar":
		print("Jawabanmu benar, lanjut\n\n")
		time.sleep(1)
		tbkscore = tbkscore + 2
	else:
		print("Salah, yang benar \"telortoar\".\nMaav, kamu kurang beruntung :(\n\n")
		time.sleep(1)

	question5 = print("5. Siapa nama penyanyi yang suka naik sepeda? (hint : cwk)")
	response = input("Jawaban mu : ")
	if response.lower() == "selena gowes":
		print("Jawabanmu benar, lanjut\n\n")
		time.sleep(1)
		tbkscore = tbkscore + 2
	else:
		print("Salah, yang benar \"selena gowes\".\nMaav, kamu kurang beruntung :(\n\n")
		time.sleep(1) 
		
	print("Yeay, kamu sudah menyelesaikan permainan Tebak-tebakan ini. Ditunggu ya update berikutnya! :)")
	print("Berikut score yang berhasil kamu proleh : ", tbkscore, "/ 10\n\n")
	while True:
		response = input("Ingin kembali ke main menu? (y/n) ")
		if response.lower() == "y":
			time.sleep(1)
			clear()
			b1()
			menu()
		elif response.lower() == "n":
			clear()
			print("[!] Selamat tinggal, dadah :)")
			time.sleep(2)
			exit()
		else:
			print("[!] Error : Input yang dimasukkan tidak ada, silahkan pilih yang lain")
			time.sleep(1)

# 3.7 - Quiz
def qz():
	clear()
	b3()
	try:
		print("Time Now	:", date_time)
		tb = input("\nSelamat datang di game Quiz, silahkan tekan enter untuk melanjutkan...")
	except KeyboardInterrupt:
		print("\n[!] Error : CTRL + C Terdeteksi... Menutup program..")
		time.sleep(2)
		exit()
	clear()
	qz1()
# 3.7.1 - Pertanyaan quiz
def qz1():
	qzscore = 0
	question6 = print("1. Kalau ada bus kecelakaan, pesawat jatuh, ada kapal tenggelam, semuanya akan muncul di mana?")
	response = input("Jawabanmu : ")
	if response.lower() == "di tv":
		print("Jawabanmu benar, lanjut\n\n")
		time.sleep(1)
		qzscore = qzscore + 2
	else:
		print("Salah, yang benar \"di tv\". Maav, kamu kurang beruntung :(\n\n")
		time.sleep(1)

	question7 = print("2. Jika ada 10 pejuang Indonesia yang berperang lalu ada satu orang yang gugur, ada berapa orang yang akan kembali ke markas?")
	response = input("Jawabanmu : ")
	if response.lower() == "1009":
		print("Jawabanmu benar, lanjut\n\n")
		time.sleep(1)
		qzscore = qzscore + 2
	else:
		print("Salah, yang benar \"1009\". Karna mati 1 tumbuh 1000, hehehe.\nMaav, kamu kurang beruntung :(\n\n")
		time.sleep(1)

	question8 = print("3. Kalau gajah mati siapa yang paling sedih?")
	response = input("Jawabanmu : ")
	if response.lower() == "tukang gali kubur":
		print("Jawabanmu benar, lanjut\n\n")
		time.sleep(1)
		qzscore = qzscore + 2
	else:
		print("Salah, yang benar \"tukang gali kubur\". Soalnya diperlukan lobang yang besar untuk mengguburkan gajah, hehehe.\nMaav, kamu kurang beruntung :(\n\n")
		time.sleep(1)

	question9 = print("4. Dalam sebuah keluarga, terdapat 3 anak perempuan yang masing-masing memiliki 1 adik laki-laki. Berapakah jumlah anak laki-laki dalam keluarga tersebut?")
	response = input("Jawabanmu : ")
	if response.lower() == "1 orang":
		print("Jawabanmu benar, lanjut\n\n")
		time.sleep(1)
		qzscore = qzscore + 2
	else:
		print("Salah, yang benar \"1 orang\". Soalnya adik laki-laki dari anak perempuan yang satu adalah adik laki-laki dari anak perempuan lainnya, hehehe.\nMaav, kamu kurang beruntung :(\n\n")
		time.sleep(1)

	question10 = print("5. Ibu david punya anak 4, jona, joni, jeni. Siapakah nama anak ke 4?")
	response = input("Jawabanmu : ")
	if response.lower() == "david":
		print("Jawabanmu benar, lanjut\n\n")
		time.sleep(1)
		qzscore = qzscore + 2
	else:
		print("Salah, yang benar \"david\". Kan ibu david punya anak 4, jona joni jeni yang terakhir berarti david dong, hehehe.\nMaav, kamu kurang beruntung :(\n\n")
		time.sleep(1)

	print("Yeay, kamu sudah menyelesaikan permainan Quiz ini. Ditunggu ya update berikutnya! :)")
	print("Berikut score yang berhasil kamu proleh : ", qzscore, "/ 10\n\n")
	while True:
		response = input("Ingin kembali ke main menu? (y/n) ")
		if response.lower() == "y":
			time.sleep(1)
			clear()
			b1()
			menu()
		elif response.lower() == "n":
			clear()
			print("[!] Selamat tinggal, dadah :)")
			time.sleep(2)
			exit()
		else:
			print("[!] Error : Input yang dimasukkan tidak ada, silahkan pilih yang lain")
			time.sleep(1)

# 3.8 - RFUM
def rfum():
	clear()
	print("Maaf, program ini sedang dalam pengerjaan")
	time.sleep(2)
	while True:
		response = input("Ingin kembali ke main menu? (y/n) ")
		if response.lower() == "y":
			time.sleep(1)
			clear()
			b1()
			menu()
		elif response.lower() == "n":
			clear()
			print("[!] Selamat tinggal, dadah :)")
			time.sleep(2)
			exit()
		else:
			print("[!] Error : Input yang dimasukkan tidak ada, silahkan pilih yang lain")
			time.sleep(1)


# 3.10 - About me
def abt():
	clear()
	b3()
	print("Time Now	:", date_time)
	print("""\nHalo... Sebelumnya perkenalkan, nama saya ev biasa dipanggil exel. Saya bekerja untuk PT. cinta abadi. 
Hobi saya menggalau dan menggamon. Keseharian BMMT (Bangun-Makan-Mandi-Tidur).
Pengen punya doi, tapi lebih kepengen duit banyak.
Mental sedikit keganggu, Kesehatan ya bgt, Makan masih nasi, Minum masih aqua. Stress dengan per sekolahan. 
Kata kata motivasi "kalo dapet alhamdulillah, ngga ya yaudah". "...ini belum separuhnya, biasa saja, kamu tak apa".
"Teknisi router nih boss, senggol dong, yahahaha". Buka jasa install ulang OS. Japri aja kalo minat.
Wibu tapi bukan tzy, eh dulu tapi. Maen PB g q? Mabar hayukkk, add username gua => rxlsthcdrz. Mabar beginner gas.
Twitter ada, tapi isinya keluh kesah kehidupan. Gausa dicari. Kalo FB buat repost meme, jangan dicari juga.
IG gada apa apanya, jangan difollow. Dah gt aja, kalo mau tau lebih lanjut bisa japri aja langsung ke orangnya. BYE.\n\n
		""")
	while True:
		response = input("About You? (y/n) ")
		if response.lower() == "y":
			if usr[0] == "fazila":
				time.sleep(1)
				clear()
				abty()
			else:
				print("Maaf, kamu tidak bisa mengakses menu ini\nSilahkan kembali...")
				time.sleep(1)
				clear()
				b1()
				menu()
		elif response.lower() == "n":
			time.sleep(1)
			clear()
			b1()
			menu()
		else:
			print("[!] Error : Input yang dimasukkan tidak ada, silahkan pilih yang lain")
			time.sleep(1)

# 3.x - ?
def abty():
	print("Nama kamu {}.".format(name()))
	time.sleep(1)
	print("Kamu lahir tanggal", aby[0],".")
	time.sleep(2)
	print("Kamu tinggal di", aby[1],".")
	time.sleep(3)
	print("Kamu sekolah di",aby[2],".")
	time.sleep(4)
	print("Iya kan?")
	while True:
		response = input("Ingin kembali ke main menu? (y/n) ")
		if response.lower() == "y":
			time.sleep(1)
			clear()
			b1()
			menu()
		elif response.lower() == "n":
			clear()
			print("[!] Selamat tinggal, dadah :)")
			time.sleep(2)
			exit()
		else:
			print("[!] Error : Input yang dimasukkan tidak ada, silahkan pilih yang lain")
			time.sleep(1)

	
# 4 - Banner
# 4.1 - Start banner
def b1():
	print('                   _         _    ')
	print('                  | |       | |   ')
	print('  __ _ _ __  _ __ | | _____ | | __')
	print(' / _` | \'_ \\| \'_ \\| |/ / _ \\| |/ /')
	print('| (_| | |_) | |_) |   < (_) |   < ')
	print(' \\__, | .__/| .__/|_|\\_\\___/|_|\\_\\ ')
	print('  __/ | |   | |__________________ ')
	print(' |___/|_|   |____________________|\n')

# 4.2 - Tebak-tebakan banner
def b2():
	print(' _   _     _    _   _     _               ')
	print('| | | |   | |  | | | |   | |              ')
	print('| |_| |__ | | _| |_| |__ | | ____ _ _ __  ')
	print('| __| \'_ \\| |/ / __| \'_ \\| |/ / _` | \'_ \\ ')
	print('| |_| |_) |   <| |_| |_) |   < (_| | | | |')
	print(' \\__|_.__/|_|\\_\\\\__|_.__/|_|\\_\\__,_|_| |_|')
	print('-------------------------------------------')

# 4.3 - Quiz banner
def b3():
	print('             _     ')
	print('            (_)    ')
	print('  __ _ _   _ _ ____')
	print(' / _` | | | | |_  /')
	print('| (_| | |_| | |/ / ')
	print(' \\__, |\\__,_|_/___|')
	print('    | |            ')
	print('    |_|            ')
	print('-------------------')

# 4.4 - Text Based Game banner
def b4():
	print('  _   _           ')
	print(' | | | |          ')
	print(' | |_| |__   __ _ ')
	print(' | __| \'_ \\ / _` |')
	print(' | |_| |_) | (_| |')
	print('  \\__|_.__/ \\__, |')	
	print('             __/ |')
	print('            |___/ ')
	print('------------------')

# 4.6 - About me banner
def b8():
	print('       _                 _                  ')
	print('      | |               | |                 ')
	print('  __ _| |__   ___  _   _| |_ _ __ ___   ___ ')
	print(' / _` | \'_ \\ / _ \\| | | | __| \'_ ` _ \\ / _ \\')
	print('| (_| | |_) | (_) | |_| | |_| | | | | |  __/')
	print(' \\__,_|_.__/ \\___/ \\__,_|\\__|_| |_| |_|\\___|')
	print('--------------------------------------------')


# 5 - Start
if __name__ == "__main__":
	start()
