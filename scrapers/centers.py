from bs4 import BeautifulSoup
import requests
import os

from config import CENTER_LINK_AR, CENTER_LINK_FR, BASE_DIR
from managedata import dumpData
import tools


def get_center_data(key):
    """Fro scraping the list of algerian national teachers schools,
    the key is to specify the regions, the code is not perfect,
    but it does the work.

    It return a list of dectionaries of this format:
    out_data = {
        "web_site":"",
        "name_ar":"",
        "name_fr":"",
        "name_en":"",
        "region_ar":"",
        "region_fr":"",
        "region_en":"",
    }
    """
    if key == "2":
        region_ar = "الغرب"
        region_en = "west"
        region_fr = "ouest"
    elif key == "3":
        region_ar = "الوسط"
        region_fr = "centre"
        region_en = "center"
    elif key == "4":
        region_ar = "الشرق"
        region_en = "east"
        region_fr = "est"

    # data, by each language
    out_ar = list()
    out_fr = list()
    out_en = list()

    '''Extracting the data for the arabic version'''
    # dowloading the page, and parsing the data
    # for the arabic version
    html = requests.get(CENTER_LINK_AR)
    html = BeautifulSoup(html.text, 'html.parser')

    # fetching the first div(the west one), and getting the links from it
    # we do it on both arabic and fench version to get the complete one
    data_ar = html.find_all("div", id="column-{}".format(key))
    data_ar = data_ar[0].find_all("a")

    # fetching the first div(the west one), and getting the links from it
    # we do it on both arabic and fench version to get the complete one
    data_ar = html.find_all("div", id="column-{}".format(key))
    data_ar = data_ar[0].find_all("a")

    # adding the elements
    for item in data_ar:
        try:
            out_ar.append([item.get("href").rstrip(),
                           item.text.replace("\xa0", "")])
        except:
            pass

    '''Extracting the data for the french version'''
    # dowloading the page, and parsing the data
    # for the french version
    html = requests.get(CENTER_LINK_FR)
    html = BeautifulSoup(html.text, 'html.parser')

    # fetching the first div(the west one), and getting the links from it
    # we do it on both arabic and fench version to get the complete one
    data_fr = html.find_all("div", id="column-{}".format(key))
    data_fr = data_fr[0].find_all("a")

    # adding the elements
    for item in data_fr:
        # adding the elements
        try:
            out_fr.append([item.get("href").rstrip(),
                           item.text.replace("\xa0", "")])
        except:
            pass

    '''Converting university names from French to English'''
    # converting university name from franch to english
    for item in out_fr:
        name = item[-1]
        name = tools.replacing(name)
        out_en.append([item[0], name])

    for zip_item in zip(out_ar, out_fr, out_en):
        univ = {
            "web_site": zip_item[0][0],
            "name_ar": zip_item[0][1],
            "name_fr": zip_item[1][1],
            "name_en": zip_item[2][1],
            "region_ar": region_ar,
            "region_fr": region_fr,
            "region_en": region_en,
        }

        yield univ


if __name__ == "__main__":
    pass
    # data = list()  # sotre the data

    # # pasrse the key, to extract the data
    # for key in ["2", "3", "4"]:
    #     for univ_item in get_center_data(key):
    #         data.append(univ_item)

    # # dumping the data into jdon file
    # dumpData(os.path.join(BASE_DIR, "data/universities/center.json"), {"centers": data})

    # # write data into csv file
    # tools.csv_writer(os.path.join(BASE_DIR, "data/universities/center.csv"),
    #                  ["web_site", "name_ar", "name_fr", "name_en",
    #                   "region_ar", "region_fr", "region_en"],
    #                  [val.values() for val in data])
