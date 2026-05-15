# Selenium – Automatisierte UI‑Tests

Dieses Verzeichnis enthält meine Selenium‑Automatisierungstests aus dem QA‑Training.  
Die Tests sind mit **PyTest + Selenium** geschrieben und folgen einer professionellen Struktur.

---

## 📁 Struktur

- `src/` – optionaler Code (Page Objects)
- `tests/` – alle Testfälle
- `conftest.py` – WebDriver‑Fixture

---

## 🧪 Testfälle

### 1. Login‑Test (saucedemo.com)
- Login durchführen
- Erfolgreiche Anmeldung prüfen

### 2. Produkt in den Warenkorb legen
- Produkt auswählen
- Warenkorb‑Counter prüfen

### 3. Registrierung (automationexercise.com)
- Signup‑Flow automatisieren
- Cookie‑Banner umgehen
- Erfolgreiche Registrierung prüfen

---

## ▶️ Tests ausführen

```bash
pytest -v
``

---

## 🎯 Ziel

Diese Tests demonstrieren:

- UI‑Automatisierung mit Selenium
- XPath‑ und CSS‑Selektoren
- Fixtures und Teststruktur
- Umgang mit dynamischen Elementen
- Professionelle QA‑Arbeitsweise