from dataclasses import asdict
from dead_cells_wiki_scraper import models

melee_weapons_collection = u'melee_weapons'
ranged_weapons_collection = u'ranged_weapons'
shields_collection = u'shields'
traps_collection = u'traps'
grenades_collection = u'grenades'
powers_collection = u'powers'
enemies_collection = u'enemies'

class FirestoreManager:
    def __init__(self, db, provider):
        self.db = db
        self.provider = provider
        self.firestore_data = self.get_firestore_data()
        self.new_data = self.get_new_data()

    def get_firestore_data(self):
        melee_weapons = self.get_firebase_items(
            lambda weapon: models.Weapon(**weapon),
            melee_weapons_collection
        )
        ranged_weapons = self.get_firebase_items(
            lambda weapon: models.Weapon(**weapon),
            ranged_weapons_collection
        )
        shields = self.get_firebase_items(
            lambda shield: models.Shield(**shield),
            shields_collection
        )
        traps = self.get_firebase_items(
            lambda trap: models.TrapOrTurret(**trap),
            traps_collection
        )
        grenades = self.get_firebase_items(
            lambda grenade: models.Grenade(**grenade),
            grenades_collection
        )
        powers = self.get_firebase_items(
            lambda power: models.Power(**power),
            powers_collection
        )
        enemies = self.get_firebase_items(
            lambda enemy: models.Enemy(**enemy)
            enemies_collection
        )
        return {
            'melee_weapons': melee_weapons,
            'ranged_weapons': ranged_weapons,
            'shields': shields, 
            'traps': traps,
            'grenades': grenades,
            'powers': powers,
            'enemies': enemies
        }

    def get_new_data(self):
        melee_weapons = set(self.provider.get_melee_weapons())
        ranged_weapons = set(self.provider.get_ranged_weapons())
        shields = set(self.provider.get_shields())
        traps = set(self.provider.get_traps_and_turrets())
        grenades = set(self.provider.get_grenades())
        powers = set(self.provider.get_powers())
        enemies = set(self.provider.get_enemies())
        return {
            'melee_weapons': melee_weapons,
            'ranged_weapons': ranged_weapons,
            'shields': shields,
            'traps': traps,
            'grenades': grenades,
            'powers': powers,
            'enemies': enemies
        }

    def get_existing_collection(self, collection):
        docs = self.db.collection(collection).stream()
        result = []
        for doc in docs:
            result.append(doc.to_dict())
        return result

    def get_firebase_items(self, predicate, collection):
        return set(self.convert_to_model(predicate, self.get_existing_collection(collection)))

    def convert_to_model(self, predicate, dict_list):
        return [predicate(item) for item in dict_list]

    def get_diff(self, key):
        return { 
            'removals': list(self.firestore_data[key].difference(self.new_data[key])),
            'additions': list(self.new_data[key].difference(self.firestore_data[key]))
        }

    def get_diffs(self):
        return {
            'melee_diffs': self.get_diff('melee_weapons'),
            'ranged_diffs': self.get_diff('ranged_weapons'),
            'shield_diffs': self.get_diff('shields'),
            'trap_diffs': self.get_diff('traps'),
            'grenade_diffs': self.get_diff('grenades'),
            'power_diffs': self.get_diff('powers'),
            'enemy_diffs': self.get_diff('enemies')
        }

    def delete_collection(self, collection):
        docs = self.db.collection(collection).stream()
        for doc in docs:
            print('Deleting doc {} => {}'.format(doc.id, doc.to_dict()))
            doc.reference.delete()

    def write_list_to_firestore(self, collection, list):
        for item in list:
            self.db.collection(collection).document(item.name).set(asdict(item))

    def write_new_data_to_firestore(self):
        for collection, item_list in self.new_data.items():
            self.delete_collection(collection)
            self.write_list_to_firestore(collection, item_list)
        