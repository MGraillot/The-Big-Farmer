import argparse
from typing import NoReturn

from chronobio.network.client import Client


class PlayerGameClient(Client):
    def __init__(self: "PlayerGameClient", server_addr: str, port: int) -> None:
        super().__init__(server_addr, port, "THE_BIG_FARMER", spectator=False)
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

    def run(self: "PlayerGameClient") -> NoReturn:

        while True:
            self.game_data = self.read_json()
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
<<<<<<< HEAD
                self.add_command("8 CUISINER")
                self.add_command("9 CUISINER")

            self.arroser(1, 1)
            self.arroser(2, 2)
            self.arroser(3, 3)
            self.arroser(4, 4)
            self.arroser(5, 5)

=======
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
            
>>>>>>> 9f1865b8b92efcf5ef6926b9844098ccb3205586
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
            self.send_commands()

            for champs in range(5):
                self.contenance_des_champs[champs] = self.my_farm["fields"][champs][
                    "content"
                ]

    def arroser_localisation(self: "PlayerGameClient", ouvrier, champs):
        if self.my_farm["fields"][champs - 1]["needed_water"] != 0:
            for employe in self.my_farm["employees"]:
                if (
                    employe["id"] == ouvrier
                    and employe["location"] == f"FIELD{champs}"
                ):
                    self.add_command(f"{ouvrier} ARROSER {champs}")

    def vendre(self: "PlayerGameClient", champs):
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

    def semer_vente(self: "PlayerGameClient", ouvrier, champs, legume):
        if self.game_data["day"] == self.date_vente[champs - 1] + 2:
            self.add_command(f"{ouvrier} SEMER {legume} {champs}")

    def semer_stock(self: "PlayerGameClient", ouvrier, champs, legume):

        if (
            self.my_farm["fields"][champs - 1]["content"] == "NONE"
            and self.contenance_des_champs[champs - 1] != "NONE"
        ):
            self.add_command(f"{ouvrier} SEMER {legume} {champs}")

    def stocker(self: "PlayerGameClient", ouvrier, tracteur):
        print(self.ouvrier_stockage_par_champ)
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

    def ouvrier_en_cours_de_stockage(self: "PlayerGameClient", ouvrier):
        for ouvrier_stockage in self.ouvrier_stockage_par_champ:
            if ouvrier_stockage == ouvrier:
                return True
        return False

    def detection_fin_stockage(self: "PlayerGameClient"):
        for numero_champ in range(5):
            id_ouvrier_en_deplacement = self.ouvrier_stockage_par_champ[numero_champ]
            for employe in self.my_farm["employees"]:
                if (
                    employe["id"] == id_ouvrier_en_deplacement
                    and employe["location"] == "SOUP_FACTORY"
                ):
                    self.champs_en_cours_de_stockage[numero_champ] = False
                    self.ouvrier_stockage_par_champ[numero_champ] = -1

    def cuisine_tout(self: "PlayerGameClient", ouvrier):
        for employe in self.my_farm["employees"]:
            if employe["id"] == ouvrier and employe["location"] != "SOUP_FACTORY":
                return
        self.add_command(f"{ouvrier} CUISINER")

    def cuisiner_5legumes(self: "PlayerGameClient", ouvrier):
        for employe in self.my_farm["employees"]:
            if employe["id"] == ouvrier and employe["location"] != "SOUP_FACTORY":
                return

        for legume in ("POTATO", "LEEK", "TOMATO", "ONION", "ZUCCHINI"):
            if self.my_farm["soup_factory"]["stock"][legume] == 0:
                return
        self.add_command(f"{ouvrier} CUISINER")

    def add_command(self: "PlayerGameClient", command: str) -> None:
        self._commands.append(command)

    def send_commands(self: "PlayerGameClient") -> None:
        data = {"commands": self._commands}
        print("sending", data)
        self.send_json(data)
        self._commands.clear()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Game client.")
    parser.add_argument(
        "-a",
        "--address",
        type=str,
        help="name of server on the network",
        default="localhost",
    )
    parser.add_argument(
        "-p",
        "--port",
        type=int,
        help="location where server listens",
        default=16210,
    )

    args = parser.parse_args()

    client = PlayerGameClient(args.address, args.port).run()
