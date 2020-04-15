from bs4 import BeautifulSoup
import requests
import os

from managedata import loadData

global links, univ_names, data

"""
	club_name, univ_name, president_club, club_depart, club_type, facebook_page, linkedin_page, phone, Email, logo_link, data_pdf
"""

def categorie1(list):
	# No Contacts but still maybe scrap it for future updates
	for i in list:
		html = requests.get(links[i]+"clubs-scientifiques")
		html = BeautifulSoup(html.text, 'html.parser')
		headers = html.find_all("span", {"class": "rl_sliders-toggle-inner nn_sliders-toggle-inner"})
		for x in headers:
			arr = []
			arr = x.text.rstrip().split("-")
			if len(arr) < 2:
				arr = x.text.split("–")
			if len(arr) == 2:
				data.append([arr[0], univ_names[i], "", arr[1], "scientifique", "", "", "", "", ""])
			elif len(arr) == 3:
				data.append([arr[0], univ_names[i], "", arr[1]+"-"+arr[2], "scientifique", "", "", "", "", ""])

def categorie2(list):
	for i in list:
		html = requests.get(links[i]+"Vie%20Etudiante/Clubs-scientifiques.html")
		html = BeautifulSoup(html.text, 'html.parser')
		tab = html.find_all("div", {"class": "resp-tabs-container"})[0]
		body = tab.findChildren("div" , recursive=False)[0]
		names = body.findChildren("strong" , recursive=False)
		donnees = body.findChildren("div" , recursive=False)
		Names = []
		for name in names:
			Names += [name.encode('utf-8')]
		p = 0
		for donnee in donnees:
			d = donnee.findChildren("ul" , recursive=False)
			if len(d) > 1:
				d = d[1]
			else:
				d = d[0]
			arr = d.text.strip().rstrip().split("\n")
			president = arr[0].split(":")[1].rstrip().strip().encode('utf-8')
			tel = arr[1].split(":")[1].rstrip().strip()
			email = arr[2].split(":")[1].rstrip().strip()
			dept = arr[4].split(":")[1].rstrip().strip()
			data.append([Names[p], univ_names[i], president, dept, "scientifique", "", "", tel, email, "", ""])
			p += 1

def categorie3(list):
	for i in list:
		html = requests.get(links[i]+"/clubs-scientifiques/")
		html = BeautifulSoup(html.text, 'html.parser')
		names = html.find_all("h3", {"class": "section-heading sh-t1 sh-s5"})
		Names = []
		for name in names:
			Names += [name.text.strip().rstrip().split(' ')[2]]
		images = html.find_all("img", {"class": "vc_single_image-img attachment-thumbnail"})
		p = 0
		for image in images:
			data.append([Names[p], univ_names[i], "", "", "scientifique", "", "", "", "", image["src"], ""])
			p += 1

links = []
univ_names = []
data = []
myUniversities = loadData("data/univ.json")
for x in myUniversities["universities"]:
	links.append(x["web_site"])
	univ_names.append(x["name_fr"])

i=0
for x in links:
	if "www.univ-setif.dz" in x:
		print(i)
		break
	i += 1
	
cat1 = [44]
cat2 = [19]
cat3 = [7]

#categorie1(cat1)
#categorie2(cat2)
#categorie3(cat3)
print(data)