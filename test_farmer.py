# FILE FOR FUNCTION == TEST
# complete with functions and tests

from class_Fonctions import Ferme
import copy

# =====================
# Examples
# =====================
my_farm_de_base = {
    "fields": [
        {"needed_water": 10},
        {"needed_water": 10},
        {"needed_water": 10},
        {"needed_water": 10},
        {"needed_water": 10},
    ],
    "employees": [
        #        {"id": id_employee, "location": "FIELD{nb_field}"},
        {"id": 1, "location": "FIELD1"},  # 0
        {"id": 2, "location": "FIELD1"},
        {"id": 3, "location": "FIELD1"},
        {"id": 4, "location": "FIELD1"},
        {"id": 5, "location": "FIELD1"},
        {"id": 6, "location": "FIELD1"},
        {"id": 7, "location": "FIELD1"},
        {"id": 8, "location": "FIELD1"},
        {"id": 9, "location": "FIELD1"},
        {"id": 10, "location": "FIELD1"},
        {"id": 11, "location": "FIELD1"},  # 10
        {"id": 12, "location": "FIELD1"},
        {"id": 13, "location": "FIELD1"},
        {"id": 14, "location": "FIELD1"},
        {"id": 15, "location": "FIELD1"},
        {"id": 16, "location": "FIELD1"},
        {"id": 17, "location": "FIELD1"},
        {"id": 18, "location": "FIELD1"},
        {"id": 19, "location": "FIELD1"},
        {"id": 20, "location": "FIELD1"},
        {"id": 21, "location": "FIELD1"},  # 20
        {"id": 22, "location": "FIELD1"},
        {"id": 23, "location": "FIELD1"},
        {"id": 24, "location": "FIELD1"},
        {"id": 25, "location": "FIELD1"},
        {"id": 26, "location": "FIELD1"},
        {"id": 27, "location": "FIELD1"},
        {"id": 28, "location": "FIELD1"},
        {"id": 29, "location": "FIELD1"},
        {"id": 30, "location": "FIELD1"},
        {"id": 31, "location": "FIELD1"},  # 30
        {"id": 32, "location": "FIELD1"},
        {"id": 33, "location": "FIELD1"},
        {"id": 34, "location": "FIELD1"},
        {"id": 35, "location": "FIELD1"},
        {"id": 36, "location": "FIELD1"},
        {"id": 37, "location": "FIELD1"},
        {"id": 38, "location": "FIELD1"},
        {"id": 39, "location": "FIELD1"},
        {"id": 40, "location": "FIELD1"},
        {"id": 41, "location": "FIELD1"},  # 40
        {"id": 42, "location": "FIELD1"},
        {"id": 43, "location": "FIELD1"},
        {"id": 44, "location": "FIELD1"},
        {"id": 45, "location": "FIELD1"},
        {"id": 46, "location": "FIELD1"},
        {"id": 47, "location": "FIELD1"},
        {"id": 48, "location": "FIELD1"},
        {"id": 49, "location": "FIELD1"},
        {"id": 50, "location": "FIELD1"},
        {"id": 51, "location": "FIELD1"},  # 50
        {"id": 52, "location": "FIELD1"},
        {"id": 53, "location": "FIELD1"},
        {"id": 54, "location": "FIELD1"},
        {"id": 55, "location": "FIELD1"},
        {"id": 56, "location": "FIELD1"},
        {"id": 57, "location": "FIELD1"},
        {"id": 58, "location": "FIELD1"},
        {"id": 59, "location": "FIELD1"},
    ],
}

# DEF ARROSER LOCALISATION TESTS


def test_arroser_localisation():

    ferme = Ferme("Ferme_1")
    ferme.my_farm = copy.deepcopy(my_farm_de_base)

    ouvrier = ferme.my_farm["employees"][8]["id"]
    champs = ferme.my_farm["fields"][4]["needed_water"] = 0

    ferme._commands.clear()

    ferme.arroser_localisation(ouvrier, champs)

    assert ferme._commands == []


def test_arroser_localisation_1():

    ferme = Ferme("Ferme_1")
    ferme.my_farm = copy.deepcopy(my_farm_de_base)

    ouvrier = ferme.my_farm["employees"][7]["id"]
    champs = ferme.my_farm["fields"][3]["needed_water"] = 1

    ferme._commands.clear()

    ferme.arroser_localisation(ouvrier, champs)

    assert ferme._commands == [f"{ouvrier} ARROSER {champs}"]
