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
- Dockerized for easy setup and portability

---

## 📦 Installation

Clone the repository:

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

## 🧩 Assumptions

Reflection detection uses simple substring matching (not full DOM parsing).

Scanner inspects raw HTTP responses only.

At least 3 contexts supported: attribute name, attribute value, text node.

Payloads are randomized slightly to bypass naive filters.

## 🛠️ PayloadGenerator Logic

Attribute name → <tag PAYLOAD=123>

Attribute value → <tag attr="PAYLOAD">

Text node → <tag>PAYLOAD</tag>

Payloads vary depending on injection position, ensuring coverage of multiple contexts.

## Reflection Detection Approach

Scanner sends requests with generated payloads.

Checks if payload string appears in the response body.

Reports context, parameter, and payload if reflected.

## Design Choices

Modular design: PayloadGenerator class + Scanner class.

Clear separation of payload generation and scanning logic.

Docker support for containerized execution.

Readable, maintainable code structure with comments for clarity.
