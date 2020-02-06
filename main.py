import requests
from bs4 import BeautifulSoup
from config import *

def go(key):

	if key == "2":
		region_fr = "ouest"
		region_ar = "الغرب"
	elif key == "3":
		region_fr = "centre"
		region_ar = "الوسط"
	elif key == "4":
		region_fr = "est"
		region_ar = "الشرق"

	out_ar = list()
	out_fr = list()

	# dowloading the page, and parsing the data
	# for the arabic version
	html = requests.get(UNIV_LINK_AR)
	html = BeautifulSoup(html.text, 'html.parser')

	# fetching the first div(the west one), and getting the links from it
	# we do it on both arabic and fench version to get the complete one
	data_ar = html.find_all("div", id="column-{}".format(key))
	data_ar = data_ar[0].find_all("a")

	# adding the elements
	for item in data_ar:
		out_ar.append([item.get("href"), item.text])


	# dowloading the page, and parsing the data
	# for the french version
	html = requests.get(UNIV_LINK_FR)
	html = BeautifulSoup(html.text, 'html.parser')

	# fetching the first div(the west one), and getting the links from it
	# we do it on both arabic and fench version to get the complete one
	data_fr = html.find_all("div", id="column-{}".format(key))
	data_fr = data_fr[0].find_all("a")


	# adding the elements
	for item in data_fr:
		# adding the elements
		out_fr.append([item.get("href"), item.text])

	# a problem in there web site	
	if key == "2":
		out_fr.pop(-2)

	out = [{"web_site":item[0][0], "name_ar":item[0][1], "name_fr":item[1][1],
			"region_ar":region_ar, "region_fr":region_fr}
			for item in zip(out_ar, out_fr)]

	print(len(out))


go("2")

