# 🔍 FINN Job Scout & Match Analyst

An automated Python tool for scouting developer job listings on **FINN.no**, extracting structured Schema.org JSON-LD data, and calculating candidate match percentage.

---

## 🚀 Features

- **Automated Web Scraping:** Queries FINN.no search endpoints for developer positions (Fullstack, Frontend, Android, Kotlin, React, TypeScript).
- **Schema.org JSON-LD Parser:** Extracts rich structured metadata (job title, company, location, application deadline, full job description) directly from embedded JSON-LD scripts to minimize token usage.
- **Smart Filtering:** Automatically excludes senior, lead, and executive roles requiring 5+ years of experience.
- **Weighted Skill Matcher:** Calculates a percentage match score based on candidate core tech stack (Kotlin, React, Next.js, TypeScript, SQL, Firebase, Agile).
- **Automated Report Generation:** Exports a sorted Markdown report with job links, deadlines, match scores, and tailored company hooks.

---

## 🛠️ Tech Stack & Architecture

- **Language:** Python 3 (Built with pure standard library: `urllib`, `json`, `re`, `pathlib`, `datetime`). Zero external dependencies required!
- **Data Storage:** Local JSON Database & Markdown Report output.

---

## 📦 How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/markusingierd/finn-job-scout.git
   cd finn-job-scout
   ```

2. **Scout for new job listings:**
   ```bash
   python3 finn_scout.py
   ```
   *Fetches new developer job postings from FINN.no and updates the database.*

3. **Analyze and calculate match score:**
   ```bash
   python3 job_analyst.py
   ```
   *Evaluates all jobs against candidate skills and generates a sorted Markdown report.*

---

## 📄 License
MIT License
