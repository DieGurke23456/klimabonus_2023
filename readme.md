# Klimabonus Auswertung 2023 

Hier findet man mehrere Scripts, mit denen man verschiedene Visualisierungen erstellen kann, die die Einstufung einzelner Gemeinden in eine Klimabonus-Kategorie dem Wahlverhalten dieser Gemeinde bei den Nationalratswahlen 2019 gegenüberstellt. 

### Resourcen 
## plz_klima.json 
gefunden auf https://www.klimabonus.gv.at/assets/json/2023-05-30-plz.json, bietet Informationen über Postleitzahlen und die zugehörige Klimabonus-Kategorie

## nrwahl.json 

gefunden auf https://www.data.gv.at/katalog/dataset/ergebnisse-der-nationalratswahl-2019-aviso#resources

## scraper.py

Erstellt eine Datei plz.json, die Namen von Gemeinden Postleitzahlen zuordnet. 

## merge_election.py

Kombiniert die Informationen aus plz.json, plz_klima.json und nrwahl.json in eine Datei, nrwahl_plz.json 

### Visualisierungen

## klimabonus_average.py

Berrechnet den Mittelwert des Erhaltenen Klimabonus nach Stimmabgabe in der NR-Wahl 2019 und erstellt ein Balkendiagram.

## klimabonus_bar.py
Erstellt 4 Verteilungskurven für die Verschiedenen Kategorien und Partein

## klimabonus_bar_split.py

Wie klimabonus_bar.py, nur nach Partei aufgeteilt

## klimabonus_pie_precentages.py

Erstellt 4 Tortendiagramme, die Aufteilung der Klimabonuskategoiren nach Wahlverhalten zeigen.



