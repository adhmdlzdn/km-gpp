# encoding: utf-8
# (c) 2021-2022, ev All rights reserved

# 1 - Import all modules we need
from datetime import datetime
import time, os, sys


# 2 - Data, list, etc
usr = []
aby = []
N = '\x1b[0m'
M = '\x1b[1;31m'
H = '\x1b[1;32m'
K = '\x1b[1;33m'
B = '\x1b[1;34m'
U = '\x1b[1;35m'
C = '\x1b[1;36m'
P = '\x1b[1;37m'
now = datetime.now()
date_time = now.strftime('%A, %d %b %Y (%H:%M:%S)')
clear = lambda : os.system('cls')
 

# 3 - Menu, Function, etc
# 3.1 - Restart program
def restart_program():
	start()

# 3.2 - Start menu
def start():
	clear()
	b1()
	try:
		print('Dibuat pada 19-09-2021 (22:58)')
		print('Author		: Exxvor')
		print('Kode		: Python versi 3')
		print('Deskripsi	: Iseng iseng aja')
		enter = input('[~] Tekan Enter untuk melanjutkan...')
	except KeyboardInterrupt:
		print('\n[!] Error : CTRL + C Terdeteksi... Menutup program..')
		time.sleep(2)
		exit()
	clear()
	user()

# 3.3 - Ask for username
def user():
	try:
		ask = input('Silahkan masukkan username yang akan kamu gunakan : ')
		while True:
			if ask == '':
				print('Silahkan isi usernamenya, jangan dibiarkan kosong ya!!\n')
				time.sleep(1)
			# Coba isi pake username yang kalian mau
			# Misalnya username pacar kalian
			# example : Fulan
			elif ask.lower() == '':
				usr.append(ask)
				# Terus masukin juga tanggal lahirnya
				bd = ''
				aby.append(bd)
				# Tempat tinggalnya
				tt = ''
				aby.append(tt)
				# Sekolahnya
				ns = ''
				aby.append(ns)
				doi = True
				time.sleep(1)
				loading()
			else:
				usr.append(ask)
				time.sleep(1)
				loading()
	except KeyboardInterrupt:
		print('\n[!] Error : CTRL + C Terdeteksi... Menutup program..')
		time.sleep(2)
		exit()

# 3.4 - Loading screen
def loading():
	n = 100
	for i in range(n):
		time.sleep(0.05)
		sys.stdout.write('\r'+'Loading... Process '+str(i).format(n*100)+'%')
	clear()
	sys.stdout.write('\r'+'Loading... Finished\n')
	print('Selamat datang,', usr[0])
	time.sleep(2)
	clear()
	b1()
	menu()

# 3.5 - Menu
def menu():
	print('Dibuat pada 19-09-2021 (22:58)')
	print('Author		: Exxvor')
	print('Kode		: Python versi 3')
	print('Versi		: 1.1')
	print('Time Now	:', date_time)
	print('(c) 2021-2022, ev All rights reserved')
	print('-------------------------------------')
	print('[$] Opsi :')
	print('	1. Tebak-tebakan')
	print('	2. Quiz')
	print('	3. About me')
	print('	4. Restart Program')
	print('	5. Keluar Program')
	try:
		opsi = input('[>] Pilihanmu : ')
		while True:
			if opsi == '1':
				time.sleep(1)
				tbk()
			elif opsi == '2':
				time.sleep(1)
				qz()
			elif opsi == '3':
				time.sleep(1)
				abt()
			elif opsi == '4':
				clear()
				time.sleep(1)
				restart_program()
			elif opsi == '5':
				clear()
				print('[!] Selamat tinggal, dadah :)')
				time.sleep(2)
				exit()
			else:
				print('[!] Error : Input yang dimasukkan tidak ada, silahkan pilih yang lain')
				time.sleep(1)
	except KeyboardInterrupt:
		print('\n[!] Error : CTRL + C Terdeteksi... Menutup program..')
		time.sleep(2)
		exit()

# 3.6 - Tebak-tebakan
def tbk():
	clear()
	b2()
	try:
		print('Time Now	:', date_time)
		tb = input('\nSelamat datang di game Tebak-tebakan, silahkan tekan enter untuk melanjutkan...')
	except KeyboardInterrupt:
		print('\n[!] Error : CTRL + C Terdeteksi... Menutup program..')
		time.sleep(2)
		exit()
	clear()
	tb1()
