# Task 1: Enhancing Secure Data Exchange with Encoding Formats and Protocol Integration

**Student:** Aayush Kadel (Student ID: 250573)  
**Module:** ST4015CMD — Foundation of Computer Science  
**College:** Softwarica College of IT & E-Commerce (in collaboration with Coventry University)  
**Submitted To:** Rupak Rajbanshi  

---

## Overview

This task investigates the role of encoding formats in secure data exchange across web protocols and modern networks. It evaluates Base64, Hex, URL and ASCII encoding in conjunction with HTTPS, TLS and SMTP, examines their role in injection prevention, explores interoperability with REST APIs and OAuth 2.0, and proposes enhanced encoding strategies.

---

## Files in This Folder

| File | Description |
|------|-------------|
| `images/Fig-1 Encryption Vs Encoding.png` | Difference between encryption and encoding |
| `images/Fig-2 HTTP payload and input validation process.png` | HTTP input-output encoding and authentication pipeline |
| `images/Fig-3 SQL injection.png` | SQL injection risk without input encoding |
| `images/Fig-4 Secure Mail Transfer.png` | Base64 + TLS email transmission data flow |

---

## Report Structure

| Section | Topic |
|---------|-------|
| 1 | Introduction — role of encoding in secure data exchange |
| 2 | Strengths and weaknesses of Base64, Hex, URL and ASCII encoding |
| 3 | Encoding role in HTTP payload security and injection prevention |
| 4 | Interoperability with REST APIs and OAuth 2.0 |
| 5 | Data-flow: Base64 encoding in TLS-based email transmission |
| 6 | Proposed enhanced encoding strategies |
| 7 | Conclusion |

---

## Encoding Formats Summary

| Encoding Format | Primary Use | Key Strength | Key Weakness | Size Impact |
|----------------|-------------|--------------|--------------|-------------|
| Base64 | Binary-to-text (email, tokens) | Universal text compatibility | No confidentiality; trivially decodable | +33% |
| Hex | Debugging, hash display | Precise byte-level readability | Doubles data size; no security | +100% |
| URL Encoding | Query strings, HTTP parameters | Universal browser/server support | Vulnerable to double-encoding attacks | Variable |
| ASCII | Basic text representation, protocol communication | Universal system and protocol compatibility | Limited to 128 characters; no multilingual support | None |

---

## Diagrams

### Fig-1: Comparison between Encryption and Encoding
![Fig-1](images/Fig-1%20Encryption%20Vs%20Encoding.png)

Encryption requires a secret key and produces cipher text. Encoding uses a public scheme and produces encoded data. Both are two-way reversible processes, but only encryption guarantees confidentiality.

---

### Fig-2: HTTP Payload Encoding and Input Validation Process
![Fig-2](images/Fig-2%20HTTP%20payload%20and%20input%20validation%20process.png)

Shows the pipeline from User Input → Input Encoding → Server Validation → Application Processing → Safe Output. URL encoding neutralises malicious characters such as single quotes before they reach the database query parser.

---

### Fig-3: SQL Injection
![Fig-3](images/Fig-3%20SQL%20injection.png)

Illustrates the risk of SQL injection when input encoding and validation are absent. Without encoding, an attacker can inject strings like `' OR '1'='1` directly into the database query.

---

### Fig-4: Secure Email Transmission using Base64 and TLS
![Fig-4](images/Fig-4%20Secure%20Mail%20Transfer.png)

Shows the full data flow: Sender Email Client → Base64 Encoding → SMTP Transmission with TLS → Mail Server → Base64 Decoding → Recipient Client. Base64 handles protocol compatibility; TLS handles confidentiality.

---

## Proposed Enhanced Encoding Strategies

| Strategy | Description |
|----------|-------------|
| Decode Before Inspect | WAFs must fully decode all incoming data before applying security rules to eliminate blind spots |
| Context-Aware Output Encoding | Use Base64url for HTTP headers, URL encoding for query parameters, HTML encoding for browser output |
| Mandatory TLS 1.3 | All encoded data must be transmitted through a TLS 1.3 encrypted tunnel |
| Asymmetric JWT Signing | Use RS256 or ES256 instead of symmetric HMAC to prevent token compromise even if intercepted |

---

## References

1. Forouzan, B. A. (2013) *Data Communications and Networking.*
2. Jones, M., Bradley, J. and Sakimura, N. (2015) JSON Web Token (JWT). RFC 7519. https://datatracker.ietf.org/doc/html/rfc7519
3. OWASP Foundation (2021) Top 10:2021-Injection. https://owasp.org/Top10/A03_2021-Injection/
4. Rescorla, E. (2018) The Transport Layer Security (TLS) Protocol Version 1.3. RFC 8446. https://datatracker.ietf.org/doc/html/rfc8446
5. Stallings, W. (2017) *Cryptography and Network Security: Principles and Practice.*
