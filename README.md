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

## Designprinzipien

Diese Prinzipien sind verbindlich — wer beiträgt, wer Code ändert, wer Daten ergänzt, hält sich daran. Sie kommen vor jedem Feature, jeder Funktion, jedem schicken Detail.

### 1. Kompromisslos frustfrei

Das Tool soll so unterhaltsam sein, dass Menschen freiwillig Geschichte und Zusammenhänge lernen. **Null Frust** ist das Designziel — keine Sackgassen, keine ins Leere klickenden Buttons, keine "geht nicht"-Erlebnisse. Wenn ein Feature den User frustriert, wird es umgebaut oder entfernt. Wenn ein Klick kein hilfreiches Ergebnis liefert, ist der Klick falsch designt.

### 2. Multiperspektivität & Objektivität

**Geschichte hat keine objektive Erzählung, aber faktische Genauigkeit ist nicht verhandelbar.** Wir bemühen uns aktiv um:

- **Mehrere Perspektiven:** Ein Ereignis kann in mehreren Regionen relevant sein. Westliche Brille vermeiden — was für die USA "War on Terror" war, war für China Aufstieg, für Afrika weitgehend irrelevant.
- **Faktische Sprache:** Akteur + Handlung. Keine PR-Frames übernehmen ("Liberation Day", "Operation X"). Keine moralisierenden Adjektive ("schrecklich", "brutal", "tragisch"). Der Leser bewertet selbst.
- **Quellen-Diversität:** Tier-1-Quellen sollten nicht nur Reuters/BBC/AFP sein. Al Jazeera (mit Vorbehalt), Nikkei, SCMP, lokale Quellen wo verfügbar.
- **Aktive Lücken-Suche:** Wenn wir merken dass Afrika, Lateinamerika, Südostasien dünn vertreten sind — das ist ein Auftrag zur Recherche, kein Schweigen.

### 3. Eine Wahrheit, viele Beiträger

Das Schema ist klar definiert. Wer beiträgt folgt dem Schema. Diskussion über Schema-Änderungen läuft via Issues — nicht durch ad-hoc-Felder.

---

## Bedienung

| Aktion | Funktion |
|--------|----------|
| **Klick** auf Knoten | Zeigt Ursachen und Folgen im Panel |
| **Hover** über Knoten | Tooltip mit Name & Jahr |
| **Scroll** | Rein-/Rauszoomen — kleine Knoten bekommen Labels |
| **Drag** Hintergrund | Netz verschieben |
| **⇢ Kette** + zwei Klicks | Findet Kausalweg zwischen zwei Ereignissen |
| **Ursachen-/Folgen-Tiefe** im Panel | Mehrstufige Vorfahren/Nachkommen sichtbar machen |
| **★★★ Historisch** | Nur die ~30 wichtigsten Ereignisse |
| **Region-Dropdown** | Nach Bereich filtern |

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
- **100 Links** — Kausale Verbindungen mit Begründung
- **17 Regionen/Bereiche** — von USA bis Südostasien
- **Multilingual-ready** — aktuell Deutsch, Englisch via Pull Request möglich

Geplant: Erweiterung auf 1980–1999 (Kalter Krieg, Mauerfall, Jugoslawien), dann weiter zurück. Stärkere Vertretung außereuropäischer Regionen.

---

## Mitmachen

Das ist ein offenes Projekt. Langfristiges Ziel: ein kollaboratives Kausalitätsnetz der Menschheitsgeschichte — kuratiert, mehrsprachig, erweiterbar. Wikipedia für Zusammenhänge statt für Fakten.

### Schema — Node (Ereignis)

```json
{
  "id":     "irak_2003",
  "yr":     2003,
  "end_yr": null,
  "r":      "usa",
  "imp":    3,
  "short":  { "de": "Irak-Invasion ohne Mandat" },
  "detail": { "de": "USA und UK ohne UN-Mandat. Keine Massenvernichtungswaffen. Folge: IS, Millionen Tote, Destabilisierung einer ganzen Region für Jahrzehnte." },
  "tags":   ["krieg", "geopolitik"],
  "src":    "https://quellenlink.com"
}
```

### Schema — Link (Kausalverbindung)

```json
{
  "source":    "irak_2003",
  "target":    "isis_2014",
  "type":      "direkt",
  "why":       { "de": "IS entstand aus dem Machtvakuum nach dem Irak-Krieg" },
  "certainty": "belegt",
  "src":       "https://quellenlink.com"
}
```

**Wichtig zur Pfeilrichtung:** `source` ist Ursache, `target` ist Folge. Der Pfeil muss zeitlich vorwärts laufen (Source-Jahr ≤ Target-Jahr). Eine Reaktion auf ein Ereignis ist Folge, nicht Ursache.

