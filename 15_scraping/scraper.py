import csv

import bs4
import requests

# URL = 'https://www.espn.com/racing/raceresults/_/series/sprint/raceId/202102143995'
# RACE = '01_daytona_results'
URL = input("What is the espn race results URL: ")
RACE = input("What is the race number: ")


def pull_site():
    raw_site = requests.get(URL)
    raw_site.raise_for_status()

    return raw_site


def scrape(site):
    header_list = []

    soup = bs4.BeautifulSoup(site.text, 'html.parser')
    # get the table
    table = soup.find_all("tr")
    for row in table[1:]:
        temp = row.find_all("td")
        list = []
        for tag in temp:
            list.append(tag.get_text())
        header_list.append(list)

    return header_list


def write_csv(data):
    with open(f"{RACE}_results.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(data)


if __name__ == '__main__':
    site = pull_site()
    data = scrape(site)
    write_csv(data)
