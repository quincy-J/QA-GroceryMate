# Testfälle – GroceryMate

---

# 1. Bewertungssystem

## Testfall 1 – Bewertung mit 5 Sternen speichern  
**Technik:** Funktionstest  
**Schritte:**  
1. Produktseite öffnen  
2. 5 Sterne auswählen  
3. Bewertung speichern  
**Erwartet:** Bewertung wird gespeichert und angezeigt  

## Testfall 2 – Bewertung mit Text (max. 300 Zeichen)  
**Technik:** Äquivalenzklassen  
**Schritte:**  
1. Produktseite öffnen  
2. Text mit 300 Zeichen eingeben  
3. Speichern  
**Erwartet:** Bewertung wird gespeichert  

## Testfall 3 – Bewertung über 300 Zeichen  
**Technik:** Grenzwertanalyse  
**Schritte:**  
1. 301 Zeichen eingeben  
2. Speichern  
**Erwartet:** Fehlermeldung  

---

# 2. Altersverifikation

## Testfall 1 – Altersmodal erscheint  
**Technik:** Funktionstest  
**Schritte:**  
1. Kategorie „Alkohol“ öffnen  
**Erwartet:** Altersmodal erscheint  

## Testfall 2 – Zugriff verweigert  
**Technik:** Fehlervermutung  
**Schritte:**  
1. „Nein, ich bin nicht 18“ klicken  
**Erwartet:** Kein Zugriff  

## Testfall 3 – Zugriff nach Bestätigung  
**Technik:** Funktionstest  
**Schritte:**  
1. „Ich bin 18+“ klicken  
**Erwartet:** Kategorie wird angezeigt  

---

# 3. Versandkosten

## Testfall 1 – Warenkorb unter 50 €  
**Technik:** Grenzwertanalyse  
**Schritte:**  
1. Produkt für 20 € hinzufügen  
**Erwartet:** Versandkosten = 4,99 €  

## Testfall 2 – Warenkorb genau 50 €  
**Technik:** Grenzwertanalyse  
**Schritte:**  
1. Produkte für genau 50 € hinzufügen  
**Erwartet:** Versandkosten = 0 €  

## Testfall 3 – Warenkorb über 50 €  
**Technik:** Äquivalenzklassen  
**Schritte:**  
1. Produkte für 60 € hinzufügen  
**Erwartet:** Versandkosten = 0 €  

---

# Automatisierbare Testfälle
- Versandkosten (alle 3) → stabil, klar, deterministisch  
- Altersverifikation (Testfall 1 & 3) → UI‑Modal, gut automatisierbar  
- Bewertungssystem (Testfall 1 & 2) → Eingabe + Speicherung
