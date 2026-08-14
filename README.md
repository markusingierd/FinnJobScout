# 🔍 FinnJobScout

**FinnJobScout** er en automatisert multi-agent pipeline som skanner FINN.no for relevante IT- og utviklerstillinger, beregner match-skår mot en masterprofil, og strukturerer data for å forenkle skriving av skreddersydde jobbsøknader.

---

## 🚀 Funksjoner

* 📊 **FINN Job Scout (`finn_scout.py`)**: Henter og parser strukturert JSON-LD-data direkte fra FINN.no-annonser (Oslo og omegn).
* 🧠 **Match Analyst (`job_analyst.py`)**: Analyserer stillingstekster mot utvalgte ferdigheter (Kotlin, React, Next.js, TypeScript, Python, AI-agenter, databaser, drift m.m.) og beregner match-prosent.
* 💡 **FINN-Forankret Vipps-Krok**: Genererer forslag til uformelle, treffsikre åpningssetninger for søknadsbrev forankret i bedriftens egen annonsetekst.
* 🛡️ **Automatisk Dublettsjekk**: Skanner mappen `soknadsbrev/` og merker stillinger du har skrevet søknad til som `✅ Søkt`, slik at du aldri søker på samme FINN-annonse to ganger.
* 🤖 **Application Expert Agent (`.agents/skills/application_expert/`)**: Spesialtilpasset agentkonfigurasjon for å generere naturlige, engasjerende søknadsbrev (Vipps-formelen, aldersriktig uformell tone på 23 år, korte setninger, null konsulentspråk).
* 📄 **DOCX Mal-generering**: Mulighet for automatisk konvertering av ferdige søknader til formatert Word-dokument (`.docx`) basert på din mal.
* 🔒 **100% Anonymisert & Privatsikret**: Kode og skripter er helt uavhengige av personlige opplysninger. Alt av CV-er, masterprofiler, søknadsbrev og private opplysninger er avskjermet fra Git via `.gitignore`.

---

## ⚙️ Slik tilpasser du prosjektet til din egen profil

Prosjektet er universelt bygget og fungerer for hvem som helst som søker IT- og utviklerjobber:

1. **Kopier profilmalen:**
   Kopier malfilen i `user_profile/`-mappen for å lage din egen private profil:
   ```bash
   cp user_profile/master_profile.template.md user_profile/master_profile.md
   ```
2. **Fyll inn dine opplysninger:**
   Åpne `user_profile/master_profile.md` og legg inn ditt navn, nøkkelkompetanse og erfaringer.
3. **Privat og trygt:**
   Mappen `user_profile/` og `.gitignore`-reglene gjør at dine private opplysninger (`master_profile.md`), søknader (`soknadsbrev/`) og CV-er **aldri blir committet eller publisert til Git/GitHub**.

---

## 🛠️ Forutsetninger

* **Python 3.9+** (Bruker standardbiblioteker som `json`, `re`, `urllib`, `datetime`, `pathlib`).
* **Valgfri utvidelse:** `python-docx` for generering av `.docx`-søknadsbrev fra mal:
  ```bash
  pip install python-docx
  ```

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
├── user_profile/                      # Profilmappe for bruker
│   └── master_profile.template.md     # Offentlig mal for ny bruker
├── .agents/skills/application_expert/ # Agent-konfigurasjon og språkskille
├── Mal-søknadsbrev.docx               # Mal for Word-søknadsbrev
├── relevante_stillinger_database.json # Lokalt datalager for alle skannede stillinger
├── relevante_stillinger.md            # Generert rapport (sortert etter Match %)
├── .gitignore                         # Ekskluderer personopplysninger og konfidensielle filer
└── README.md                          # Prosjektdokumentasjon
```

*(Merk: Personlig CV, masterprofil og søknadsbrev oppbevares kun lokalt på maskinen din og skjules 100 % fra versjonskontroll).*

---

## 📄 Lisens
MIT License.
