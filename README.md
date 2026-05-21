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
      "tags": ["politik", "wahl"]
    }
  ],
  "links": [
    {
      "source": "finanzkrise_2008",
      "target": "trump_2016",
      "type": "indirekt",
      "why": { "de": "..." },
      "certainty": "plausibel"
    }
  ]
}
```

**Wichtigkeit (imp):**
- `4` = Epochal (strukturell weltverändernd)
- `3` = Historisch (wichtiger Wendepunkt)
- `2` = Wichtig (kausal relevant)
- `1` = Relevant (Kontext-Knoten)

**Verbindungstypen:** `direkt`, `indirekt`, `beschleunigt`
**Gewissheit:** `belegt`, `plausibel`, `umstritten`

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
