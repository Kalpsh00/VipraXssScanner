# VipraXssScanner 🔍

VipraXssScanner is a Python-based reflected XSS scanner built as part of a security engineering assignment.  
It detects whether injected payloads are reflected in HTTP responses across multiple contexts, helping identify potential XSS vulnerabilities.



## 🚀 Features
- Supports **GET** and **POST** requests
- Payloads generated dynamically by a `PayloadGenerator` class
- Handles at least 3 injection contexts:
  - Attribute name
  - Attribute value
  - Text node
- Reflection detection via substring matching
- Simple terminal/HTML report of reflections



## 📦 Installation

Clone the repository:
```bash
git clone git@github.com:Kalpsh00/VipraXssScanner.git
cd VipraXssScanner



Disclaimer : This tool is intended for educational and authorized security testing purposes only.  
Do not use it against systems without explicit permission.



