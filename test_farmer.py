# FILE FOR FUNCTION == TEST
# complete with functions and tests

from class_Fonctions import Ferme
import copy

# =====================
# Examples
# =====================

legume = ["POTATO", "LEEK", "TOMATO", "ONION", "ZUCCHINI"]

my_farm_de_base = {
    "fields": [
        {"needed_water": 10, "content": "NONE", "location": "FIELD1"},
        {"needed_water": 10, "content": "TOMATO", "location": "FIELD2"},
        {"needed_water": 10, "content": "NONE", "location": "FIELD3"},
        {"needed_water": 10, "content": "NONE", "location": "FIELD4"},
        {"needed_water": 10, "content": "NONE", "location": "FIELD5"},
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
    "tracteur": [1, 2, 3],
    "soup_factory": "SOUP_FACTORY",
    "stock": legume,
}

location_ouvrier_soupfactory = {
    "employees_location": [
        {"id": 1, "location": "SOUP_FACTORY"},
        {"id": 2, "location": "SOUP_FACTORY"},
        {"id": 3, "location": "SOUP_FACTORY"},
        {"id": 4, "location": "SOUP_FACTORY"},
        {"id": 5, "location": "SOUP_FACTORY"},
        {"id": 6, "location": "SOUP_FACTORY"},
        {"id": 7, "location": "SOUP_FACTORY"},
        {"id": 8, "location": "SOUP_FACTORY"},
        {"id": 9, "location": "SOUP_FACTORY"},
        {"id": 10, "location": "SOUP_FACTORY"},
        {"id": 11, "location": "SOUP_FACTORY"},
        {"id": 12, "location": "SOUP_FACTORY"},
        {"id": 13, "location": "SOUP_FACTORY"},
        {"id": 14, "location": "SOUP_FACTORY"},
        {"id": 15, "location": "SOUP_FACTORY"},
        {"id": 16, "location": "SOUP_FACTORY"},
        {"id": 17, "location": "SOUP_FACTORY"},
        {"id": 18, "location": "SOUP_FACTORY"},
        {"id": 19, "location": "SOUP_FACTORY"},
        {"id": 20, "location": "SOUP_FACTORY"},
        {"id": 21, "location": "SOUP_FACTORY"},
        {"id": 22, "location": "SOUP_FACTORY"},
        {"id": 23, "location": "SOUP_FACTORY"},
        {"id": 24, "location": "SOUP_FACTORY"},
        {"id": 25, "location": "SOUP_FACTORY"},
        {"id": 26, "location": "SOUP_FACTORY"},
        {"id": 27, "location": "SOUP_FACTORY"},
        {"id": 28, "location": "SOUP_FACTORY"},
        {"id": 29, "location": "SOUP_FACTORY"},
        {"id": 30, "location": "SOUP_FACTORY"},
        {"id": 31, "location": "SOUP_FACTORY"},
        {"id": 32, "location": "SOUP_FACTORY"},
        {"id": 33, "location": "SOUP_FACTORY"},
        {"id": 34, "location": "SOUP_FACTORY"},
        {"id": 35, "location": "SOUP_FACTORY"},
        {"id": 36, "location": "SOUP_FACTORY"},
        {"id": 37, "location": "SOUP_FACTORY"},
        {"id": 38, "location": "SOUP_FACTORY"},
        {"id": 39, "location": "SOUP_FACTORY"},
        {"id": 40, "location": "SOUP_FACTORY"},
        {"id": 41, "location": "SOUP_FACTORY"},
        {"id": 42, "location": "SOUP_FACTORY"},
        {"id": 43, "location": "SOUP_FACTORY"},
        {"id": 44, "location": "SOUP_FACTORY"},
        {"id": 45, "location": "SOUP_FACTORY"},
        {"id": 46, "location": "SOUP_FACTORY"},
        {"id": 47, "location": "SOUP_FACTORY"},
        {"id": 48, "location": "SOUP_FACTORY"},
        {"id": 49, "location": "SOUP_FACTORY"},
        {"id": 50, "location": "SOUP_FACTORY"},
        {"id": 51, "location": "SOUP_FACTORY"},
        {"id": 52, "location": "SOUP_FACTORY"},
        {"id": 53, "location": "SOUP_FACTORY"},
        {"id": 54, "location": "SOUP_FACTORY"},
        {"id": 55, "location": "SOUP_FACTORY"},
        {"id": 56, "location": "SOUP_FACTORY"},
        {"id": 57, "location": "SOUP_FACTORY"},
        {"id": 58, "location": "SOUP_FACTORY"},
        {"id": 59, "location": "SOUP_FACTORY"},
    ],
}

game_data_base = {"day": 1}


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


# DEF VENDRE TEST


def test_vendre():

    ferme = Ferme("Ferme_1")
    ferme.my_farm = copy.deepcopy(my_farm_de_base)
    champ = ferme.my_farm["fields"][2]
    champ["needed_water"] = 10

    ferme._commands.clear()

    ferme.vendre(champ)

    assert ferme._commands == []


def test_ne_pas_vendre():
    ferme = Ferme("Ferme_1")
    ferme.my_farm = copy.deepcopy(my_farm_de_base)
    champ = ferme.my_farm["fields"][2]
    champ["needed_water"] = 0

    ferme._commands.clear()

    ferme.vendre(champ)

    assert ferme._commands == [f"0 VENDRE{champ ['location'][-1]}"]


# DEF SEMER VENTE TEST


def test_semer_vente():

    ferme = Ferme("Ferme_1")
    ferme.my_farm = copy.deepcopy(my_farm_de_base)
    # TODO:


# DEF STOCKER TEST


def test_stocker():
    ferme = Ferme("Ferme_1")
    ferme.my_farm = copy.deepcopy(my_farm_de_base)
    ouvrier = ferme.my_farm["employees"][7]["id"]
    tracteur = ferme.my_farm["tracteur"][1]
    champ = ferme.my_farm["fields"][3]
    champ["content"] = "POTATO"
    champ["needed_water"] = 0

    ferme._commands.clear()

    ferme.stocker(ouvrier, tracteur)

    assert ferme._commands == [f"{ouvrier} STOCKER {champ['location'][-1]} {tracteur}"]


def test_no_stock():
    ferme = Ferme("Ferme_1")
    ferme.my_farm = copy.deepcopy(my_farm_de_base)
    ouvrier = ferme.my_farm["employees"][7]["id"]
    tracteur = ferme.my_farm["tracteur"][1]
    champ = ferme.my_farm["fields"][1]
    champ["needed_water"] = 10

    ferme._commands.clear()

    ferme.stocker(ouvrier, tracteur)

    assert ferme._commands == []


def test_stocker_2():
    ferme = Ferme("Ferme_1")
    ferme.my_farm = copy.deepcopy(my_farm_de_base)
    ouvrier = ferme.my_farm["employees"][7]["id"]
    tracteur = ferme.my_farm["tracteur"][1]
    champ = ferme.my_farm["fields"][3]
    champ["needed_water"]

    ferme._commands.clear()

    ferme.stocker(ouvrier, tracteur)

    assert ferme._commands == []


# TESTS STOCKAGE PAR LES OUVRIERS


def test_ouvrier_en_cours_de_stockage_True():

    ferme = Ferme("Ferme_1")
    ferme.my_farm = copy.deepcopy(my_farm_de_base)
    ouvrier = ferme.my_farm["employees"][7]["id"]

    ferme._commands.clear()

    if ferme.ouvrier_en_cours_de_stockage(ouvrier) == True:
        assert True


def test_ouvrier_en_cours_de_stockage_False():

    ferme = Ferme("Ferme_1")
    ferme.my_farm = copy.deepcopy(my_farm_de_base)
    ouvrier = ferme.my_farm["employees"][7]["id"]

    ferme._commands.clear()

    if ferme.ouvrier_en_cours_de_stockage(ouvrier) == False:
        assert True


def test_detection_fin_stockage():
    ferme = Ferme("Ferme_1")
    ferme.my_farm = copy.deepcopy(my_farm_de_base)

    ferme.detection_fin_stockage

    assert ferme.champs_en_cours_de_stockage[2] == False
    assert ferme.ouvrier_stockage_par_champ[2] == -1


# TEST CUISINE DE SOUPE


def test_cuisiner_5legumes_location():
    ferme = Ferme("Ferme_1")
    ferme.my_farm = copy.deepcopy(my_farm_de_base)
    ouvrier = ferme.my_farm["employees"][7]["id"]

    ferme.cuisiner_5legumes(ouvrier)

    ferme._commands.clear()

    assert ferme._commands == []


def test_cuisinier_5legumes_stock():
    ferme = Ferme("Ferme_1")
    ferme.my_farm = copy.deepcopy(my_farm_de_base)

    ouvrier = ferme.my_farm["employees"][7]["id"]

    # ferme.my_farm["soup_factory"]["stock"][1] == 1

    ferme._commands.clear()

    ferme.cuisiner_5legumes(ouvrier)

    # assert ferme._commands == [f"{ouvrier} CUISINER"]
    # TODO:
