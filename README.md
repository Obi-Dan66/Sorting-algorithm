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

data model.jpg obsahuje tabulky se čtyřmi základními entitami Klient, Transakce, Účet a Balance. Dále obsahuje vedlejší entitu Typ transakce.
Každý atribut má i doporučený datový typ, popřípadě poznámku zda je vhodné u atributu využít funkci NULL.

Tabulka Klient - atributy (client_id(PK), first_name, last_name, client_adress, phone_number, client_email)\
Tabulka Účet - atributy (account_id(PK), account_type, client_id(FK-ref tab Klient,1-N), account_opening_day, account_status, account_balance)\
Tabulka Transakce - atributy (transaction_id(PK), transaction_date, account_id(FK-ref tab Účet, 1-N), transaction_type(FK-ref tab Typ transakce,1-1), transaction_amount, transaction description)\
Tabulka Balance - atributy (record_id(PK), account_id(FK-ref tab Účet, 1-1), principal_amount, interest_amount, fees_amount)\
Tabulka Typ transakce - atributy (transaction_type(PK), type_name)

### Druhá část: SQL queries

> Postavte dotaz, který vybere všechny klienty (např. id_klient, jméno a příjmení) pro něž bude platit, že\
> suma jistin všech jejich účtů na konci měsíce bude větší než číslo c.

SELECT Klient.cliet_id, Klient.first_name, Klient.last_name\
FROM Klient\
INNER JOIN Účet ON Klient.client_id = Účet.client_id\
INNER JOIN (\
  SELECT account_id, SUM(principal_amount) AS sum_principal_amount\
  FROM Balance\
  WHERE record_date = LAST_DAY(CURRENT_DATE)\
  GROUP BY account_id\
)
AS month_balance ON Účet.account_id = month_balance.account_id\
WHERE month_balance.sum_principal_amount > c;

> Postavte dotaz, který zobrazí 10 klientů s maximální celkovou výší pohledávky (suma všech pohledávek klienta)\
> k ultimu měsíce a tuto na konci řádku vždy zobrazte.

SELECT Klient.cliet_id, Klient.first_name, Klient.last_name,\
SUM(Balance.principal_amount + Balance.interest_amount + Balance.fees_amount)\
AS total_amount\
FROM Klient\
INNER JOIN Účet ON Klient.client_id = Účet.client_id\
INNER JOIN Balance ON Účet.account_id = Balance.account_id\
WHERE Balance.record_date = LAST_DAY(CURRENT_DATE)\
GROUP BY Klient.client_id\
ORDER BY total_amount DESC\
LIMIT 10;