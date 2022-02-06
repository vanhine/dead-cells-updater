from bs4 import BeautifulSoup
import urllib.request
from dead_cells_wiki_scraper import parsing_util as pu

URL = "https://deadcells.gamepedia.com/Gear"

class WeaponsProvider:
    def __init__(self):
        page = urllib.request.urlopen(URL)
        html = page.read().decode("utf-8")
        page.close()
        self.soup = BeautifulSoup(html, "html.parser") 
    
    def get_melee_weapons(self):
        melee_weapon_rows = pu.get_rows_from_child(self.soup, "Rusty Sword")
        return [pu.tr_to_weapon(row) for row in melee_weapon_rows[1:]]

    def get_ranged_weapons(self):
        ranged_weapon_rows = pu.get_rows_from_child(self.soup, "Beginner's Bow")
        return [pu.tr_to_weapon(row) for row in ranged_weapon_rows[1:]]

    def get_shields(self):
        shield_rows = pu.get_rows_from_child(self.soup, "Old Wooden Shield")
        return [pu.tr_to_shield(row) for row in shield_rows[1:]]

    def get_traps_and_turrets(self):
        trap_rows = pu.get_rows_from_child(self.soup, "Sinew Slicer")
        return [pu.tr_to_trap(row) for row in trap_rows[1:]]

    def get_grenades(self):
        grenade_rows = pu.get_rows_from_child(self.soup, "Infantry Grenade")
        return [pu.tr_to_grenade(row) for row in grenade_rows[1:]]

    def get_powers(self):
        power_rows = pu.get_rows_from_child(self.soup, "Death Orb")
        return [pu.tr_to_power(row) for row in power_rows[1:]]