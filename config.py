import os
BASE_DIR = os.getcwd()

UNIV_LINK_AR = "https://www.mesrs.dz/ar/universites"
UNIV_LINK_FR = "https://www.mesrs.dz/fr/universites"

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