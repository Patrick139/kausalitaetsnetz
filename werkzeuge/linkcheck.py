#!/usr/bin/env python3
"""
linkcheck.py — prüft alle Quellen-Links in kausalitaetsnetz.json

Prüft Knotenquellen (nodes[].src) und Kantenquellen (links[].src).
Jede Adresse wird einmal abgerufen, mit 1 s Pause zwischen zwei Abrufen
bei derselben Website.

Einstufung:
  OK        Seite antwortet
  FEHLT     404/410, oder Umleitung auf Start-/Suchseite bzw. "Seite nicht gefunden"
  GESPERRT  401/403/429/451 — die Seite blockt Skripte; im Browser prüfen,
            zählt nicht als Fehler (viele Seiten sperren Rechenzentren)
  FEHLER    andere HTTP-Fehler oder keine Verbindung

Aufruf:  python3 werkzeuge/linkcheck.py [--json ausgabe.json] [--md bericht.md]
Rückgabewert: 1, wenn mindestens ein Link FEHLT, sonst 0.
Nur Standardbibliothek, keine Abhängigkeiten.
"""
import argparse, collections, concurrent.futures, html, json, os, re, sys, time
import urllib.error, urllib.parse, urllib.request

HIER = os.path.dirname(os.path.abspath(__file__))
DATEN = os.path.join(HIER, "..", "kausalitaetsnetz.json")
UA = "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0"


def sammeln(daten):
    """Liefert [(art, id, beschreibung, url)] für alle Quellen."""
    out = []
    for n in daten["nodes"]:
        src = n.get("src") or []
        for u in (src if isinstance(src, list) else [src]):
            out.append(("Knoten", n["id"], (n.get("short") or {}).get("de", ""), u))
    for l in daten["links"]:
        src = l.get("src") or []
        for u in (src if isinstance(src, list) else [src]):
            out.append(("Kante", f'{l["source"]} → {l["target"]}', "", u))
    return out


def pruefen(url):
    req = urllib.request.Request(url, headers={
        "User-Agent": UA, "Accept-Language": "de,en;q=0.8",
        "Accept": "text/html,application/xhtml+xml,application/pdf;q=0.9,*/*;q=0.8"})
    try:
        with urllib.request.urlopen(req, timeout=25) as r:
            ziel = r.geturl()
            roh = r.read(300_000).decode("utf-8", "replace")
            m = re.search(r"<title[^>]*>(.*?)</title>", roh, re.S | re.I)
            titel = html.unescape(re.sub(r"\s+", " ", m.group(1))).strip()[:140] if m else ""
            pfad = urllib.parse.urlparse(ziel).path.strip("/")
            alt = urllib.parse.urlparse(url).path.strip("/")
            weich = (alt and not pfad) \
                or re.search(r"(^|/)(404|not-found|notfound|search|suche)(/|$)", pfad, re.I) \
                or re.search(r"(page not found|seite nicht gefunden|content not found|^404\b)", titel, re.I)
            if weich:
                return "FEHLT", r.status, ziel, titel
            return "OK", r.status, ziel, titel
    except urllib.error.HTTPError as e:
        if e.code in (404, 410):
            return "FEHLT", e.code, url, ""
        if e.code in (401, 403, 429, 451):
            return "GESPERRT", e.code, url, ""
        return "FEHLER", e.code, url, ""
    except Exception as e:  # Zeitüberschreitung, DNS, TLS …
        return "FEHLER", 0, url, str(e)[:120]


def je_website(urls):
    erg = {}
    for i, u in enumerate(urls):
        if i:
            time.sleep(1.0)
        erg[u] = pruefen(u)
    return erg


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", help="Ergebnis als JSON schreiben")
    ap.add_argument("--md", help="Bericht als Markdown schreiben")
    ap.add_argument("--daten", default=DATEN, help="andere Datendatei prüfen (Standard: kausalitaetsnetz.json)")
    a = ap.parse_args()

    daten = json.load(open(a.daten, encoding="utf-8"))
    eintraege = sammeln(daten)
    eindeutig = sorted({e[3] for e in eintraege})
    sites = collections.defaultdict(list)
    for u in eindeutig:
        sites[urllib.parse.urlparse(u).netloc].append(u)

    print(f"{len(eindeutig)} Links auf {len(sites)} Websites …", flush=True)
    erg = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as ex:
        for teil in ex.map(je_website, sites.values()):
            erg.update(teil)

    zahl = collections.Counter(v[0] for v in erg.values())
    print("Ergebnis: " + ", ".join(f"{k} {n}" for k, n in zahl.most_common()))

    tot = [(art, eid, kurz, u, *erg[u]) for art, eid, kurz, u in eintraege if erg[u][0] == "FEHLT"]
    fehler = [(art, eid, kurz, u, *erg[u]) for art, eid, kurz, u in eintraege if erg[u][0] == "FEHLER"]

    if a.json:
        json.dump({"zusammenfassung": dict(zahl),
                   "ergebnisse": [{"art": art, "id": eid, "url": u, "status": erg[u][0], "code": erg[u][1],
                                   "ziel": erg[u][2], "titel": erg[u][3]} for art, eid, kurz, u in eintraege]},
                  open(a.json, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    if a.md:
        z = [f"Linkprüfung vom {time.strftime('%d.%m.%Y')}: " + ", ".join(f"{k} {n}" for k, n in zahl.most_common()), ""]
        if tot:
            z += ["### Tote Links", "", "| Art | Knoten/Kante | Code | URL | Ziel/Titel |", "|---|---|---|---|---|"]
            for art, eid, kurz, u, st, code, ziel, titel in tot:
                info = (titel + (f" → {ziel}" if ziel != u else "")).replace("|", "/")
                z.append(f"| {art} | `{eid}` {kurz} | {code} | {u} | {info} |")
            z.append("")
        if fehler:
            z += ["### Nicht erreichbar (evtl. vorübergehend)", ""]
            z += [f"- `{eid}` — {u} ({code} {ziel if ziel != u else ''})" for art, eid, kurz, u, st, code, ziel, titel in fehler]
            z.append("")
        z += ["Gesperrte Seiten (401/403/429) blocken automatische Abrufe und zählen nicht als Fehler.",
              "Für tote Links gibt es auf der Seite einen Archiv-Link (archive.org) als Rückfall."]
        open(a.md, "w", encoding="utf-8").write("\n".join(z) + "\n")

    for art, eid, kurz, u, st, code, ziel, titel in tot:
        print(f"FEHLT  {eid}: {u}")
    sys.exit(1 if tot else 0)


if __name__ == "__main__":
    main()
