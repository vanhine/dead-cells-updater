from dataclasses import dataclass

@dataclass(eq=True, frozen=True)
class Weapon:
    name: str
    description: str
    blueprint_location: str
    base_dps: str
    base_special_dps: str
    scaling: str
    image_url: str

    def __str__(self):
        return '''Name:<strong>{}</strong><br>
                  Description:{}<br>
                  Blueprint Location:{}<br>
                  Base DPS:{}<br>
                  Base Special DPS:{}<br>
                  Scaling URL:{}<br>
                  Image URL:{}
                '''.format(
            self.name, 
            self.description, 
            self.blueprint_location,
            self.base_dps,
            self.base_special_dps,
            self.scaling,
            self.image_url)

@dataclass(eq=True, frozen=True)
class Shield:
    name: str
    description: str
    blueprint_location: str
    block_damage: str
    parry_damage: str
    absorb_damage: str
    scaling: str
    image_url: str

    def __str__(self):
        return '''Name:<strong>{}</strong><br>
                  Description:{}<br>
                  Blueprint Location:{}<br>
                  Block Dmg:{}<br>
                  Parry Dmg:{}<br>
                  Absorb Dmg:{}<br>
                  Scaling URL:{}<br>
                  Image URL:{}
                '''.format(
            self.name, 
            self.description, 
            self.blueprint_location,
            self.block_damage,
            self.parry_damage,
            self.absorb_damage,
            self.scaling,
            self.image_url)

@dataclass(eq=True, frozen=True)
class TrapOrTurret:
    name: str
    description: str
    blueprint_location: str
    base_damage: str
    base_cooldown_time: str
    scaling: str
    image_url: str

    def __str__(self):
        return '''Name:<strong>{}</strong><br>
                  Description:{}<br>
                  Blueprint Location:{}<br>
                  Base Dmg:{}<br>
                  Base Cooldown Time:{}<br>
                  Scaling URL:{}<br>
                  Image URL:{}
                '''.format(
            self.name, 
            self.description, 
            self.blueprint_location,
            self.base_damage,
            self.base_cooldown_time,
            self.scaling,
            self.image_url)

@dataclass(eq=True, frozen=True)
class Grenade:
    name: str
    description: str
    blueprint_location: str
    base_damage: str
    base_cooldown_time: str
    damage_reduction: str
    scaling: str
    image_url: str

    def __str__(self):
        return '''Name:<strong>{}</strong><br>
                  Description:{}<br>
                  Blueprint Location:{}<br>
                  Base Dmg:{}<br>
                  Base Cooldown Time:{}<br>
                  Dmg Reduction:{}<br>
                  Scaling URL:{}<br>
                  Image URL:{}
                '''.format(
            self.name, 
            self.description, 
            self.blueprint_location,
            self.base_damage,
            self.base_cooldown_time,
            self.damage_reduction,
            self.scaling,
            self.image_url)

@dataclass(eq=True, frozen=True)
class Power:
    name: str
    description: str
    blueprint_location: str
    base_damage: str
    base_cooldown_time: str
    damage_reduction: str
    scaling: str
    image_url: str

    def __str__(self):
        return '''Name:<strong>{}</strong><br>
                  Description:{}<br>
                  Blueprint Location:{}<br>
                  Base Dmg:{}<br>
                  Base Cooldown Time:{}<br>
                  Dmg Reduction:{}<br>
                  Scaling URL:{}<br>
                  Image URL:{}
                '''.format(
            self.name, 
            self.description, 
            self.blueprint_location,
            self.base_damage,
            self.base_cooldown_time,
            self.damage_reduction,
            self.scaling,
            self.image_url)

@dataclass(eq=True, frozen=True)
class Enemy:
    name: str
    zones: str
    offensive_abilities: str
    defensive_abilities: str
    elite: str
    blueprint_drops: str
    image_url: str

    def __str__(self):
        return '''Name:<strong>{}</strong><br>
                  Zones:{}<br>
                  Offensive Abilities:{}<br>
                  Defensive Abilities:{}<br>
                  Elite?:{}<br>
                  Blueprint Drops:{}<br>
                  Image URL:{}
                '''.format(
                    self.name,
                    self.zones,
                    self.offensive_abilities,
                    self.defensive_abilities,
                    self.elite,
                    self.blueprint_drops,
                    self.image_url
                )