# 3.6.1 - Pertanyaan
def tb1():
	tbkscore = 0
	question1 = print('1. Gang apa yang selalu bikin ibu-ibu kesel? (hint : plkr)')
	response = input('Jawaban mu : ')
	if response.lower() == 'gangguin suaminya':
		print('Jawabanmu benar, lanjut\n\n')
		time.sleep(1)
		tbkscore = tbkscore + 2
	else:
		print('Salah, yang benar \'gangguin suaminya\'.\nMaav, kamu kurang beruntung :(\n\n')
		time.sleep(1)

	question2 = print('2. Apa itu cemilan? (hint : angka)')
	response = input('Jawaban mu : ')
	if response.lower() == 'cecudah celapan cebelum cepuluh':
		print('Jawabanmu benar, lanjut\n\n')
		time.sleep(1)
		tbkscore = tbkscore + 2
	else:
		print('Salah, yang benar \'cecudah celapan cebelum cepuluh\'.\nMaav, kamu kurang beruntung :(\n\n')
		time.sleep(1)

	question3 = print('3. Bahasa mandarinnya lantai basah? (hint : ke pleset)')
	response = input('Jawaban mu : ')
	if response.lower() == 'lhi chin':
		print('Jawabanmu benar, lanjut\n\n')
		time.sleep(1)
		tbkscore = tbkscore + 2
	else:
		print('Salah, yang benar \'lhi chin\'.\nMaav, kamu kurang beruntung :(\n\n')
		time.sleep(1)

	question4 = print('4. Siapa nama presiden yang kyut? (hint : nuklir)')
	response = input('Jawaban mu : ')
	if response.lower() == 'kim jong unch':
		print('Jawabanmu benar, lanjut\n\n')
		time.sleep(1)
		tbkscore = tbkscore + 2
	else:
		print('Salah, yang benar \'kim jong unch\'.\nMaav, kamu kurang beruntung :(\n\n')
		time.sleep(1)

	question5 = print('5. Siapa nama penyanyi yang ngga suka ngebut? (hint : gantung)')
	response = input('Jawaban mu : ')
	if response.lower() == 'melly goes slow':
		print('Jawabanmu benar, lanjut\n\n')
		time.sleep(1)
		tbkscore = tbkscore + 2
	else:
		print('Salah, yang benar \'melly goes slow\'.\nMaav, kamu kurang beruntung :(\n\n')
		time.sleep(1)

	print('Yeay, kamu sudah menyelesaikan permainan Tebak-tebakan ini. Ditunggu ya update berikutnya! :)')
	print('Berikut score yang berhasil kamu proleh : ', tbkscore, '/ 10\n\n')
	while True:
		response = input('Ingin kembali ke main menu? (y/n) ')
		if response.lower() == 'y':
			time.sleep(1)
			clear()
			b1()
			menu()
		elif response.lower() == 'n':
			clear()
			print('[!] Selamat tinggal, dadah :)')
			time.sleep(2)
			exit()
		else:
			print('[!] Error : Input yang dimasukkan tidak ada, silahkan pilih yang lain')
			time.sleep(1)

# 3.7 - Quiz
def qz():
	clear()
	b3()
	try:
		print('Time Now	:', date_time)
		tb = input('\nSelamat datang di game Quiz, silahkan tekan enter untuk melanjutkan...')
	except KeyboardInterrupt:
		print('\n[!] Error : CTRL + C Terdeteksi... Menutup program..')
		time.sleep(2)
		exit()
	clear()
	qz1()
# 3.7.1 - Pertanyaan quiz
def qz1():
	qzscore = 0
	question6 = print('1. Jika dibutuhkan waktu 10 menit untuk merebus 1 butir telur, berapa waktu yang diperlukan untuk merebus 5 butir telur?')
	response = input('Jawabanmu : ')
	if response.lower() == '10 menit':
		print('Jawabanmu benar, lanjut\n\n')
		time.sleep(1)
		qzscore = qzscore + 2
	else:
		print('Salah, yang benar \'10 menit\'. Soalnya tinggal direbus aja bareng bareng, hehehe.\nMaav, kamu kurang beruntung :(\n\n')
		time.sleep(1)

	question7 = print('2. Ada ayam lima, dikali dua. Berapa semuanya?')
	response = input('Jawabanmu : ')
	if response.lower() == '5':
		print('Jawabanmu benar, lanjut\n\n')
		time.sleep(1)
		qzscore = qzscore + 2
	else:
		print('Salah, yang benar \'5\'. Soalnya yang di kali 2, yang di darat 3, hehehe.\nMaav, kamu kurang beruntung :(\n\n')
		time.sleep(1)

	question8 = print('3. Kalau saja ada sekolah yang berisi semua jenis hewan, siapa yang sering terlambat?')
	response = input('Jawabanmu : ')
	if response.lower() == 'kaki seribu':
		print('Jawabanmu benar, lanjut\n\n')
		time.sleep(1)
		qzscore = qzscore + 2
	else:
		print('Salah, yang benar \'kaki seribu\'. Soalnya kaki dia ada 1000, kelamaan make sepatunya, hehehe.\nMaav, kamu kurang beruntung :(\n\n')
		time.sleep(1)

	question9 = print('4. Kalo gajah jadi ayam, singa jadi ayam, dan kambing jadi ayam, terus ayam jadi apa?')
	response = input('Jawabanmu : ')
	if response.lower() == 'ayam':
		print('Jawabanmu benar, lanjut\n\n')
		time.sleep(1)
		qzscore = qzscore + 2
	else:
		print('Salah, yang benar \'ayam\'. Soalnya ayamnya jadi banyak, hehehe.\nMaav, kamu kurang beruntung :(\n\n')
		time.sleep(1)

	question10 = print('5. Aku punya jeruk 5, kamu minta 2. Sisanya berapa?')
	response = input('Jawabanmu : ')
	if response.lower() == '5':
		print('Jawabanmu benar, lanjut\n\n')
		time.sleep(1)
		qzscore = qzscore + 2
	else:
		print('Salah, yang benar \'5\'. Soalnya jeruknya ga aku kasih, hehehe.\nMaav, kamu kurang beruntung :(\n\n')
		time.sleep(1)

	print('Yeay, kamu sudah menyelesaikan permainan Quiz ini. Ditunggu ya update berikutnya! :)')
	print('Berikut score yang berhasil kamu proleh : ', qzscore, '/ 10\n\n')
	while True:
		response = input('Ingin kembali ke main menu? (y/n) ')
		if response.lower() == 'y':
			time.sleep(1)
			clear()
			b1()
			menu()
		elif response.lower() == 'n':
			clear()
			print('[!] Selamat tinggal, dadah :)')
			time.sleep(2)
			exit()
		else:
			print('[!] Error : Input yang dimasukkan tidak ada, silahkan pilih yang lain')
			time.sleep(1)

