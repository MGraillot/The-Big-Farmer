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
        {"id": 1, "location": "FIELD1"},
        {"id": 2, "location": "FIELD1"},
        {"id": 3, "location": "FIELD1"},
        {"id": 4, "location": "FIELD1"},
        {"id": 5, "location": "FIELD1"},
        {"id": 6, "location": "FIELD1"},
        {"id": 1, "location": "FIELD2"},
        {"id": 2, "location": "FIELD2"},
        {"id": 3, "location": "FIELD2"},
        {"id": 4, "location": "FIELD2"},
        {"id": 5, "location": "FIELD2"},
    ],
}


def test_arroser_localisation():
    ferme = Ferme("Ferme_1")
    ferme.my_farm = copy.deepcopy(my_farm_de_base)
    ferme.my_farm["fields"][2]["needed_water"] = 5
    ferme.my_farm["employees"][3]["id"] = 4
    ouvrier = 3
    champs = 2

    ferme._commands.clear()

    ferme.arroser_localisation(ouvrier, champs)

    assert ferme._commands == ["3 ARROSER 2"]


def test_arroser_localisation_bis():
    ferme = Ferme("Ferme_1")
    ferme.my_farm = {
        "fields": [
            {"needed_water": 10},
            {"needed_water": 10},
            {"needed_water": 10},
            {"needed_water": 10},
            {"needed_water": 10},
        ],
        "employees": [
            {"id": 1, "location": "FIELD1"},
            {"id": 2, "location": "FIELD1"},
            {"id": 3, "location": "FIELD1"},
            {"id": 4, "location": "FIELD1"},
            {"id": 5, "location": "FIELD1"},
            {"id": 6, "location": "FIELD1"},
            {"id": 1, "location": "FIELD2"},
            {"id": 2, "location": "FIELD2"},
            {"id": 3, "location": "FIELD2"},
            {"id": 4, "location": "FIELD2"},
            {"id": 5, "location": "FIELD2"},
        ],
    }
    ouvrier = 6
    champs = 1
    ferme._commands.clear()

    ferme.arroser_localisation(ouvrier, champs)

    assert ferme._commands == ["6 ARROSER 1"]
