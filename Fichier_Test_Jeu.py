import argparse
from typing import NoReturn

from chronobio.network.client import Client


class PlayerGameClient(Client):
    def __init__(
        self: "PlayerGameClient", server_addr: str, port: int
    ) -> None:
        super().__init__(server_addr, port, "THE_BIG_FARMER", spectator=False)
        self._commands: list[str] = []

    def run(self: "PlayerGameClient") -> NoReturn:
        date_vente = -100000

        while True:
            game_data = self.read_json()
            for farm in game_data["farms"]:
                if farm["name"] == self.username:
                    my_farm = farm
                    break
            else:
                raise ValueError(f"My farm is not found ({self.username})")
            print(my_farm)

            if game_data["day"] == 0:
                #self.add_command("0 EMPRUNTER 100000")
                self.add_command("1 ACHETER_CHAMP")
                #self.add_command("0 ACHETER_TRACTEUR")
                self.add_command("1 EMPLOYER")
                self.add_command("1 SEMER TOMATE 1")
                #self.add_command("3 ARROSER 1")
            

            if my_farm["fields"][0]["needed_water"] != 0:
                self.add_command("1 ARROSER 1")
            elif my_farm["fields"][0]["content"] != "NONE" and game_data["day"] > date_vente + 2 :
                 self.add_command("0 VENDRE 1")
                 date_vente = game_data["day"]

            if game_data["day"] == date_vente + 2:
                self.add_command("1 SEMER TOMATE 1")

            self.send_commands()

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
