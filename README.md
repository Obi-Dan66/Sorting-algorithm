# hiring-task-epptec

## Zadání
Algoritmus\
Napište algoritmus, který ze seznamu vytřídí prvky podle nějakých pravidel,
včetně příkladu takového pravidla. Tzn. ať je tam sekce, kam se doplní konkrétní pravidla,
prvky budou někde mimo v seznamu, který algoritmus projde a smaže hodnoty, které neprošly pravidly.
Prosíme uvést následně instrukci jak spustit a kde najdeme algoritmus.

## Řešení

### Specifikace vstupních dat:

Jméno zaměstnance, tým, odpracované hodiny (za měsíc), odpracované hodiny na klientských projektech (za měsíc), email,
dvoufaktorová autentizace povolena.

### Případová studie:

a) Chceme vymazat uživatele, kteří mají větší než 50% utilizaci, aby jsme sledovali efektivitu jednotlivců.

b) Dále nás zajímá, kteří uživatelé používají dvoufaktorovou autentizaci, abychom zajistili větší bezpečnost interního systému.

### Implementace:

Průchod neseřazeným polem, kde při nalezení neodpovídajícího elementu, element odstraníme a pokračujeme v iteraci. Program příjímá první
argument typu boolean a druhý argument značící pravidlo. Pokud je první argument nastavený na 'True' tak se vstupní soubor modifikuje,
dle příslušných pravidel. Pokud je nastavený na 'False' tak pouze vypíše na standartní výstup. Druhý argument určuje pravidlo k selekci.

### Dostupné možnosti spuštění:

python main.py True utilization - vymaže všechny uživatele ze vstupního souboru, kteří mají utilizaci vyšší než 50%\
python main.py True 2fa - vymaže všechny uživatele ze vstupního souboru, kteří mají povolené dvoufázové ověření\
python main.py False utilization - vypíše všechny uživatele, kteří mají utilizaci nižší než 50%\
python main.py False 2fa - vypíše všechny uživatele, kteří nemají povolené dvoufázové ověření