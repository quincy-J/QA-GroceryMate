# Testdurchführung – GroceryMate

Dieses Dokument enthält die Ergebnisse der Testausführung.

---

# 1. Bewertungssystem

| Testfall | Ergebnis | Kommentar |
|----------|----------|-----------|
| BVA 1 | PASS | |
| BVA 2 | PASS | |
| BVA 3 | PASS | |
| BVA 4 | FAIL | >500 Zeichen akzeptiert |
| EP 1 | PASS | |
| Error 1 | PASS | |
| Error 2 | FAIL | HTML wird akzeptiert |
| UC 1 | PASS | |
| UC 2 | PASS | |
| UC 3 | PASS | Durchschnitt aktualisiert |

---

# 2. Altersverifikation

| Testfall | Ergebnis | Kommentar |
|----------|----------|-----------|
| UC 1 | FAIL | Modal erscheint zu früh |
| EP 1 | PASS | |
| BVA 1 | PASS | |
| BVA 2 | PASS | |
| Error 1 | FAIL | Ungültige Daten akzeptiert |
| UC 2 | FAIL | Falsche Weiterleitung |
| Session | PASS | |

---

# 3. Versandkosten

| Testfall | Ergebnis | Kommentar |
|----------|----------|-----------|
| BVA 1 | PASS | |
| BVA 2 | PASS | |
| BVA 3 | PASS | |
| UC 1 | PASS | |
| Error 1 | FAIL | Versandkosten bleiben bei 0 € |

---

# 4. Warenkorb

| Testfall | Ergebnis | Kommentar |
|----------|----------|-----------|
| UC 1 | FAIL | Warenkorb bleibt gefüllt |