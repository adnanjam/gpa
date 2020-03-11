import requests
import getpass
import webbrowser
from bs4 import BeautifulSoup
import os

username = input("Ange ditt användarnamn: ")
password = getpass.getpass(prompt="Ange ditt lösenord: ")

score_dict = {"A": 5, "B": 4.5, "C": 4, "D": 3.5, "E": 3, "F": 0, "P": 3}

# Log in url for antagning.se
login_url = "https://www.antagning.se/se/loginajax"
merits_url = "https://www.antagning.se/se/mypages/credentials"

# log in the user at antagning.se
session = requests.Session()
res = session.post(
    login_url, data={"username": username, "password": password})


# now get the merits page:

res = session.get(
    "https://www.antagning.se/se/mypages/credentials")

soup = BeautifulSoup(res.text, features="html.parser")
rows = soup.findAll("tr", {"class": "haschild"})

sum_points = 0
sum_grade = 0

for r in rows:
    tds = r.findChildren()

    hp = float(tds[2].text.strip().replace(",", "."))
    score = tds[3].text.strip()
    eligible = tds[5].text.strip()

    if(eligible == "Ja"):
        sum_grade += int(score_dict[score]) * hp
        sum_points += hp


print("Ditt mertivärder är: ", sum_grade/sum_points)
