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

`` git clone git@github.com:Kalpsh00/VipraXssScanner.git ``

`` cd VipraXssScanner ``

##  Requirements
- Docker (must be installed on the system to build and run the scanner)


## Usage (Docker Only)

 🐳 Run with Docker

Build the image:

``docker build -t vipra-xss-scanner . ``

Run the scanner:


`` docker run -it vipra-xss-scanner --url https://example.com --method GET --params q=test ``

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

`` Attribute name → <tag PAYLOAD=123> ``

`` Attribute value → <tag attr="PAYLOAD"> ``

`` Text node → <tag>PAYLOAD</tag> ``

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

## 🛡️ Disclaimer

This tool is intended for **educational and authorized security testing purposes only**.  
Do not use it against systems without explicit permission.

## Screenshots

<img width="1485" height="711" alt="Screenshot 2025-11-24 130228" src="https://github.com/user-attachments/assets/823f3a56-2533-401a-9d32-4602e9980aad" />






