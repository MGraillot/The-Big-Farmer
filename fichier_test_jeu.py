import logging
import argparse
from class_Fonctions import Ferme
from typing import NoReturn

from chronobio.network.client import Client


class PlayerGameClient(Client):
    def __init__(self: "PlayerGameClient", server_addr: str, port: int) -> None:
        super().__init__(server_addr, port, "THE BIG FARMER", spectator=False)
        self.fonction = Ferme("THE BIG FARMER")

    def run(self: "PlayerGameClient") -> NoReturn:
        while True:
            self.fonction.turn(self.read_json())
            self.send_commands()

    def send_commands(self: "PlayerGameClient") -> None:
        data = {"commands": self.fonction._commands}
        print("sending", data)
        self.send_json(data)
        self.fonction._commands.clear()


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
    logging.basicConfig(
        filename="THE BIG FARMER.log",
        encoding="utf-8",
        level=logging.DEBUG,
        format="%(asctime)s [%(levelname)-8s] %(filename)20s(%(lineno)3s):%(funcName)-20s :: %(message)s",
        datefmt="%m/%d/%Y %H:%M:%S",
    )
    client = PlayerGameClient(args.address, args.port).run()
