from dead_cells_wiki_scraper.providers import enemies
from dead_cells_wiki_scraper.providers import weapons
from dead_cells_wiki_scraper import parsing_util as pu

class DeadCellsWikiProvider:
    gear_url = "https://deadcells.gamepedia.com/Gear"
    soup = ""

    def __init__(self):
        self.enemies_provider = enemies.EnemiesProvider()
        self.weapons_provider = weapons.WeaponsProvider()

    def get_melee_weapons(self):
        return self.weapons_provider.get_melee_weapons()

    def get_ranged_weapons(self):
        return self.weapons_provider.get_ranged_weapons()

    def get_shields(self):
        return self.weapons_provider.get_shields()

    def get_traps_and_turrets(self):
        return self.weapons_provider.get_traps_and_turrets()

    def get_grenades(self):
        return self.weapons_provider.get_grenades()

    def get_powers(self):
        return self.weapons_provider.get_powers()

    def get_enemies(self):
        return self.enemies_provider.get_enemies()
