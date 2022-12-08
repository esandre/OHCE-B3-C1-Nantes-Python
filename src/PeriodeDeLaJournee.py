from enum import Enum


class PeriodeDeLaJournee(Enum):
    DEFAULT = 1  # Quand on ne sait pas à quel moment nous sommes
    MATIN = 2
    APRES_MIDI = 3
    SOIR = 4
    NUIT = 5
