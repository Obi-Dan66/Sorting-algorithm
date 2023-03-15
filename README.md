# hiring-task-epptec

## 1. Zadání
Algoritmus

Napište algoritmus, který ze seznamu vytřídí prvky podle nějakých pravidel,
včetně příkladu takového pravidla. Tzn. ať je tam sekce, kam se doplní konkrétní pravidla,
prvky budou někde mimo v seznamu, který algoritmus projde a smaže hodnoty, které neprošly pravidly.
Prosíme uvést následně instrukci jak spustit a kde najdeme algoritmus.

### Řešení

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


## 2. Zadání

### Datový model

### První část: ER diagram

> Vytvořte jednoduchý datový model obsahující 4 základní entity: Klient, Účet, Transakce a Balance.
>
> Naznačte základní sadu atributů v jednotlivých tabulkách, kardinalitu, primární/cizí klíče, apod.
>
> V tabulce transakcí se bude vyskytovat TYP_TRANSAKCE, který bude odkazovat do číselníku typů transakcí.
>
> Předpokládejte, že tabulka BALANCE obsahuje denní snímky nesoucí informaci o výši jednotlivých komponent pohledávky (jistina, úrok, poplatky) na konci dne.

První část v souboru data model.jpg v tomto repozitáři.

Komentář:

data model.jpg obsahuje tabulky se čtyřmi základními entitami Klient, Transakce, Účet a Balance. Dále obsahuje vedlejší entitu Typ transakce a Produkt. Každý atribut má i doporučený datový typ, popřípadě poznámku zda je vhodné u atributu využít funkci NULL.

### Druhá část: SQL queries

> Postavte dotaz, který vybere všechny klienty (např. id_klient, jméno a příjmení) pro něž bude platit, že\
> suma jistin všech jejich účtů na konci měsíce bude větší než číslo c.

SELECT k.client_id, k.first_name, k.last_name\
FROM Klient k\
JOIN (\
  SELECT client_id, SUM(principal_amount) as sum_b\
  FROM Klient k\
  JOIN Účet u on k.client_id = u.account_id\
  JOIN Produkt p on p.produkt_id = u.account_id\
  JOIN Balance b on b.record_id = p.product_id\
  WHERE DAY (record_date) = DAY(LAST_DATE(CURRENT_DATE))\
  GROUP BY client_id\
  HAVING SUM(principal_amount) > c\
) sums\
ON k.client_id = sums.client_id\
;

> Postavte dotaz, který zobrazí 10 klientů s maximální celkovou výší pohledávky (suma všech pohledávek klienta)\
> k ultimu měsíce a tuto na konci řádku vždy zobrazte.

SELECT k.first_name, k.last_name, sum_b\
FROM Klient k\
JOIN (JOIN\
  SELECT client_id, SUM(balance_amount) as sum_b\
  FROM Klient k\
  JOIN Účet u on k.client_id = u.account_id\
  JOIN Produkt p on p.produkt_id = u.account_id\
  JOIN Balance b on b.record_id = p.product_id\
  WHERE DAY (record_date) = DAY(LAST_DATE(CURRENT_DATE))\
  GROUP BY client_id\
) sums\
ON k.client_id = sums.client_id\
ORDER BY sum_b DESC\
LIMIT 10\
;