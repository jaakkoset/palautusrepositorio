
class IntJoukko:
    OLETUSPITUUS = 5
    OLETUSKASVATUSKOKO = 5


    def __init__(self, pituus=OLETUSPITUUS, kasvatuskoko=OLETUSKASVATUSKOKO):
        self._validate_init(pituus, kasvatuskoko)

        self.pituus = pituus
        self.kasvatuskoko = kasvatuskoko

        self.lista = self._luo_lista(self.pituus)

        self.alkioiden_lkm = 0


    def _validate_init(self, pituus, kasvatuskoko):
        if not isinstance(pituus, int):
            raise TypeError("Pituuden täytyy olla kokonaisluku")
        if pituus < 0:
            raise ValueError("Pituus ei saa olla alle nolla")
        if not isinstance(kasvatuskoko, int):
            raise TypeError("Kasvatuskoon täytyy olla kokonaisluku")
        if kasvatuskoko < 0:
            raise ValueError("Kasvatuskoko ei saa olla alle nolla")


    # tämä metodi on ainoa tapa luoda listoja
    def _luo_lista(self, pituus):
        self.pituus = pituus
        return [0] * pituus


    def kuuluu(self, luku):
        if luku in self.lista:
            return True
        return False


    def lisaa(self, luku):
        if not self.kuuluu(luku):
            self.lista[self.alkioiden_lkm] = luku
            self.alkioiden_lkm = self.alkioiden_lkm + 1

            # ei mahdu enempää, luodaan uusi säilytyspaikka luvuille
            if self.alkioiden_lkm >= self.pituus:
                self._kasvata_listaa()

            return True

        return False


    def _kasvata_listaa(self):
        vanha_lista = self.lista
        self.lista = self._luo_lista(self.alkioiden_lkm + self.kasvatuskoko)
        self._kopioi_lista(self.lista, vanha_lista)


    def poista(self, luku):
        for i in range(self.alkioiden_lkm):
            if self.lista[i] == luku:
                kohta = i  # siis luku löytyy tuosta kohdasta :D
                self.lista[i] = 0
                self._siirra_alkoita_vasemmalle(kohta)
                self.alkioiden_lkm = self.alkioiden_lkm - 1

                return True

        return False


    def _siirra_alkoita_vasemmalle(self, kohta):
        for j in range(kohta, self.alkioiden_lkm - 1):
            self.lista[j] = self.lista[j + 1]

    def _kopioi_lista(self, kopio_lista, vanha_lista):
        """Siirtää vanhan listan sisällön uuteen listaan"""
        vanha_pituus = len(vanha_lista)
        for i in range(vanha_pituus):
            kopio_lista[i] = vanha_lista[i]

    def mahtavuus(self):
        return self.alkioiden_lkm


    def to_int_list(self):
        return self.lista[:self.alkioiden_lkm]


    @staticmethod
    def yhdiste(a, b):
        yhdiste = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for alkio in a_taulu:
            yhdiste.lisaa(alkio)

        for alkio in b_taulu:
            yhdiste.lisaa(alkio)

        return yhdiste


    @staticmethod
    def leikkaus(a, b):
        leikkaus = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for alkio in a_taulu:
            if alkio in b_taulu:
                leikkaus.lisaa(alkio)

        return leikkaus


    @staticmethod
    def erotus(a, b):
        erotus = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for alkio in a_taulu:
            if not alkio in b_taulu:
                erotus.lisaa(alkio)

        return erotus


    def __str__(self):
        tulos = ""
        if self.alkioiden_lkm > 0:
            alkiot = self.to_int_list()
            viimeinen_alkio = alkiot[-1]
            for alkio in alkiot:
                tulos += str(alkio)
                if alkio != viimeinen_alkio:
                    tulos += ", "

        return "{" + tulos + "}"
