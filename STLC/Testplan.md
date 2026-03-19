# Testplan – GroceryMate

## 1. Produktanalyse

### Zielsetzung
Ziel ist es, die neuen Funktionen des GroceryMate‑Webshops zu testen und sicherzustellen, dass sie korrekt, stabil und benutzerfreundlich funktionieren.

### Zielnutzergruppe
- Alle Nutzer des Webshops
- Käufer von Lebensmitteln
- Nutzer, die alkoholische Produkte kaufen möchten
- Nutzer, die Bewertungen abgeben möchten

### Hardware- und Software-Spezifikationen
**Hardware:**
- PCs, Laptops, Smartphones, Tablets

**Software:**
- Betriebssysteme: Windows, macOS, Android, iOS
- Browser: Chrome, Firefox, Safari, Edge
- Abhängigkeiten: Backend‑Services, Zahlungsdienste, Session‑Management

### Produktfunktionalität
**Bestehende Funktionen:**
- Produktsuche
- Kategorien
- Warenkorb
- Checkout

**Neue Funktionen:**
1. Bewertungssystem  
2. Altersverifikation  
3. Versandkostenänderung

---

## 2. Teststrategie

### Testumfang (Scope)
**Im Umfang:**
- Bewertungssystem
- Altersverifikation
- Versandkostenlogik
- UI‑Darstellung der neuen Elemente

**Nicht im Umfang:**
- Backend‑Datenbanktests
- Zahlungsabwicklung
- Admin‑Funktionen

### Testarten
- Funktionale Tests
- Regressionstests
- Usability‑Tests
- Sicherheitstests (Basis)
- Performance‑Smoke‑Tests

### Risiken & Gegenmaßnahmen
- **Live‑System** → Daten ändern sich  
  → Tests mehrfach validieren  
- **Keine Testnutzer**  
  → Nutzung öffentlicher Funktionen  
- **Keine API‑Dokumentation**  
  → Fokus auf UI‑Tests

### Testlogistik
- Testmanager – Jane Smith  
- QA Engineer – John Doe  
- QA Engineer – Alice Johnson  
- QA Engineer – Robert Brown  
- UAT – Maria Garcia  

---

## 3. Testziele
- Neue Funktionen arbeiten wie spezifiziert  
- UI ist konsistent und verständlich  
- Versandkosten werden korrekt berechnet  
- Altersverifikation blockiert Minderjährige  
- Bewertungen werden korrekt gespeichert und angezeigt  

---

## 4. Testkriterien

### Aussetzungskriterien
- Kritische Fehler, die Tests blockieren  
- Ausfall der Testumgebung  

### Abnahmekriterien
- 95 % der Testfälle ausgeführt  
- 90 % bestanden  
- Keine offenen kritischen Fehler  
- UAT erfolgreich  

---

## 5. Ressourcenplanung
- QA‑Team  
- Entwicklerteam  
- Endnutzer für UAT  
- Geräte: PC, Laptop, Smartphone  
- Tools: Browser, PyCharm, GitHub  

---

## 6. Testumgebung
- DEV, TEST, ACC, PROD  
- Echte Geräte  
- Browser: Chrome, Firefox, Safari, Edge  

---

## 7. Zeitplan
*(Beispiel aus Vorlage übernommen)*

| Aktivität        | Zeitraum        | Umgebung | Verantwortlich |
|------------------|-----------------|----------|----------------|
| Testplanung      | 01.08 – 05.08   | Alle     | Testmanager    |
| Testfalldesign   | 06.08 – 15.08   | Alle     | QA-Team        |
| Integrationstest | 26.08 – 30.08   | TEST     | QA-Team        |
| Systemtest       | 01.09 – 10.09   | TEST     | QA-Team        |
| Regressionstest  | 11.09 – 15.09   | TEST     | QA-Team        |
| UAT              | 22.09 – 30.09   | ACC      | Endnutzer      |

---

## 8. Test-Deliverables
- Testplan  
- Testfälle  
- Testdaten  
- Testberichte  
- Fehlerberichte  
- UAT‑Freigabe
