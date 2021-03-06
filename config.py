import os

BASE_DIR = os.getcwd()

# for universities
UNIV_LINK_AR = "https://www.mesrs.dz/ar/universites"
UNIV_LINK_FR = "https://www.mesrs.dz/fr/universites"

# for national schools
ECOLE_LINK_AR = "https://www.mesrs.dz/ar/ecoles-nationales"
ECOLE_LINK_FR = "https://www.mesrs.dz/fr/ecoles-nationales"

# for teachers national schools
TEACH_LINK_AR = "https://www.mesrs.dz/ar/ecoles-normales"
TEACH_LINK_FR = "https://www.mesrs.dz/fr/ecoles-normales"

# university centers
CENTER_LINK_AR = "https://www.mesrs.dz/ar/centres-universitaires"
CENTER_LINK_FR = "https://www.mesrs.dz/fr/centres-universitaires"

REPLACE_ITEMS = [
    ("technologie", "technology"),
    ("Université", "University"),
    (" et de ", " and "),
    (" et des ", " and "),
    (" des ", " of "),
    (" de ", " of "),
    ("d'", " of "),
    (" et ", " and "),
    (" le ", " "),
    (" la ", " "),
    (" les ", ""),
    (" l'", ""),
    ("è", "e"),
    ("é", "e"),
]
