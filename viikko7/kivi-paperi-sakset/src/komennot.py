from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly
from kps import KiviPaperiSakset

class Komentotehdas:
    def luo_peli(komento):
        if komento == "a":
            return KPSPelaajaVsPelaaja(KiviPaperiSakset)
        if komento == "b":
            return KPSTekoaly(KiviPaperiSakset)
        if komento == "c":
            return KPSParempiTekoaly(KiviPaperiSakset)

        return None