### Feldwerte

**Wichtigkeit (`imp`):** `3` = historisch (epochal) / `2` = wichtig / `1` = relevant (Kontext)

**Link-Typ (`type`):** `direkt` / `indirekt` / `beschleunigt`

**Sicherheit (`certainty`):** `belegt` (Konsens) / `plausibel` (etablierte Lesart) / `umstritten` (offene Debatte)

### Region-Codes (`r`)

Eigene Codes — Länder und große Kulturen werden nicht in Cluster geworfen. Beispiel: Japan und Südkorea sind eigenständig, nicht "Ostasien". Sammelcodes nur wenn mehrere Länder gleichzeitig betroffen und kein Land Schwerpunkt ist.

**Großmächte / Eigenständige:**
`usa`, `eu`, `uk`, `russland`, `china`, `japan`, `südkorea`, `indien`, `taiwan`, `iran`, `israel`, `türkei`, `saudi`, `brasilien`, `mexiko`, `argentinien`, `ägypten`, `südafrika`, `nigeria`, `indonesien`, `australien`, `kanada`, `ukraine`, `afghanistan`, `syrien`, `vietnam`, ...

**Sammelbegriffe** (nur wenn mehrere Länder gleichzeitig betroffen):
`mittelost`, `südostasien`, `lateinamerika`, `nordafrika`, `subsahara`, `zentralasien`

**Special:**
`oesterreich` (heimischer Schwerpunkt, transparent dokumentiert)
`global` (transnational: COVID, Klimaabkommen, Internet-Plattformen)

Neue Codes können bei Bedarf hinzugefügt werden — bitte als Issue diskutieren.

### Tag-Vocabulary

Tags ergänzen die primäre Region — ein Knoten kann thematisch in mehrere Bereiche fallen ohne dass `r` anders sein muss.

**Themen:**
`politik`, `wirtschaft`, `krieg`, `technologie`, `klima`, `umwelt`, `gesundheit`, `gesellschaft`, `religion`, `kultur`, `energie`, `migration`, `geopolitik`

**Akteur-Typen / Ereignis-Art:**
`staat`, `terror`, `konzern`, `bewegung`, `wahl`, `vertrag`, `gesetz`

**Eigenschaften:**
`katastrophe`, `entdeckung`, `revolution`, `protest`

Eigene Tags erlaubt, aber Standard wird empfohlen für Filter-Konsistenz.

### Sprachregeln

Faktisch, präzise, ohne übernommene Frames.

**Tu:**
- "USA und UK marschieren in Irak ein"
- "Saudi-Arabien tötet Khashoggi im Konsulat"
- "Trump verhängt 145% Zölle auf China"
- "Hamas tötet 1.200 Israelis"

**Vermeide:**
- ~~"Liberation Day" (US-PR-Frame)~~ → "Trump-Zölle April 2025"
- ~~"in 45 Tagen durchgepaukt"~~ → "in 45 Tagen verabschiedet"
- ~~"schreckliches Massaker"~~ → "Massaker mit X Toten"
- ~~"Mord ohne Konsequenz"~~ → "MBS-Verantwortung von CIA bestätigt, keine Sanktionen"

Lebende Personen nur dort namentlich nennen wo sie als Akteur zentral sind.

### Sprachen

Pflichtsprache: **Deutsch** (`de`). Englisch (`en`) und andere optional via Pull Request. Wenn eine Sprache fehlt, fällt das Tool auf `de` zurück.

```json
"short": {
  "de": "Irak-Invasion ohne Mandat",
  "en": "Iraq invasion without mandate"
}
```

### Beitrag einreichen

1. Repository forken
2. `kausalitaetsnetz.json` editieren (oder Issue öffnen wenn keine Git-Kenntnisse)
3. Pull Request stellen — Begründung warum der Knoten/Link relevant ist

---

## Technisch

- **Engine:** D3.js v7 (Force Simulation, BFS Pathfinding, depth-limited Traversal)
- **Daten:** JSON (getrennt von Engine — beliebig erweiterbar)
- **Hosting:** GitHub Pages (kein Server, kein Backend)
- **Abhängigkeiten:** keine außer D3 (CDN)

Die Engine (`index.html`) und die Daten (`kausalitaetsnetz.json`) sind bewusst getrennt. Wer neue Ereignisse beiträgt muss die Engine nie anfassen. Das Region-Dropdown wird beim Laden dynamisch aus den Daten generiert — neue Regionen erscheinen automatisch.

---

## Autoren

Initiiert von **Patrick Valda** (Wien, Mai 2026) — mit Claude (Anthropic) als technischem Co-Autor.

---

*Geschichte ist kein Lehrbuch. Sie ist ein Netz. Zieh den Faden.*
