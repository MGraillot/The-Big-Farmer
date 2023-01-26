import logging


class Ferme:
    def __init__(self: "Ferme", username) -> None:
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
        self.trie_des_stock_de_legume: list[int] = [0, 0, 0, 0, 0]
        self.jour_de_catastrophe_climatique: int = 0
        self.id_ouvrier_stockage_climat: list[int] = [-1, -1, -1, -1, -1]

    def turn(self: "Ferme", gamedata):
        """ Find out which field should be watered and send a worker to water it

        args : self: "ferme": call the class "Ferme",

               gamedata : Data from the game (.json file)

        return : Function that allows to send game actions    

        """
        logging.info("turn")
        self.game_data = gamedata
        for farm in self.game_data["farms"]:
            if farm["name"] == self.username:
                self.my_farm = farm
                break
        else:
            raise ValueError(f"My farm is not found ({self.username})")
        print(self.my_farm)
        logging.info("jour %d", self.game_data["day"])
        logging.debug("Block %d", self.my_farm["blocked"])
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
            self.add_command("19 ARROSER 3")
            self.add_command("20 ARROSER 4")
            self.add_command("13 ARROSER 5")
            self.add_command("21 ARROSER 1")
            self.add_command("22 ARROSER 2")
            self.add_command("23 ARROSER 3")
            self.add_command("24 ARROSER 4")
            self.add_command("25 ARROSER 5")
            self.add_command("26 ARROSER 1")
            self.add_command("27 ARROSER 2")
            self.add_command("28 ARROSER 3")
            self.add_command("29 ARROSER 4")
            self.add_command("30 ARROSER 5")
            self.add_command("11 CUISINER")
            self.add_command("12 CUISINER")
            self.add_command("32 CUISINER")
            self.add_command("33 CUISINER")
            self.add_command("31 CUISINER")

        if self.game_data["day"] < 896:
            logging.info("arroser_localisation")
            self.arroser_localisation(1, 1)
            self.arroser_localisation(2, 2)
            self.arroser_localisation(3, 3)
            self.arroser_localisation(4, 4)
            self.arroser_localisation(5, 5)
            self.arroser_localisation(6, 1)
            self.arroser_localisation(7, 2)
            self.arroser_localisation(8, 3)
            self.arroser_localisation(9, 4)
            self.arroser_localisation(10, 5)
            self.arroser_localisation(17, 1)
            self.arroser_localisation(18, 2)
            self.arroser_localisation(19, 3)
            self.arroser_localisation(20, 4)
            self.arroser_localisation(13, 5)
            self.arroser_localisation(21, 1)
            self.arroser_localisation(22, 2)
            self.arroser_localisation(23, 3)
            self.arroser_localisation(24, 4)
            self.arroser_localisation(25, 5)
            self.arroser_localisation(26, 1)
            self.arroser_localisation(27, 2)
            self.arroser_localisation(28, 3)
            self.arroser_localisation(29, 4)
            self.arroser_localisation(30, 5)
            logging.info("detection_climat")
            self.detection_climat()
            logging.info("detection_climat")
            self.semer_stock(1, 1)
            self.semer_stock(2, 2)
            self.semer_stock(3, 3)
            self.semer_stock(4, 4)
            self.semer_stock(5, 5)

            self.detection_fin_stockage()
            self.detection_fin_stockage_climat()
            self.stocker(14, 1)
            self.stocker(15, 2)
            self.stocker(16, 3)

            self.cuisiner_5legumes(11)
            self.cuisiner_5legumes(12)
            self.cuisiner_5legumes(32)
            self.cuisiner_5legumes(33)
            self.cuisiner_5legumes(31)

        if self.game_data["day"] == 896:
            logging.info("licencié_embauché")
            self.licencier_embaucher()

        if self.game_data["day"] > 896:
            logging.info("arroser_localisation")
            self.arroser_localisation(35, 1)
            self.arroser_localisation(36, 2)
            self.arroser_localisation(37, 3)
            self.arroser_localisation(38, 4)
            self.arroser_localisation(39, 5)
            self.arroser_localisation(40, 1)
            self.arroser_localisation(41, 2)
            self.arroser_localisation(42, 3)
            self.arroser_localisation(43, 4)
            self.arroser_localisation(44, 5)
            self.arroser_localisation(45, 1)
            self.arroser_localisation(46, 2)
            self.arroser_localisation(47, 3)
            self.arroser_localisation(48, 4)
            self.arroser_localisation(49, 5)
            self.arroser_localisation(50, 1)
            self.arroser_localisation(51, 2)
            self.arroser_localisation(52, 3)
            self.arroser_localisation(53, 4)
            self.arroser_localisation(54, 5)
            self.arroser_localisation(55, 1)
            self.arroser_localisation(56, 2)
            self.arroser_localisation(57, 3)
            self.arroser_localisation(58, 4)
            self.arroser_localisation(59, 5)

            logging.info("detection_climat")
            self.detection_climat()
            logging.info("detection_climat")

            self.semer_stock(35, 1)
            self.semer_stock(36, 2)
            self.semer_stock(37, 3)
            self.semer_stock(38, 4)
            self.semer_stock(39, 5)

            self.detection_fin_stockage()
            self.detection_fin_stockage_climat()
            self.stocker(60, 1)
            self.stocker(61, 2)
            self.stocker(62, 3)

            self.cuisiner_5legumes(64)
            self.cuisiner_5legumes(65)
            self.cuisiner_5legumes(66)
            self.cuisiner_5legumes(67)
            self.cuisiner_5legumes(63)
            self.cuisiner_5legumes(68)
        logging.debug(self.my_farm["soup_factory"]["stock"])

    def arroser_localisation(self: "Ferme", ouvrier, champs):
        """ Find out which field should be watered and send a worker to water it

        args : self: "ferme": call the class "Ferme",

               ouvrier is the ID of the worker, 

               champs is the ID of the fied

        return : A command for send the worker on the field for water it     

        """
        if self.my_farm["fields"][champs - 1]["needed_water"] != 0:
            for employe in self.my_farm["employees"]:
                if employe["id"] == ouvrier and employe["location"] == f"FIELD{champs}":
                    self.add_command(f"{ouvrier} ARROSER {champs}")

    def vendre(self: "Ferme", champs):
        """ Selling the vegetable from the field 

        args : self: "ferme": call the class "Ferme",

               champs is the ID of the fied

        return : A command for send the maanger on the field for selling the vegetable     

        """
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

    def semer_stock(self: "Ferme", ouvrier, champs):
        """ Find out which field is ready to be sown and send a worker to sow 

        args : self: "ferme": call the class "Ferme",

               ouvrier is the ID of the worker, 

               champs is the ID of the fied

        return : A command for send the worker on the field for sown

        """
        self.trie_des_stock_de_legume = self.my_farm["soup_factory"]["stock"]
        sorted_legume_by_stock = sorted(
            self.trie_des_stock_de_legume.items(), key=lambda x: x[1]
        )
        legume = sorted_legume_by_stock[0][0]
        print(sorted_legume_by_stock)
        print(legume)
        for employe in self.my_farm["employees"]:
            if (
                employe["id"] == ouvrier
                and employe["location"] == f"FIELD{champs}"
                and self.my_farm["fields"][champs - 1]["content"] == "NONE"
            ):

                if legume == ("POTATO"):
                    legume = "PATATE"

                elif legume == ("LEEK"):
                    legume = "POIREAU"

                elif legume == ("ONION"):
                    legume = "OIGNON"

                elif legume == ("TOMATO"):
                    legume = "TOMATE"

                elif legume == ("ZUCCHINI"):
                    legume = "COURGETTE"
                self.add_command(f"{ouvrier} SEMER {legume} {champs}")

    def stocker(self: "Ferme", ouvrier, tracteur):
        """ Find out which field is ready to be harvested and send a worker on a tractor

        args : self: "ferme": call the class "Ferme",

               ouvrier is the ID of the worker, 

               tracteur is the ID of the tractor

        return : A command for send the worker on the field for harvesting

        """
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

    def ouvrier_en_cours_de_stockage(self: "Ferme", ouvrier):
        """ Find out if a worker is harvesting and storing vegetables from the field 

        args : self: "ferme": call the class "Ferme",

               ouvrier is the ID of the worker, 

        return : True if the worker is busy

        """
        for ouvrier_stockage in self.ouvrier_stockage_par_champ:
            if ouvrier_stockage == ouvrier:
                return True
        return False

    def detection_fin_stockage(self: "Ferme"):
        """ Find out if a worker has finished storing the vegetables in the field 

        args : self: "ferme": call the class "Ferme",

        return : False if the worker as done

        """
        for numero_champ in range(5):
            id_ouvrier_en_deplacement = self.ouvrier_stockage_par_champ[numero_champ]
            for employe in self.my_farm["employees"]:
                if (
                    employe["id"] == id_ouvrier_en_deplacement
                    and employe["location"] == "SOUP_FACTORY"
                ):
                    self.champs_en_cours_de_stockage[numero_champ] = False
                    self.ouvrier_stockage_par_champ[numero_champ] = -1

    def cuisiner_5legumes(self: "Ferme", ouvrier):
        """ Requires a cook to cook soups of 5 vegetables

        args : self: "ferme": call the class "Ferme",

               ouvrier is the ID of the worker, 

        return : A command for the cook to cook 
        """
        for employe in self.my_farm["employees"]:
            if employe["id"] == ouvrier and employe["location"] != "SOUP_FACTORY":
                return

        for legume in ("POTATO", "LEEK", "TOMATO", "ONION", "ZUCCHINI"):
            if self.my_farm["soup_factory"]["stock"][legume] == 0:
                return
        self.add_command(f"{ouvrier} CUISINER")

    def licencier_embaucher(self: "Ferme"):
        """ Function to dismiss all workers and rehire new ones

        args : self: "ferme": call the class "Ferme",

        return : New workers

        """
        for employe in range(33):
            self.add_command(f"0 LICENCIER {employe+1}")
            self.add_command("0 EMPLOYER")
        for numero_champ in range(5):
            if self.my_farm["fields"][numero_champ]["content"] != "NONE":
                self.add_command(f"{35+numero_champ} ARROSER {1 + numero_champ}")
            else:
                self.add_command(f"{35+numero_champ} SEMER PATATE {1 + numero_champ}")
        self.add_command("0 EMPLOYER")
        self.add_command("0 EMPLOYER")
        self.add_command("40 ARROSER 1")
        self.add_command("41 ARROSER 2")
        self.add_command("42 ARROSER 3")
        self.add_command("43 ARROSER 4")
        self.add_command("44 ARROSER 5")
        self.add_command("45 ARROSER 1")
        self.add_command("46 ARROSER 2")
        self.add_command("47 ARROSER 3")
        self.add_command("48 ARROSER 4")
        self.add_command("49 ARROSER 5")
        self.add_command("50 ARROSER 1")
        self.add_command("51 ARROSER 2")
        self.add_command("52 ARROSER 3")
        self.add_command("53 ARROSER 4")
        self.add_command("54 ARROSER 5")
        self.add_command("55 ARROSER 1")
        self.add_command("56 ARROSER 2")
        self.add_command("57 ARROSER 3")
        self.add_command("58 ARROSER 4")
        self.add_command("59 ARROSER 5")
        self.add_command("64 CUISINER")
        self.add_command("65 CUISINER")
        self.add_command("66 CUISINER")
        self.add_command("67 CUISINER")
        self.add_command("68 CUISINER")
        self.add_command("63 CUISINER")
        self.champs_en_cours_de_stockage = [
            False,
            False,
            False,
            False,
            False,
        ]
        self.ouvrier_stockage_par_champ = [-1, -1, -1, -1, -1]

    def detection_climat(self: "Ferme"):
        """ Function to detect climatic hazards

        args : self: "ferme": call the class "Ferme",

        return : Action according to these climatic hazards

        """
        logging.info(self.game_data["events"])
        for event in self.game_data["events"]:
            logging.info(event)
            if "fire" in event:
                if event[-1:] != "Y":
                    numero_de_champ = int(event[-1:])
                    self.champs_en_cours_de_stockage[numero_de_champ - 1] = False
                    self.id_ouvrier_stockage_climat[numero_de_champ -
                                                    1] = self.ouvrier_stockage_par_champ[numero_de_champ - 1]
                    logging.info("fire")

            elif "frost" in event or "heat wave" in event:
                logging.info(self.game_data["events"])
                numero_de_champ = int(event[-1:])
                self.champs_en_cours_de_stockage[numero_de_champ - 1] = False
                self.id_ouvrier_stockage_climat[numero_de_champ -
                                                1] = self.ouvrier_stockage_par_champ[numero_de_champ - 1]
                logging.info("frost or heat wave")

    def get_employee_by_id(self: "Ferme", id):
        for employe in self.my_farm["employees"]:
            if employe["id"] == id:
                return employe

    def detection_fin_stockage_climat(self: "Ferme"):
        for champs_index, ouvrier_id in enumerate(self.id_ouvrier_stockage_climat):
            if ouvrier_id == -1:
                continue
            ouvrier = self.get_employee_by_id(ouvrier_id)
            if ouvrier["location"] == "SOUP_FACTORY" or ouvrier["location"] == f"FIELD{champs_index + 1}":
                self.ouvrier_stockage_par_champ[champs_index] = -1

    def add_command(self: "Ferme", command: str) -> None:
        logging.info(command)
        self._commands.append(command)
