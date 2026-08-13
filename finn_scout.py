#!/usr/bin/env python3
"""
FINN Job Scout
--------------
Scouts and extracts developer job listings from FINN.no (Oslo & region).
Extracts structured JSON-LD (Schema.org / JobPosting) data for minimal token usage
and updates local database storage.
"""

import json
import re
import urllib.request
import urllib.parse
from datetime import datetime
from pathlib import Path

BASE_DIR = Path(__file__).parent.resolve()
DB_FILE = BASE_DIR / "job_listings_database.json"

# Keywords that automatically exclude senior/lead roles
EXCLUDE_KEYWORDS = [
    "senior", "lead", "principal", "direktør", "seksjonsleder", 
    "avdelingsleder", "cto", "arkitekt - senior", "head of"
]

# FINN.no search endpoints for developer roles
FINN_SEARCH_URLS = [
    "https://www.finn.no/job/fulltime/search.html?q=utvikler&location=1.20001.20061",
    "https://www.finn.no/job/fulltime/search.html?q=systemutvikler&location=1.20001.20061",
    "https://www.finn.no/job/fulltime/search.html?q=kotlin&location=1.20001.20061",
    "https://www.finn.no/job/fulltime/search.html?q=react&location=1.20001.20061",
    "https://www.finn.no/job/fulltime/search.html?occupations=0.23"
]

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def load_database():
    if DB_FILE.exists():
        try:
            with open(DB_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"[!] Error reading database: {e}")
    return {}

def save_database(db):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(db, f, ensure_ascii=False, indent=2)
    print(f"[+] Database updated. Total {len(db)} jobs stored.")

def fetch_url(url):
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=10) as response:
            return response.read().decode("utf-8")
    except Exception as e:
        print(f"[!] Error fetching {url}: {e}")
        return None

def extract_job_ids_from_search(html):
    if not html:
        return []
    matches = re.findall(r'/ad/(\d+)', html)
    return list(set(matches))

def fetch_and_parse_ad(ad_id):
    url = f"https://www.finn.no/job/ad/{ad_id}"
    html = fetch_url(url)
    if not html:
        return None

    # Extract JSON-LD (Schema.org JobPosting)
    json_ld_matches = re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.DOTALL)
    
    title = ""
    company = ""
    location = ""
    description = ""
    date_published = "Unknown"
    application_deadline = "Unknown"

    for match in json_ld_matches:
        try:
            data = json.loads(match)
            if isinstance(data, dict) and data.get("@type") == "JobPosting":
                title = data.get("title", "")
                company = data.get("hiringOrganization", {}).get("name", "") if isinstance(data.get("hiringOrganization"), dict) else ""
                loc_data = data.get("jobLocation", {})
                if isinstance(loc_data, dict):
                    addr = loc_data.get("address", {})
                    if isinstance(addr, dict):
                        location = addr.get("addressLocality", "") or addr.get("addressRegion", "")
                elif isinstance(loc_data, list) and len(loc_data) > 0:
                    addr = loc_data[0].get("address", {})
                    if isinstance(addr, dict):
                        location = addr.get("addressLocality", "")
                
                description = data.get("description", "")
                date_published = data.get("datePosted", "Unknown")[:10] if data.get("datePosted") else "Unknown"
                application_deadline = data.get("validThrough", "Unknown")[:10] if data.get("validThrough") else "Unknown"
                break
        except Exception:
            continue

    # Fallback if JSON-LD tag was missing
    if not title:
        title_match = re.search(r'<h1[^>]*>(.*?)</h1>', html, re.DOTALL)
        if title_match:
            title = re.sub(r'<[^>]+>', '', title_match.group(1)).strip()

    # Clean HTML tags from description
    clean_desc = re.sub(r'<[^>]+>', ' ', description)
    clean_desc = re.sub(r'\s+', ' ', clean_desc).strip()

    # Check for exclusion keywords
    status = "new"
    reason = ""
    for kw in EXCLUDE_KEYWORDS:
        if kw in title.lower():
            status = "excluded"
            reason = f"Title contains exclusion keyword '{kw.capitalize()}'"
            break

    today_str = datetime.now().strftime("%Y-%m-%d")

    return {
        "id": str(ad_id),
        "title": title or f"Job {ad_id}",
        "company": company or "Unknown Company",
        "location": location or "Oslo / Region",
        "url": url,
        "status": status,
        "reason": reason,
        "experience_req": "Not specified",
        "date_found": today_str,
        "date_published": date_published,
        "application_deadline": application_deadline,
        "match_percentage": 0,
        "match_analysis": "",
        "description_text": clean_desc
    }

def run_scout():
    print("🔍 Starting FINN Job Scout...")
    db = load_database()

    found_ids = set()
    for search_url in FINN_SEARCH_URLS:
        html = fetch_url(search_url)
        ids = extract_job_ids_from_search(html)
        found_ids.update(ids)

    print(f"📊 Found {len(found_ids)} unique job ID(s) on FINN.")
    
    new_adds = 0
    for ad_id in found_ids:
        if str(ad_id) in db:
            continue
        
        print(f"  -> Fetching job {ad_id}...")
        ad_data = fetch_and_parse_ad(ad_id)
        if ad_data:
            db[str(ad_id)] = ad_data
            new_adds += 1

    save_database(db)
    print(f"✨ Scout completed: {new_adds} new job(s) added to database.")

if __name__ == "__main__":
    run_scout()
