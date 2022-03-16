import json
import requests
import os

def Urban():
	url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"
	key = input('[?] Input Slang/Urban Word : ')
	querystring = {"term":key}

	headers = {
		'x-rapidapi-host':"mashape-community-urban-dictionary.p.rapidapi.com",
		'x-rapidapi-key': "cdab10c346msha814bf020a2f051p1e3fbbjsneccd334a1722"
		}

	resp = requests.request("GET", url, headers=headers, params=querystring)
	i = resp.json()
	L = i["list"]

	for i in L:
		deff = i['example']
		aut = i['author']
		word = i['word']

		print('//'*30)
		print('[*] Author :',aut)
		print('[=] Word   :',word,'\n')
		print('[!] Definiton :')
		print(deff,'\n\n')

os.system('clear')
Urban()