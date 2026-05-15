# PyTest – Test Suite

Dieses Verzeichnis enthält alle automatisierten Tests für mein QA‑Portfolio.  
Die Tests sind mit **PyTest** geschrieben und folgen einer klaren, professionellen Struktur.

---

## 📁 Struktur

- `test_count_word_matches.py`  
  Enthält Unit‑Tests für die Funktion `count_word_matches` aus dem `src/`‑Ordner.

---

## 🧪 Ausführung der Tests

Tests können direkt über PyTest ausgeführt werden:

```bash
pytest -v
```

---

## 🧩 Testkonzept

Die Tests decken folgende Bereiche ab:

- **Parametrisierte Tests**  
  Überprüfung verschiedener Eingaben und erwarteter Ergebnisse.

- **Edge Cases**  
  Leere Strings, Groß-/Kleinschreibung, Sonderzeichen.

- **Negative Tests**  
  Ungültige Eingaben, Typfehler, unerwartete Werte.

---

## 🎯 Ziel

Diese Test-Suite demonstriert:

- saubere Teststruktur  
- professionellen Umgang mit PyTest  
- Trennung von Code (`src/`) und Tests (`tests/`)  
- reproduzierbare, automatisierte Tests  

---

## 📌 Hinweis

Alle Tests basieren auf der Funktion `count_word_matches.py` im `src/`‑Ordner.