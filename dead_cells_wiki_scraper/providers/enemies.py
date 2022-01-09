from bs4 import BeautifulSoup
import urllib.request
from dead_cells_wiki_scraper import parsing_util as pu

URL = "https://deadcells.gamepedia.com/Enemies"

class EnemiesProvider:
    def __init__(self):
        page = urllib.request.urlopen(URL)
        html = page.read().decode("utf-8")
        page.close()
        self.soup = BeautifulSoup(html, "html.parser") 

    def get_enemies(self):
        rows = pu.get_rows_from_child(self.soup, "Zombie")
        return [pu.tr_to_enemy(row) for row in rows[1:]]