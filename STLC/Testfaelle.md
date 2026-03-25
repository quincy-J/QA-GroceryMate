# Testfälle – GroceryMate

Dieses Dokument enthält alle funktionalen Testfälle basierend auf den finalen Anforderungen.  
Jeder Testfall ist einer Testdesign‑Technik zugeordnet.

---

# 1. Bewertungssystem

Da das Bewertungssystem im Live‑System nicht implementiert ist, beziehen sich die Testfälle auf die spezifizierten Anforderungen.

---

## BS‑01 – Bewertung mit 5 Sternen speichern  
**Technik:** Funktionstest  
**Voraussetzung:** Nutzer ist registriert und eingeloggt  

**Schritte:**  
1. Produktseite öffnen  
2. 5 Sterne auswählen  
3. Bewertung speichern  

**Erwartet:**  
- Bewertung wird gespeichert  
- Bewertung erscheint auf der Produktseite  

---

## BS‑02 – Bewertung mit Text (max. 300 Zeichen)  
**Technik:** Äquivalenzklassen (gültige Eingabe)  
**Voraussetzung:** Nutzer ist eingeloggt  

**Schritte:**  
1. Produktseite öffnen  
2. Text mit genau 300 Zeichen eingeben  
3. Bewertung speichern  

**Erwartet:**  
- Bewertung wird gespeichert  
- Text wird korrekt angezeigt  

---

## BS‑03 – Bewertung über 300 Zeichen  
**Technik:** Grenzwertanalyse  
**Voraussetzung:** Nutzer ist eingeloggt  

**Schritte:**  
1. Produktseite öffnen  
2. Text mit 301 Zeichen eingeben  
3. Bewertung speichern  

**Erwartet:**  
- Fehlermeldung: „Feedback darf maximal 300 Zeichen enthalten.“  

---

## BS‑04 – Bewertung bearbeiten  
**Technik:** Use Case Testing  
**Voraussetzung:** Nutzer hat bereits eine Bewertung abgegeben  

**Schritte:**  
1. Bewertung öffnen  
2. Text ändern  
3. Speichern  

**Erwartet:**  
- Bewertung wird aktualisiert  

---

## BS‑05 – Bewertung löschen  
**Technik:** Use Case Testing  
**Voraussetzung:** Nutzer hat bereits eine Bewertung abgegeben  

**Schritte:**  
1. Bewertung öffnen  
2. „Löschen“ klicken  

**Erwartet:**  
- Bewertung wird entfernt  
- Durchschnittswert wird neu berechnet  

---

# 2. Altersverifikation

---

## AV‑01 – Altersmodal erscheint beim ersten Aufruf  
**Technik:** Funktionstest  

**Schritte:**  
1. Kategorie „Alkohol“ öffnen  

**Erwartet:**  
- Altersmodal erscheint  

---

## AV‑02 – Zugriff verweigert bei „Nein“  
**Technik:** Fehlerermessen  

**Schritte:**  
1. Kategorie „Alkohol“ öffnen  
2. „Nein, ich bin nicht 18“ klicken  

**Erwartet:**  
- Kein Zugriff  
- Nutzer bleibt auf vorheriger Seite  

---

## AV‑03 – Zugriff nach Bestätigung  
**Technik:** Funktionstest  

**Schritte:**  
1. Kategorie „Alkohol“ öffnen  
2. „Ich bin 18+“ klicken  

**Erwartet:**  
- Kategorie „Alkohol“ wird angezeigt  

---

## AV‑04 – Session‑Speicherung  
**Technik:** Zustandsbasierter Test  

**Schritte:**  
1. Altersmodal bestätigen  
2. Zur Startseite wechseln  
3. Kategorie „Alkohol“ erneut öffnen  

**Erwartet:**  
- Kein erneutes Modal innerhalb derselben Session  

---

## AV‑05 – Erneute Prüfung beim Checkout  
**Technik:** Use Case Testing  
**Hinweis:** Checkout im Live‑System nicht implementiert → Testdurchführung = N/A  

**Schritte:**  
1. Alkoholisches Produkt in den Warenkorb legen  
2. Checkout öffnen  

**Erwartet:**  
- Altersverifikation wird erneut geprüft  

---

# 3. Versandkosten

Versandkostenregelung laut Anforderung:  
- Unter **20 €** → **4,99 € Versandkosten**  
- Ab **20 €** → **0 € Versandkosten**

---

## VK‑01 – Warenkorb unter 20 €  
**Technik:** Grenzwertanalyse  

**Schritte:**  
1. Produkte im Wert von 19,99 € in den Warenkorb legen  
2. Warenkorb öffnen  

**Erwartet:**  
- Versandkosten = 4,99 €  

---

## VK‑02 – Warenkorb genau 20 €  
**Technik:** Grenzwertanalyse  

**Schritte:**  
1. Produkte im Wert von genau 20 € in den Warenkorb legen  
2. Warenkorb öffnen  

**Erwartet:**  
- Versandkosten = 0 €  

---

## VK‑03 – Warenkorb über 20 €  
**Technik:** Äquivalenzklassen (gültige Klasse: „Versandkostenfrei“)  

**Schritte:**  
1. Produkte im Wert von über 20 € in den Warenkorb legen  
2. Warenkorb öffnen  

**Erwartet:**  
- Versandkosten = 0 €  

---

## VK‑04 – Dynamische Aktualisierung  
**Technik:** Use Case Testing  

**Schritte:**  
1. Produkt hinzufügen  
2. Menge erhöhen  
3. Warenkorb beobachten  

**Erwartet:**  
- Versandkosten aktualisieren sich dynamisch  

---

# 4. Automatisierbare Testfälle

Diese Testfälle eignen sich besonders gut für Selenium/pytest:

### ✔ Versandkosten  
- VK‑01  
- VK‑02  
- VK‑03  
- VK‑04  

### ✔ Altersverifikation  
- AV‑01  
- AV‑03  

### ✔ Bewertungssystem (sobald implementiert)  
- BS‑01  
- BS‑02  

---
