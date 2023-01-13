import argparse
from typing import NoReturn

from chronobio.network.client import Client


class PlayerGameClient(Client):
    def __init__(
        self: "PlayerGameClient", server_addr: str, port: int
    ) -> None:
        super().__init__(server_addr, port, "THE_BIG_FARMER", spectator=False)
        self._commands: list[str] = []
        self.date_vente: list[int] = [-100, -100, -100, -100, -100]
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
                #self.add_command("0 EMPRUNTER 100000")
                self.add_command("1 ACHETER_CHAMP")
                self.add_command("2 ACHETER_CHAMP")
                self.add_command("3 ACHETER_CHAMP")
                self.add_command("4 ACHETER_CHAMP")
                self.add_command("5 ACHETER_CHAMP")
                #self.add_command("0 ACHETER_TRACTEUR")
                self.add_command("1 EMPLOYER")
                self.add_command("2 EMPLOYER")
                self.add_command("3 EMPLOYER")
                self.add_command("4 EMPLOYER")
                self.add_command("5 EMPLOYER")
                self.add_command("1 SEMER TOMATE 1")
                self.add_command("2 SEMER POIREAU 2")
                self.add_command("3 SEMER PATATE 3")
                self.add_command("4 SEMER OIGNON 4")
                self.add_command("5 SEMER COURGETTE 5")
            
            self.arroser(1, 1)
            self.vendre(1)
            self.semer(1, 1, "TOMATE")

            self.arroser(2, 2)
            self.vendre(2)
            self.semer(2, 2, "POIREAU")

            self.arroser(3, 3)
            self.vendre(3)
            self.semer(3, 3, "PATATE")

            self.arroser(4, 4)
            self.vendre(4)
            self.semer(4, 4, "OIGNON")
            
            self.arroser(5, 5)
            self.vendre(5)
            self.semer(5, 5, "COURGETTE")
            self.send_commands()

    def arroser(self: "PlayerGameClient", ouvrier, champs):
        if self.my_farm["fields"][champs-1]["needed_water"] != 0:
            self.add_command(f"{ouvrier} ARROSER {champs}")

    def vendre(self: "PlayerGameClient", champs):
        champs_en_cours_de_vente = False
        for index in range(5):
            if self.game_data["day"] <= self.date_vente[index] + 2:
                champs_en_cours_de_vente = True 
                break

        if self.my_farm["fields"][champs-1]["content"] != "NONE" and not champs_en_cours_de_vente and self.my_farm["fields"][champs-1]["needed_water"] == 0 :
            self.add_command(f"0 VENDRE {champs}")
            self.date_vente[champs-1] = self.game_data["day"]

    def semer(self: "PlayerGameClient", ouvrier, champs, legume):
        if self.game_data["day"] == self.date_vente[champs-1] + 2:
            self.add_command(f"{ouvrier} SEMER {legume} {champs}")

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
