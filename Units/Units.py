class Unit_status:
    """ Abstract class inherited by all the units """
    ARMOR_TYPES = ['light', 'heavy']
    DAMAGE_TYPES = ['normal', 'heavy', 'range', 'magic', 'swift']

    def __init__(self, price, health, armor_type, armor, \
                 damage_type, damage, requiered_level):

        self.price = price
        self.health = health
        self.armor_type = self.ARMOR_TYPES[armor_type]
        self.armor = armor
        self.damage_type = self.DAMAGE_TYPES[damage_type]
        self.damage = damage
        self.requiered_level = requiered_level


ELF_UNITS = {'archer': Unit_status(20, 200, 0, 5, 2, 300, 1), \
             'rogue': Unit_status(35,  300, 0, 7, 0, 300, 3), \
             'druid': Unit_status(60, 450, 0, 10, 3, 300, 5), \
             'assasin': Unit_status(80, 500, 0, 10, 4, 500, 7)}

TROLL_UNITS = {'fermer': Unit_status(15, 200, 0, 3, 0, 200, 1), \
               'hunter': Unit_status(20, 300, 0, 3, 2, 300, 3), \
               'warrior': Unit_status(70,  500, 1, 10, 1, 350, 6),\
               'warlock': Unit_status(100, 500, 0, 10, 3, 400, 8)}

HUMAN_UNITS = {'mage': Unit_status(30, 200, 0, 4, 3, 300, 1), \
               'defender': Unit_status(40, 350, 1, 15, 0, 200, 3),\
               'knight': Unit_status(60, 400, 1, 10, 1, 350, 5), \
               'wizzard': Unit_status(100, 450, 0, 10, 3, 450, 7)}

DWARF_UNITS = {'miner': Unit_status(30, 300, 1, 10, 0, 300, 1), \
               'priest': Unit_status(40, 250, 1, 10, 3, 400, 3), \
               'crossbow': Unit_status(45, 400, 1, 10, 2, 300, 5),\
               'hammer': Unit_status(100, 600, 1, 10, 1, 300, 8)}
