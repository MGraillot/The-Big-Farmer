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
                self.add_command("0 EMPRUNTER 100000")
                self.add_command("0 ACHETER_CHAMP")
                self.add_command("0 ACHETER_CHAMP")
                self.add_command("0 ACHETER_CHAMP")
                self.add_command("0 ACHETER_CHAMP")
                self.add_command("0 ACHETER_CHAMP")
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
                self.add_command("1 SEMER TOMATE 1")
                self.add_command("2 SEMER POIREAU 2")
                self.add_command("3 SEMER PATATE 3")
                self.add_command("4 SEMER OIGNON 4")
                self.add_command("5 SEMER COURGETTE 5")
                self.add_command("8 CUISINER")

            self.arroser(1, 1)
            self.arroser(2, 2)
            self.arroser(3, 3)
            self.arroser(4, 4)
            self.arroser(5, 5)

            # self.semer_stock(1, 1, "TOMATE")
            # self.semer_stock(2, 2, "POIREAU")
            # self.semer_stock(3, 3, "PATATE")
            # self.semer_stock(4, 4, "OIGNON")
            # self.semer_stock(5, 5, "COURGETTE")

            self.detection_fin_stockage()
            self.stocker(6, 1)
            self.stocker(7, 2)
            self.cuisiner(8)
            self.send_commands()

    def arroser(self: "PlayerGameClient", ouvrier, champs):
        if self.my_farm["fields"][champs - 1]["needed_water"] != 0:
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
        if self.my_farm["fields"][champs - 1]["content"] == "NONE":
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

    def cuisiner(self: "PlayerGameClient", ouvrier):
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