# 3.8 - About me
def abt():
	clear()
	b3()
	print('Time Now	:', date_time)
	print('''\nHalo... Sebelumnya perkenalkan, nama saya ev biasa dipanggil exel. Saya bekerja untuk PT. cinta abadi. \nHobi saya menggalau dan menggamon. 
Keseharian BMMT (Bangun-Makan-Mandi-Tidur). Pengen punya doi, tapi lebih kepengen duit banyak.
Mental sedikit keganggu, Kesehatan ya bgt, Makan masih nasi, Minum masih aqua. 
Kata kata motivasi "kalo dapet alhamdulillah, ngga ya yaudah". Stress dengan per sekolahan.
"Teknisi router nih boss, senggol dong, yahahaha". Buka jasa install ulang OS. PC aja kalo minat.
Wibu tapi bukan tzy, eh dulu tapi. Maen PB g q? Mabar hayukkk, add username gua => rxlsthcdrz. Mabar begginer gas.
Twitter ada, tapi isinya keluh kesah kehidupan. Gausa dicari. Kalo FB buat repost meme, jangan dicari juga.
IG gada apa apanya, jangan difollow. Dah gt aja, kalo mau tau lebih lanjut bisa PC aja langsung ke orangnya. BYE.\n\n
		''')
	while True:
		response = input('About You? (y/n) ')
		if response.lower() == 'y':
			# Isi dengan nama yang tadi diawal
			# example : Fulan
			if usr[0] == '':
				time.sleep(1)
				clear()
				abty()
			else:
				print('Maaf, kamu tidak bisa mengakses menu ini\nSilahkan kembali...')
				time.sleep(1)
				clear()
				b1()
				menu()
		elif response.lower() == 'n':
			time.sleep(1)
			clear()
			b1()
			menu()
		else:
			print('[!] Error : Input yang dimasukkan tidak ada, silahkan pilih yang lain')
			time.sleep(1)

# 3.x - ?
def abty():
	print('Nama kamu', usr[0],'. \nKamu lahir tanggal', aby[0],'. \nKamu tinggal di', aby[1],'. \nKamu sekolah di',aby[2],'. \nIya kan?')
	while True:
		response = input('Ingin kembali ke main menu? (y/n) ')
		if response.lower() == 'y':
			time.sleep(1)
			clear()
			b1()
			menu()
		elif response.lower() == 'n':
			clear()
			print('[!] Selamat tinggal, dadah :)')
			time.sleep(2)
			exit()
		else:
			print('[!] Error : Input yang dimasukkan tidak ada, silahkan pilih yang lain')
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

# 4.4 - About me banner
def b3():
	print('       _                 _                  ')
	print('      | |               | |                 ')
	print('  __ _| |__   ___  _   _| |_ _ __ ___   ___ ')
	print(' / _` | \'_ \\ / _ \\| | | | __| \'_ ` _ \\ / _ \\')
	print('| (_| | |_) | (_) | |_| | |_| | | | | |  __/')
	print(' \\__,_|_.__/ \\___/ \\__,_|\\__|_| |_| |_|\\___|')
	print('--------------------------------------------')


# 5 - Start
start()
