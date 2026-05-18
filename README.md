# Kausal*netz* — Weltgeschichte als navigierbares Ursachen-Netz

**🌐 Live:** [patrick139.github.io/kausalitaetsnetz](https://patrick139.github.io/kausalitaetsnetz/)

---

## Was ist das?

Geschichte wird meistens falsch präsentiert: chronologisch, vollständig, neutral, trocken. Schule. Lehrbuch. Wikipedia.

Das ist das falsche Format für das falsche Medium.

Dieses Tool zeigt Geschichte als das was sie ist: **ein Netz von Ursachen und Folgen.** Kein Ereignis existiert isoliert. Der Irak-Krieg 2003 und Trump 2016 hängen zusammen. Die Finanzkrise 2008 und der Brexit 2016 hängen zusammen. Das soll man hier sehen, verstehen, nachverfolgen können.

Klick auf ein Ereignis. Sieh was dazu geführt hat. Sieh was es ausgelöst hat. Zieh den Faden durch die Jahrzehnte.

---

## Warum?

Es gibt immer mehr Wissen — aber der Kopf des Menschen bleibt klein. Niemand überblickt mehr die Komplexität der modernen Weltgeschichte, egal wie gebildet. Kausalketten die 30 Jahre umspannen passen in kein Schulbuch und in keinen Kopf gleichzeitig.

Wikipedia löst das für Fakten. Dieses Tool löst es für **Kausalität**.

---

## Wie benutzen?

| Aktion | Funktion |
|--------|----------|
| **Klick** auf Knoten | Zeigt Ursachen und Folgen im Panel |
| **Scroll** | Rein-/Rauszoomen |
| **Drag** Hintergrund | Netz verschieben |
| **⇢ Kette** + zwei Klicks | Findet Kausalweg zwischen zwei Ereignissen |
| **★★★ Historisch** | Nur die ~30 wichtigsten Ereignisse — guter Einstieg |

### Linien-Bedeutung
- 🔴 **Rot** — Direkte Ursache: A hat B unmittelbar ausgelöst
- 🟡 **Gelb** — Indirekte Folge: A hat Bedingungen für B geschaffen
- 🔵 **Blau** — Beschleunigt: A hat B schneller oder stärker gemacht

### Knoten-Größe
- **Groß** (glühend) — Historisch: epochales Ereignis
- **Mittel** — Wichtig: bedeutendes Ereignis
- **Klein** — Relevant: Kontext und Hintergrund

---

## Aktueller Stand

- **79 Knoten** — Ereignisse 2000–2026
- **101 Links** — Kausale Verbindungen mit Begründung
- **9 Regionen** — USA, Europa, Russland, China, Nahost, Global, Tech, Klima, Österreich
- **8 Epochen** — von Post-Cold-War bis Trump 2.0

Geplant: Erweiterung auf 1980–1999 (Kalter Krieg, Mauerfall, Jugoslawien), dann weiter zurück.

---

## Mitmachen

Das ist ein offenes Projekt. Langfristiges Ziel: ein kollaboratives Kausalitätsnetz der Menschheitsgeschichte — kuratiert, mehrsprachig, erweiterbar. Wikipedia für Zusammenhänge statt für Fakten.

### Neue Ereignisse vorschlagen

Die Daten leben in [`kausalitaetsnetz.json`](kausalitaetsnetz.json). Jeder Eintrag folgt diesem Format:

**Node (Ereignis):**
```json
{
  "id":        "ereignis_2003",
  "epoch":     "war_on_terror",
  "sub_epoch": "iraq",
  "yr":        2003,
  "end_yr":    null,
  "r":         "welt",
  "imp":       3,
  "short":     "Kurzer Name (max. 5-6 Wörter)",
  "detail":    "2-3 Sätze. Was ist passiert, warum wichtig.",
  "src":       "https://quellenlink.com",
  "tags":      ["geopolitik", "krieg"]
}
```

**Link (Verbindung):**
```json
{
  "source":    "ereignis_2003",
  "target":    "folge_2014",
  "type":      "direkt",
  "why":       "Ein Satz: WARUM ist das kausal?",
  "yr":        2014,
  "src":       "https://quellenlink.com",
  "certainty": "belegt"
}
```

**Wichtigkeitsgrade (`imp`):** `3` = historisch / `2` = wichtig / `1` = relevant

**Verbindungstypen (`type`):** `direkt` / `indirekt` / `beschleunigt`

**Sicherheitsgrad (`certainty`):** `belegt` / `plausibel` / `umstritten`

### Beitrag einreichen

1. Repository forken
2. `kausalitaetsnetz.json` editieren
3. Pull Request stellen

Oder: Issue öffnen mit dem Vorschlag, wenn kein GitHub-Kenntnisse vorhanden.

---

## Technisch

- **Engine:** D3.js v7 (Force Simulation, BFS Pathfinding)
- **Daten:** JSON (getrennt von Engine — beliebig erweiterbar)
- **Hosting:** GitHub Pages (kein Server, kein Backend)
- **Abhängigkeiten:** keine außer D3 (CDN)

Die Engine (`index.html`) und die Daten (`kausalitaetsnetz.json`) sind bewusst getrennt. Wer neue Ereignisse beiträgt muss die Engine nie anfassen.

---

## Autoren

Initiiert von **Patrick Valda** (Wien, Mai 2026) — mit Claude (Anthropic) als technischem Co-Autor.

---

*Geschichte ist kein Lehrbuch. Sie ist ein Netz. Zieh den Faden.*
