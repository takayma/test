from random import randint as rd
from colorama import init, Fore
from playsound import playsound
import os
init(autoreset=True)

for i in range(100): print('')

good, bad = 0, 0
maxx = 10
minn = 1
mark = 0

path = os.getcwd()
true_path = path + r'\true_melody.mp3'
false_path = path + r'\false_melody.mp3'
marks_path = path + r'\marks.txt'


difficult = 1
availability_of_marks = 1

while True:
	#Генерация случайного примера
	args = [0, 0, minn - 1]
	sign = 0
	while args[2] < minn or args[2] > maxx:
		args[0], args[1] = rd(minn, maxx), rd(minn, maxx)
		sign = ('+', '-')[rd(0, 1)]
		args[2] = eval(f'{args[0]} {sign} {args[1]}')

	#Замена одного из аргументов пропуском
	space = 2
	if difficult == 2: space = rd(0, 2)
	correct_input = args[space]
	
	#Считывание ответа от пользователя
	while True:
		args[space] = '_'
		print(f'{args[0]} {sign} {args[1]} = {args[2]}')
		args[space] = input()
		for i in range(100): print('')
		
		#Закончить игру
		if args[space] == '':
			if availability_of_marks and mark != 0:
				file = open(marks_path, 'a')
				file.write(str(mark))
				file.close()
			os._exit(1)

		#Изменить параметры ишры
		elif args[space].strip().lower() in ('настройки', 'settings'):
			difficult = int(input('Сложность '))
			availability_of_marks = int(input('Сохранить окончательную оценку '))

			continue

		#Узнать статистику
		elif args[space].strip().lower() in ('статистика', 'status'):
			res, count = 0, 0
			file = open(marks_path, 'r')
			text = file.read()
			file.close()
			for x in text:
				res += int(x)
				count += 1	
			print(Fore.GREEN + f'Правильных ответов {good}')
			print(Fore.RED + f'Неправильных ответов {bad}') 
			print(f'Средний балл {round(res / count, 2)}')
			try:
				percent = round(good / (good + bad) * 100)
			except:
				percent = 0
			print(f'Процент выполнения {percent}%')

			if percent < 50:
				mark = 2
				print(Fore.RED + f'Оценка {mark}')
			elif 50 <= percent < 70:
				mark = 3
				print(Fore.MAGENTA + f'Оценка {mark}')
			elif 70 <= percent < 90:
				mark = 4
				print(Fore.YELLOW + f'Оценка {mark}')
			else:
				mark = 5
				print(Fore.GREEN + f'Оценка {mark}')

			continue

		args[space] = eval(args[space])

		#Ответ правильный
		if args[space] == correct_input:
			playsound(true_path, block=False)
			good += 1
			print(Fore.GREEN + f'{args[0]} {sign} {args[1]} = {args[2]}')
			break

		#Ответ не правильный
		else:
			playsound(false_path, block=False)
			bad += 1
			print(Fore.RED + f'{args[0]} {sign} {args[1]} \u2260 {args[2]}')
