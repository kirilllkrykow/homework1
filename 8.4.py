class Storage:
    volume = 500
    equip = {"print":200, "scan":100, "copy":75, "other":25, "empty":100}

class Equip:
    type = "type"
    value = "value"
    number = "number"

class Printer(Equip):
    type = "type"
    speed_of_print = "30"

class Scan(Equip):
    brand = "Xerox"
    speed = "8"

class Copier(Equip):
    brand = "hp"
    size = "800"

