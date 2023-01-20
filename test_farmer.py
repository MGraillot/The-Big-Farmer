# FILE FOR FUNCTION == TEST
# complete with functions and tests

from class_Fonctions import Ferme

# =====================
# Examples
# =====================


def test_arroser_localisation():
    ferme = Ferme("Ferme_1")
    ouvrier = 1
    champs = 1
    ferme._commands.clear()
    ferme.arroser_localisation(ouvrier, champs)
    assert ferme._commands == ("1 ARROSER 1")


def test_arroser_localisation_bis():
    ferme = Ferme("Ferme_1")
    ouvrier = 3
    champs = 2
    ferme._commands.clear()

    ferme.arroser_localisation(ouvrier, champs)

    assert ferme._commands == ("3 ARROSER 2")
