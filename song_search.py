#!/usr/bin/env python
# coding: utf-8

# In[21]:


import requests
from bs4 import BeautifulSoup


# In[22]:


def song_search(song_title):
    url = "https://www.billboard.com/charts/greatest-hot-100-singles/"

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    chart_items = soup.select("ul > li.o-chart-results-list__item")

    songs = []

    for item in chart_items:
        title = item.find("h3")
        if title:
            title_text = title.get_text().strip()
            artist = item.find_all("span")[-1].get_text().strip()
            songs.append({"title": title_text, "artist": artist})

    for i, song in enumerate(songs, 1):
        if song_title.lower() == song['title'].lower():
            return i

    return -1

