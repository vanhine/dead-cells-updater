from dead_cells_wiki_scraper import models


def get_rows_from_child(soup, child_text):
    parent_table = soup.find(text=child_text).find_parent('table')
    table_body = parent_table.find('tbody')
    return table_body.find_all('tr')


def split_dps(dps):
    result = dps.split(' ')
    base_special_dps = ''
    if len(result) > 1:
        base_special_dps = result[1]
    base_dps = result[0]
    return base_dps, base_special_dps


def tr_to_weapon(table_row):
    columns = table_row.find_all('td')
    image_url = columns[0].find('img')['data-src']
    name = columns[1].find('a').getText()
    description = columns[2].getText()
    blueprint_location = columns[3].getText()
    base_dps, base_special_dps = split_dps(columns[4].getText())
    scaling_img_url = columns[5].find('img')['data-src']
    return models.Weapon(name, description, blueprint_location, base_dps, base_special_dps, scaling_img_url, image_url)


def tr_to_shield(table_row):
    columns = table_row.find_all('td')
    image_url = columns[0].find('img')['data-src']
    name = columns[1].find('a').getText()
    description = columns[2].getText()
    blueprint_location = columns[3].getText()
    if len(columns) == 7:
        block_damage = columns[4].getText()
        parry_damage = columns[4].getText()
        absorb_damage = columns[5].getText()
        scaling_img_url = columns[6].find('img')['data-src']
    else:
        block_damage = columns[4].getText()
        parry_damage = columns[5].getText()
        absorb_damage = columns[6].getText()
        scaling_img_url = columns[7].find('img')['data-src']
    return models.Shield(name, description, blueprint_location, block_damage, parry_damage, absorb_damage, scaling_img_url, image_url)


def tr_to_trap(table_row):
    columns = table_row.find_all('td')
    image_url = columns[0].find('img')['data-src']
    name = columns[1].find('a').getText()
    description = columns[2].getText()
    blueprint_location = columns[3].getText()
    base_damage = columns[4].getText()
    base_cooldown_time = columns[5].getText()
    try:
        scaling_image_url = columns[6].find('img')['data-src']
    except:
        scaling_image_url = columns[6].getText()
    return models.TrapOrTurret(name, description, blueprint_location, base_damage, base_cooldown_time, scaling_image_url, image_url)


def tr_to_grenade(table_row):
    columns = table_row.find_all('td')
    image_url = columns[0].find('img')['data-src']
    name = columns[1].find('a').getText()
    description = columns[2].getText()
    blueprint_location = columns[3].getText()
    base_damage = columns[4].getText()
    base_cooldown_time = columns[5].getText()
    damage_reduction = ''
    scaling_image_url = columns[6].find('img')['data-src']
    return models.Grenade(name, description, blueprint_location, base_damage, base_cooldown_time, damage_reduction, scaling_image_url, image_url)


def tr_to_power(table_row):
    columns = table_row.find_all('td')
    image_url = columns[0].find('img')['data-src']
    name = columns[1].find('a').getText()
    description = columns[2].getText()
    blueprint_location = columns[3].getText()
    base_damage = columns[4].getText()
    base_cooldown_time = columns[5].getText()
    damage_reduction = ''
    scaling_image_url = columns[6].find('img')['data-src']
    return models.Power(name, description, blueprint_location, base_damage, base_cooldown_time, damage_reduction, scaling_image_url, image_url)


def tr_to_enemy(table_row):
    columns = table_row.find_all('td')
    name = columns[1].find('a').getText()
    zone_element = columns[2].find_all('i')
    zones = []
    for zone in zone_element:
        zones.append(zone.getText())
    zone_str = ''.join(zones)
    offensive_abilities = columns[3].getText()
    defensive_abilities = columns[4].getText()
    elite = columns[5].getText()
    blueprint_drops = None
    if len(columns) > 5:
        blueprint_drops = columns[6].getText()
    img_tag = columns[0].find('img')
    if img_tag.get('data-src'):
        image_url = img_tag.get('data-src')
    else:
        image_url = img_tag.get('src')
    return models.Enemy(name, zone_str, offensive_abilities,
                        defensive_abilities, elite, blueprint_drops, image_url)
