from chronobio.game.location import Location


class Tractor:
    def __init__(self: "Tractor", id: int) -> None:
        self.location = Location.FARM
        self.id = id

    def state(self: "Tractor") -> dict:
        return {
            "location": self.location.name,
            "id": self.id,
        }

    def __repr__(self: "Tractor") -> str:
        return f"Tractor(id={self.id}, location={self.location.name})"
