# Testplan – GroceryMate

## 1. Produktanalyse

### Zielsetzung
Ziel ist es, die neuen Funktionen des GroceryMate‑Webshops zu testen und sicherzustellen, dass sie korrekt, stabil und benutzerfreundlich funktionieren.

### Zielnutzergruppe
- Alle Nutzer des Webshops  
- Käufer von Lebensmitteln  
- Nutzer, die alkoholische Produkte kaufen möchten  
- Nutzer, die zukünftig Bewertungen abgeben möchten  

### Hardware- und Software-Spezifikationen
**Hardware:**  
- PCs, Laptops, Smartphones, Tablets  

**Software:**  
- Betriebssysteme: Windows, macOS, Android, iOS  
- Browser: Chrome, Firefox, Safari, Edge  
- Abhängigkeiten: Backend‑Services, Session‑Management  

### Produktfunktionalität
**Bestehende Funktionen:**  
- Produktsuche  
- Kategorien  
- Warenkorb  
- Produktdetails  
- Favoriten  
- Checkout (nicht vollständig implementiert, kein Kaufabschluss möglich)

**Neue Funktionen:**  
1. Bewertungssystem (noch nicht implementiert)  
2. Altersverifikation  
3. Versandkostenregelung (20 € Schwellenwert)

---

## 2. Teststrategie

### Testumfang (Scope)
**Im Umfang:**  
- Bewertungssystem (Testfalldesign, Durchführung = N/A)  
- Altersverifikation  
- Versandkostenlogik  
- UI‑Darstellung der neuen Elemente  

**Nicht im Umfang:**  
- Kaufabschluss / Zahlungsabwicklung  
- Backend‑Datenbanktests  
- Admin‑Funktionen  

### Testarten
- Funktionale Tests  
- Regressionstests  
- Usability‑Tests  
- Basis‑Sicherheitstests  
- Performance‑Smoke‑Tests  

### Risiken & Gegenmaßnahmen
- **Live‑System** → Daten ändern sich  
  → Tests mehrfach validieren  
- **Bewertungssystem nicht implementiert**  
  → Testfälle erstellen, Durchführung = N/A  
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
- Altersverifikation blockiert Minderjährige  
- Versandkosten werden korrekt berechnet (unter/über 20 €)  
- UI ist konsistent und verständlich  
- Bewertungssystem ist spezifiziert und testbar, sobald implementiert  

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
- Live‑System (öffentliche Demo)  
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
- Anforderungen  
- Testfälle  
- Testdaten  
- Testdurchführung  
- Testreporting  
- Fehlerberichte (GitHub Issues)  
- UAT‑Freigabe
