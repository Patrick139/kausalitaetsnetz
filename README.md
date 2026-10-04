# Kausalnetz

Interaktive Visualisierung historischer Kausalzusammenhänge — politisch, wirtschaftlich, gesellschaftlich.

**Live:** https://patrick139.github.io/kausalitaetsnetz/

---

## Copyright & Lizenzen

Copyright © 2026 Patrick Valda

Dieses Projekt ist unter zwei Lizenzen veröffentlicht:

- **Quellcode** (`index.html` und alle Code-Dateien): [GNU AGPL-3.0](LICENSE)
- **Daten** (`kausalitaetsnetz.json` und alle Knoten/Verbindungs-Inhalte): [Creative Commons BY-SA 4.0](LICENSE-DATA)

### Was das bedeutet

**Du darfst:**
- Den Code und die Daten frei nutzen, verändern und weiterverbreiten
- Eigene Forks erstellen
- Das Tool für eigene Zwecke einsetzen

**Du musst:**
- Den ursprünglichen Autor nennen (Patrick Valda)
- Veränderte Versionen unter derselben Lizenz veröffentlichen (Copyleft)
- Bei Web-Anwendungen den Quellcode der modifizierten Version zugänglich machen (AGPL-Klausel)

**Du darfst NICHT:**
- Diese Arbeit als deine eigene ausgeben
- Eine geschlossene (proprietäre) Version vertreiben
- Die Lizenzbedingungen weglassen oder ändern

---

## Schema

Knoten und Links in `kausalitaetsnetz.json`:

```json
{
  "nodes": [
    {
      "id": "trump_2016",
      "yr": 2016,
      "r": "usa",
      "imp": 4,
      "short": { "de": "Trump gewinnt Präsidentschaft" },
      "detail": { "de": "..." },
      "tags": ["politik", "wahl"],
      "src": ["https://…", "https://…"]
    }
  ],
  "links": [
    {
      "source": "finanzkrise_2008",
      "target": "trump_2016",
      "type": "indirekt",
      "why": { "de": "..." },
      "certainty": "plausibel",
      "src": ["https://…"],
      "gegen": { "de": "..." }
    }
  ]
}
```

- `src` (Knoten): Quellen für das **Ereignis** selbst.
- `src` (Kante, optional): Quellen für die **Kausalbehauptung** — also dafür, dass A zu B beigetragen hat, nicht nur dafür, dass A und B stattfanden.
- `gegen` (Kante, optional): die wichtigste belegte Gegenposition zur Kausalbehauptung. Wird im Panel unter der Begründung angezeigt.

**Wichtigkeit (imp):**
- `4` = Epochal (strukturell weltverändernd)
- `3` = Historisch (wichtiger Wendepunkt)
- `2` = Wichtig (kausal relevant)
- `1` = Relevant (Kontext-Knoten)

**Verbindungstypen:** `direkt`, `indirekt`, `beschleunigt`

**Gewissheit (certainty)** — wird im Panel bei jeder Verbindung angezeigt:
- `belegt` = Mindestens eine Quelle beschreibt den Zusammenhang ausdrücklich als Ursache und Wirkung (Fachliteratur, Untersuchungsbericht, Qualitätsmedium), und es gibt keine ernsthafte Gegenposition.
- `plausibel` = Zeitliche Abfolge und ein nachvollziehbarer Mechanismus, aber kein direkter Beleg für den Kausalzusammenhang.
- `umstritten` = Es gibt eine ernsthafte, belegte Gegenposition. Dann ist `gegen` auszufüllen.

**Fakt und Deutung:** `detail` beschreibt zuerst, was geschah (prüfbare Zahlen, Daten, Namen). Wertungen sind erlaubt, sollen aber als Deutung erkennbar sein.

---

## Direktlinks

Jede Ansicht hat eine eigene Adresse; der Knopf „Link kopieren“ im Panel kopiert sie.

- `?node=finanzkrise_2008` — Knoten auswählen
- `&ursachen=2&folgen=3` — Tiefe der angezeigten Ursachen/Folgen (0–5)
- `?von=finanzkrise_2008&nach=trump_2016` — Kausalkette zwischen zwei Knoten
- `&imp=alle` (oder `1`–`4`), `&region=usa`, `&thema=krieg` — Filter

---

## Linkprüfung

`werkzeuge/linkcheck.py` prüft alle Quellen-Links (Knoten und Kanten). Ein GitHub-Ablauf führt die Prüfung am 1. jedes Monats und bei jeder Datenänderung auf `main` aus und legt bei toten Links ein Issue an. Zu jeder Quelle zeigt die Seite außerdem einen Archiv-Link (archive.org) als Rückfall.

---

## Quellenpolitik

- **Tier 1** (immer zitierfähig): Reuters, AP, AFP, BBC, ARD/ZDF, ORF, RFI, FT
- **Tier 2** (mit Kontext): Al Jazeera, SCMP, Nikkei
- **Tier 3** (Faktenbasis ohne Zitat): Regierungs-, Behörden- und Zentralbankquellen, SEC-Filings, Think Tanks

---

## Beitragen

Pull Requests willkommen. Alle Beiträge fallen unter die hier verwendeten Lizenzen (AGPL-3.0 für Code, CC BY-SA 4.0 für Daten). Mit dem Einreichen eines PR bestätigst du, dass du die Rechte an deinem Beitrag hast und ihn unter den Projektlizenzen freigibst.

---

## Werkzeuge

Bei der Entwicklung wurden gängige Werkzeuge eingesetzt: Editor, Versionskontrolle, Browser-Devtools sowie KI-basierte Code-Assistenten. Konzept, Daten-Kuration, redaktionelle Entscheidungen, Sprachregeln und Gesamtarchitektur stammen vom Autor.

---

## Zitieren

```
Valda, Patrick (2026). Kausalnetz – Interaktive Visualisierung
historischer Kausalzusammenhänge. https://github.com/Patrick139/kausalitaetsnetz
```
