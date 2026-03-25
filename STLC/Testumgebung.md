# Testumgebung – GroceryMate

Dieses Dokument beschreibt die technische Umgebung, in der die Tests für GroceryMate durchgeführt wurden.  
Ziel ist es, eine reproduzierbare, stabile und nachvollziehbare Testbasis sicherzustellen.

---

# 1. Testsystem

Da GroceryMate ein öffentlich zugängliches Live‑System ist, wurden alle Tests direkt auf der produktiven Umgebung durchgeführt.

**URL:**  
https://grocerymate.masterschool.com/

**Systemcharakteristik:**  
- Öffentliche Demo  
- Kein Login erforderlich  
- Checkout nicht vollständig implementiert  
- Bewertungssystem nicht implementiert  
- Daten können sich jederzeit ändern  

---

# 2. Hardware

Tests wurden auf folgenden Geräten durchgeführt:

| Gerätetyp | Betriebssystem | Bemerkung |
|----------|----------------|-----------|
| Laptop | macOS 15.7.4 | Haupttestgerät |
| Smartphone | iOS 17 | Mobile UI‑Check |

---

# 3. Software / Browser

| Browser | Version | Status |
|---------|---------|--------|
| Chrome | aktuell | Hauptbrowser |
| Safari | macOS/iOS | Mobile & Mac Tests |
| Firefox | aktuell | Cross‑Browser |
| Edge | aktuell | Optional |

---

# 4. Tools & Hilfsmittel

- **PyCharm** – Automatisierung & Python‑Tests  
- **GitHub** – Versionskontrolle & Issues  
- **Draw.io** – Diagramme  
- **Selenium (Python)** – Automatisierung  
- **pytest** – Test Runner  
- **Browser DevTools** – Debugging  

---

# 5. Testdaten

Da das System öffentlich ist, wurden ausschließlich **manuell erzeugte Testdaten** verwendet:

- Produkte aus dem Live‑Shop  
- Mengenvariationen (1, 5, 10, 100, 1e+72)  
- Favoritenstatus  
- Warenkorbwerte (19,99 €, 20 €, >20 €)  
- Keine Accounts notwendig  
- Keine Zahlungsdaten notwendig  

---

# 6. Einschränkungen der Testumgebung

- Checkout nicht funktionsfähig → Bewertungssystem nicht testbar  
- Daten ändern sich dynamisch → Preise & Produkte können variieren  
- Keine API‑Dokumentation → Fokus auf UI‑Tests  
- Keine Möglichkeit, Sessions zu manipulieren → Session‑Tests nur über Browser möglich  

---

# 7. Stabilität & Reproduzierbarkeit

Um reproduzierbare Ergebnisse sicherzustellen:

- Tests mehrfach ausgeführt  
- Browsercache regelmäßig geleert  
- Tests in mehreren Browsern validiert  
- Screenshots bei Fehlern erstellt (GitHub Issues)

---

# 8. Zusammenfassung

Die Testumgebung bildet eine realistische Nutzersituation ab und ermöglicht funktionale Tests der UI‑Elemente, Versandkostenlogik und Altersverifikation.  
Nicht implementierte Funktionen (z. B. Bewertungssystem, Checkout) wurden dokumentiert und als N/A markiert.

---
