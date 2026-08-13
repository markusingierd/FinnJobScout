# 🔍 FinnJobScout

**FinnJobScout** er en automatisert multi-agent pipeline som skanner FINN.no for relevante IT- og utviklerstillinger, beregner match-skår mot en masterprofil, og strukturerer data for å forenkle skriving av skreddersydde jobbsøknader.

---

## 🚀 Funksjoner

* 📊 **FINN Job Scout (`finn_scout.py`)**: Henter og parser strukturert JSON-LD-data direkte fra FINN.no-annonser (Oslo og omegn).
* 🧠 **Match Analyst (`job_analyst.py`)**: Analyserer stillingstekster mot utvalgte ferdigheter (Kotlin, React, Next.js, TypeScript, Python, AI-agenter, databaser, drift m.m.) og beregner match-prosent.
* 💡 **FINN-Forankret Vipps-Krok**: Genererer forslag til uformelle, treffsikre åpningssetninger for søknadsbrev forankret i bedriftens egen annonsetekst.
* 🛡️ **Automatisk Dublettsjekk**: Skanner mappen `soknadsbrev/` og merker stillinger du har skrevet søknad til som `✅ Søkt`, slik at du aldri søker på samme FINN-annonse to ganger.

---

## 🛠️ Forutsetninger

* **Python 3.9+** (Bruker kun standardbiblioteker som `json`, `re`, `urllib`, `datetime` og `pathlib`).
* Ingen eksterne `pip`-pakker nødvendig.

---

## 💻 Slik kjører du prosjektet

### 1. Hent ferske stillinger fra FINN.no
Kjør scout-skriptet for å søke etter nye stillinger og oppdatere den lokale stillingsdatabasen (`relevante_stillinger_database.json`):

```bash
python3 finn_scout.py
```

### 2. Analyser stillinger og generer rapport
Kjør analyst-skriptet for å beregne match-skår, hente ut team-innsikt og generere en oppdatert markdown-rapport (`relevante_stillinger.md`):

```bash
python3 job_analyst.py
```

---

## 📂 Filstruktur

```
FinnJobScout/
├── finn_scout.py                      # Web-scraper for FINN.no
├── job_analyst.py                     # Analyse- og scoringmotor
├── relevante_stillinger_database.json # Lokalt datalager for alle skannede stillinger
├── relevante_stillinger.md            # Generert rapport (sortert etter Match %)
├── .gitignore                         # Ekskluderer personopplysninger og midlertidige filer
└── README.md                          # Prosjektdokumentasjon
```

*(Merk: Personlig CV, masterprofil og søknadsbrev oppbevares kun lokalt på maskinen og publiseres ikke til offentlig versjonskontroll).*

---

## 📄 Lisens
MIT License.
