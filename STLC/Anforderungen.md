# Anforderungen – GroceryMate

## Zusammenfassung der bestehenden Software
GroceryMate ist ein öffentlicher Webshop, der Nutzern ermöglicht:
- Produkte zu durchsuchen
- Kategorien zu filtern
- Produkte in den Warenkorb zu legen
- Bestellungen abzuschließen
- Produktdetails einzusehen

Die Seite ist ohne Login nutzbar und basiert auf einem Live‑System.

---

# Neue Funktionen (für das nächste Release)

## 1. Bewertungssystem für Produkte

### Unklare Anforderung
Nutzer sollen Produkte mit einem 5‑Sterne‑System bewerten und optional Feedback hinterlassen können.

### Fragen
1. Dürfen nur registrierte Nutzer bewerten?
2. Kann ein Nutzer ein Produkt mehrfach bewerten?
3. Gibt es ein Zeichenlimit für das Feedback?
4. Können Bewertungen bearbeitet oder gelöscht werden?

### Detaillierte Anforderung
Nur registrierte Nutzer dürfen Produkte einmalig bewerten.  
Bewertungen bestehen aus:
- 1–5 Sternen  
- optionalem Text (max. 300 Zeichen)

Nutzer können ihre Bewertung bearbeiten oder löschen.  
Der Durchschnittswert wird automatisch berechnet und angezeigt.

---

## 2. Altersverifikation für alkoholische Produkte

### Unklare Anforderung
Beim Aufrufen der Kategorie „Alkohol“ soll ein Alterscheck erscheinen.

### Fragen
1. Wie erfolgt die Verifikation (Geburtsdatum, Checkbox)?
2. Wird die Verifikation pro Session gespeichert?
3. Was passiert, wenn der Nutzer nicht bestätigt?

### Detaillierte Anforderung
Beim ersten Aufruf der Kategorie „Alkohol“ erscheint ein Modal, in dem Nutzer bestätigen müssen, dass sie 18+ sind.  
Ohne Bestätigung kein Zugriff.  
Die Verifikation gilt für die Session und wird beim Checkout erneut geprüft.

---

## 3. Versandkostenänderung

### Unklare Anforderung
Versandkosten sollen ab einem bestimmten Bestellwert entfallen.

### Fragen
1. Ab welchem Betrag entfallen die Versandkosten?
2. Bezieht sich der Betrag auf den Wert vor oder nach Rabatten?
3. Wie hoch sind die Versandkosten unterhalb des Schwellenwerts?

### Detaillierte Anforderung
Unter 50 € fallen 4,99 € Versandkosten an.  
Ab 50 € (nach Rabatten) ist der Versand kostenlos.  
Die Berechnung wird dynamisch im Warenkorb angezeigt.
