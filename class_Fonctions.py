import argparse
from typing import NoReturn


class Fonctions:
    def __init__(self: "Fonctions", username) -> None:
        self.username = username
        self._commands: list[str] = []
        self.date_vente: list[int] = [-100, -100, -100, -100, -100]
        self.champs_en_cours_de_stockage: list[bool] = [
            False,
            False,
            False,
            False,
            False,
        ]
        self.ouvrier_stockage_par_champ: list[int] = [-1, -1, -1, -1, -1]
        self.contenance_des_champs: list[str] = ["NONE", "NONE", "NONE", "NONE", "NONE"]

    def turn(self: "Fonctions", gamedata):

        self.game_data = gamedata
        for farm in self.game_data["farms"]:
            if farm["name"] == self.username:
                self.my_farm = farm
                break
        else:
            raise ValueError(f"My farm is not found ({self.username})")
        print(self.my_farm)

        if self.game_data["day"] == 0:
            self.add_command("0 EMPRUNTER 40000")
            self.add_command("0 ACHETER_CHAMP")
            self.add_command("0 ACHETER_CHAMP")
            self.add_command("0 ACHETER_CHAMP")
            self.add_command("0 ACHETER_CHAMP")
            self.add_command("0 ACHETER_CHAMP")
            self.add_command("0 ACHETER_TRACTEUR")
            self.add_command("0 ACHETER_TRACTEUR")
            self.add_command("0 ACHETER_TRACTEUR")
            self.add_command("0 EMPLOYER")
            self.add_command("0 EMPLOYER")
            self.add_command("0 EMPLOYER")
            self.add_command("0 EMPLOYER")
            self.add_command("0 EMPLOYER")
            self.add_command("0 EMPLOYER")
            self.add_command("0 EMPLOYER")
            self.add_command("0 EMPLOYER")
            self.add_command("0 EMPLOYER")
            self.add_command("0 EMPLOYER")
            self.add_command("0 EMPLOYER")
            self.add_command("0 EMPLOYER")
            self.add_command("0 EMPLOYER")
            self.add_command("0 EMPLOYER")
            self.add_command("0 EMPLOYER")
            self.add_command("0 EMPLOYER")
            self.add_command("0 EMPLOYER")
            self.add_command("0 EMPLOYER")
            self.add_command("0 EMPLOYER")
            self.add_command("0 EMPLOYER")
            self.add_command("1 SEMER TOMATE 1")
            self.add_command("2 SEMER POIREAU 2")
            self.add_command("3 SEMER PATATE 3")
            self.add_command("4 SEMER OIGNON 4")
            self.add_command("5 SEMER COURGETTE 5")
            self.add_command("6 ARROSER 1")
            self.add_command("7 ARROSER 2")
            self.add_command("8 ARROSER 3")
            self.add_command("9 ARROSER 4")
            self.add_command("10 ARROSER 5")
            self.add_command("17 ARROSER 1")
            self.add_command("18 ARROSER 2")
            self.add_command("19 ARROSER 1")
            self.add_command("11 CUISINER")
            self.add_command("12 CUISINER")
            self.add_command("13 CUISINER")

        if self.game_data["day"] < 896:
            self.arroser_localisation(1, 1)
            self.arroser_localisation(6, 1)
            self.arroser_localisation(17, 1)
            self.arroser_localisation(19, 1)
            self.arroser_localisation(2, 2)
            self.arroser_localisation(7, 2)
            self.arroser_localisation(18, 2)
            self.arroser_localisation(3, 3)
            self.arroser_localisation(8, 3)
            self.arroser_localisation(4, 4)
            self.arroser_localisation(9, 4)
            self.arroser_localisation(5, 5)
            self.arroser_localisation(10, 5)

            self.semer_stock(1, 1, "TOMATE")
            self.semer_stock(2, 2, "POIREAU")
            self.semer_stock(3, 3, "PATATE")
            self.semer_stock(4, 4, "OIGNON")
            self.semer_stock(5, 5, "COURGETTE")

            self.detection_fin_stockage()
            self.stocker(14, 1)
            self.stocker(15, 2)
            self.stocker(16, 3)
            self.cuisiner_5legumes(11)
            self.cuisiner_5legumes(12)
            self.cuisiner_5legumes(13)
            self.cuisine_tout(20)

        if self.game_data["day"] == 896:
            self.licencier_embaucher()

        if self.game_data["day"] > 896:
            self.arroser_localisation(21, 1)
            self.arroser_localisation(26, 1)
            self.arroser_localisation(31, 1)
            self.arroser_localisation(33, 1)
            self.arroser_localisation(22, 2)
            self.arroser_localisation(27, 2)
            self.arroser_localisation(32, 2)
            self.arroser_localisation(23, 3)
            self.arroser_localisation(28, 3)
            self.arroser_localisation(24, 4)
            self.arroser_localisation(29, 4)
            self.arroser_localisation(25, 5)
            self.arroser_localisation(30, 5)

            self.semer_stock(21, 1, "TOMATE")
            self.semer_stock(22, 2, "POIREAU")
            self.semer_stock(23, 3, "PATATE")
            self.semer_stock(24, 4, "OIGNON")
            self.semer_stock(25, 5, "COURGETTE")

            self.detection_fin_stockage()
            self.stocker(34, 1)
            self.stocker(35, 2)
            self.stocker(36, 3)
            self.cuisiner_5legumes(37)
            self.cuisiner_5legumes(38)
            self.cuisiner_5legumes(39)
            self.cuisine_tout(40)

        for champs in range(5):
            self.contenance_des_champs[champs] = self.my_farm["fields"][champs][
                "content"
            ]

    def arroser_localisation(self: "Fonctions", ouvrier, champs):
        if self.my_farm["fields"][champs - 1]["needed_water"] != 0:
            for employe in self.my_farm["employees"]:
                if employe["id"] == ouvrier and employe["location"] == f"FIELD{champs}":
                    self.add_command(f"{ouvrier} ARROSER {champs}")

    def vendre(self: "Fonctions", champs):
        champs_en_cours_de_vente = False
        for index in range(5):
            if self.game_data["day"] <= self.date_vente[index] + 2:
                champs_en_cours_de_vente = True
                break

        if (
            self.my_farm["fields"][champs - 1]["content"] != "NONE"
            and not champs_en_cours_de_vente
            and self.my_farm["fields"][champs - 1]["needed_water"] == 0
        ):
            self.add_command(f"0 VENDRE {champs}")
            self.date_vente[champs - 1] = self.game_data["day"]

    def semer_vente(self: "Fonctions", ouvrier, champs, legume):
        if self.game_data["day"] == self.date_vente[champs - 1] + 2:
            self.add_command(f"{ouvrier} SEMER {legume} {champs}")

    def semer_stock(self: "Fonctions", ouvrier, champs, legume):

        if (
            self.my_farm["fields"][champs - 1]["content"] == "NONE"
            and self.contenance_des_champs[champs - 1] != "NONE"
        ):
            self.add_command(f"{ouvrier} SEMER {legume} {champs}")

    def stocker(self: "Fonctions", ouvrier, tracteur):
        print(self.ouvrier_stockage_par_champ)
        print(self.champs_en_cours_de_stockage)
        if self.ouvrier_en_cours_de_stockage(ouvrier):
            return
        for champ in reversed(range(5)):
            if (
                self.my_farm["fields"][champ]["needed_water"] == 0
                and self.my_farm["fields"][champ]["content"] != "NONE"
                and not self.champs_en_cours_de_stockage[champ]
            ):
                self.add_command(f"{ouvrier} STOCKER {champ+1} {tracteur}")
                self.champs_en_cours_de_stockage[champ] = True
                self.ouvrier_stockage_par_champ[champ] = ouvrier
                break

    def ouvrier_en_cours_de_stockage(self: "Fonctions", ouvrier):
        for ouvrier_stockage in self.ouvrier_stockage_par_champ:
            if ouvrier_stockage == ouvrier:
                return True
        return False

    def detection_fin_stockage(self: "Fonctions"):
        for numero_champ in range(5):
            id_ouvrier_en_deplacement = self.ouvrier_stockage_par_champ[numero_champ]
            for employe in self.my_farm["employees"]:
                if (
                    employe["id"] == id_ouvrier_en_deplacement
                    and employe["location"] == "SOUP_FACTORY"
                ):
                    self.champs_en_cours_de_stockage[numero_champ] = False
                    self.ouvrier_stockage_par_champ[numero_champ] = -1

    def cuisine_tout(self: "Fonctions", ouvrier):
        for employe in self.my_farm["employees"]:
            if employe["id"] == ouvrier and employe["location"] != "SOUP_FACTORY":
                return
        self.add_command(f"{ouvrier} CUISINER")

    def cuisiner_5legumes(self: "Fonctions", ouvrier):
        for employe in self.my_farm["employees"]:
            if employe["id"] == ouvrier and employe["location"] != "SOUP_FACTORY":
                return

        for legume in ("POTATO", "LEEK", "TOMATO", "ONION", "ZUCCHINI"):
            if self.my_farm["soup_factory"]["stock"][legume] == 0:
                return
        self.add_command(f"{ouvrier} CUISINER")

    def licencier_embaucher(self: "Fonctions"):
        for employe in range(20):
            self.add_command(f"0 LICENCIER {employe+1}")
            self.add_command("0 EMPLOYER")
        for numero_champ in range(5):
            if self.my_farm["fields"][numero_champ]["content"] != "NONE":
                self.add_command(f"{21+numero_champ} ARROSER {1 + numero_champ}")
            else:
                self.add_command(f"{21+numero_champ} SEMER PATATE {1 + numero_champ}")
        self.add_command("26 ARROSER 1")
        self.add_command("27 ARROSER 2")
        self.add_command("28 ARROSER 3")
        self.add_command("29 ARROSER 4")
        self.add_command("30 ARROSER 5")
        self.add_command("31 ARROSER 1")
        self.add_command("32 ARROSER 2")
        self.add_command("33 ARROSER 1")
        self.add_command("37 CUISINER")
        self.add_command("38 CUISINER")
        self.add_command("39 CUISINER")
        self.add_command("40 CUISINER")
        self.champs_en_cours_de_stockage = [
            False,
            False,
            False,
            False,
            False,
        ]
        self.ouvrier_stockage_par_champ = [-1, -1, -1, -1, -1]

    def add_command(self: "Fonctions", command: str) -> None:
        self._commands.append(command)