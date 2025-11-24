# VipraXssScanner 🔍

VipraXssScanner is a Python-based reflected XSS scanner built as part of a security engineering assignment.  
It detects whether injected payloads are reflected in HTTP responses across multiple contexts, helping identify potential XSS vulnerabilities.

---

## 🚀 Features
- Supports **GET** and **POST** requests
- Payloads generated dynamically by a `PayloadGenerator` class
- Handles at least 3 injection contexts:
  - Attribute name
  - Attribute value
  - Text node
- Reflection detection via substring matching
- Simple terminal/HTML report of reflections

---

## 📦 Installation

Clone the repository:
```bash
git clone git@github.com:Kalpsh00/VipraXssScanner.git
cd VipraXssScanner


## Create a virtual environment:

python3 -m venv venv
source venv/bin/activate

## Install dependencies:

pip install -r requirements.txt

## Usage

Run the scanner:

python main.py --url https://example.com --method GET --params q=test
Options:

--url → Target URL

--method → HTTP method (GET/POST)

--params → Parameters to inject

--report → Output reflection report (HTML or terminal)

## Disclaimer:
This tool is intended for educational and authorized security testing purposes only. Do not use it against systems without explicit permission.
