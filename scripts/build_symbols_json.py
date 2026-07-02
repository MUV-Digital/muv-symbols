#!/usr/bin/env python3
"""
MUV Symbol Library — JSON Builder
Laedt alle SVGs aus dem GitHub-Repo und speichert sie als references/symbols.json.

Aufruf:
    python3 scripts/build_symbols_json.py

Ausgabe:
    references/symbols.json
"""

import urllib.request
import json
import time
import os

SYMBOLS = [
    "absperrklappe","absperrventil","aktivkohlefilter","ausdehnungsgefaess",
    "brandmeldezentrale","brandschutzklappe","brenner","co2-fuehler","dachzentrale",
    "dampfbefeuchter","ddc","dreiwegeventil","druckfuehler","eev","energiezaehler",
    "fbh-verteiler","fcu","feinfilter","feuchtefuehler","feuerloescher","freikuehler",
    "frequenzumrichter","fuellstandsfuehler","gaszaehler","gateway","grobfilter",
    "grundriss","heizkessel","heizkoerper","jalousieklappe","kaeltemittelsammler",
    "kaltwassersatz","kamera","kanalkreuzung","kanaluebergang","klappenantrieb",
    "kreuzstrom-wt","kuehlturm","lufterhitzer","luftkanal","luftkuehler","magnetventil",
    "mischventil","nacherhitzer","oelabscheider","plattenwaermetauscher",
    "praezisionsklimageraet","pufferspeicher","rauchmelder","raum","regelklappe",
    "regelventil","rlt-anlage","rohrleitung","rotor-wrg","rueckschlagklappe",
    "rueckschlagventil","schalldaempfer","schaltschrank","schmutzfaenger",
    "sicherheitsventil","solarkollektor","sprinkler","stellantrieb","stroemungswaechter",
    "switch-router","taschenfilter","temperaturfuehler","tev","trafo","umwaelzpumpe",
    "usv","vav-box","ventilator","ventilator-abluft","ventilator-aussenluft",
    "ventilator-fortluft","ventilator-zuluft","verdampfer","verdichter",
    "verdunstungsbefeuchter","verfluessiger","vrf","waermemengenzaehler","waermepumpe",
    "warmwasserspeicher","wasserzaehler","zonen-overlay","zonenklappen","zugangskontrolle",
    "zuluftanlage"
]

BASE_URL = "https://raw.githubusercontent.com/MUV-Digital/muv-symbols/main/HLKK/svg/{}.svg"

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    out_dir = os.path.join(script_dir, "..", "references")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "symbols.json")

    result = {}
    failed = []

    for name in SYMBOLS:
        url = BASE_URL.format(name)
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "muv-symbol-builder/1.0"})
            with urllib.request.urlopen(req, timeout=10) as r:
                svg = r.read().decode("utf-8")
                result[name] = svg
                print(f"  OK   {name}")
        except Exception as e:
            failed.append(name)
            print(f"  FAIL {name}: {e}")
        time.sleep(0.05)

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f"\n✅  {len(result)} Symbole gespeichert → {out_path}")
    if failed:
        print(f"❌  Fehlgeschlagen ({len(failed)}): {', '.join(failed)}")

if __name__ == "__main__":
    main()
