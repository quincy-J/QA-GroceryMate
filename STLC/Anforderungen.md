# Anforderungen – GroceryMate

Dieses Dokument beschreibt die neuen Funktionen, die im nächsten Release von GroceryMate implementiert werden sollen.  
Es enthält zunächst unklare Anforderungen, anschließend Klärungsfragen und schließlich die präzisierten, testbaren Anforderungen.

---

# 1. Zusammenfassung der bestehenden Software

GroceryMate ist ein öffentlicher Webshop, der Nutzern ermöglicht:

- Produkte zu durchsuchen  
- Kategorien zu filtern  
- Produkte in den Warenkorb zu legen  
- Produktdetails einzusehen  
- Favoriten zu speichern  
- Ohne Login zu shoppen (Checkout ist im Live‑System nicht vollständig implementiert)

Die Seite ist ohne Registrierung nutzbar und basiert auf einem Live‑System.

---

# 2. Neue Funktionen (für das nächste Release)

---

# 2.1 Bewertungssystem für Produkte

## Unklare Anforderung
Nutzer sollen Produkte mit einem 5‑Sterne‑System bewerten und optional Feedback hinterlassen können.

## Klärungsfragen
1. Dürfen nur registrierte Nutzer bewerten?  
2. Kann ein Nutzer ein Produkt mehrfach bewerten?  
3. Gibt es ein Zeichenlimit für das Feedback?  
4. Können Bewertungen bearbeitet oder gelöscht werden?  
5. Wird der Durchschnittswert automatisch berechnet?  
6. Wo wird die Bewertung angezeigt (Produktseite, Listenansicht)?

## Detaillierte, testbare Anforderung
- Nur **registrierte Nutzer** dürfen Produkte bewerten.  
- Eine Bewertung besteht aus:
  - 1–5 Sternen  
  - optionalem Text (max. **300 Zeichen**)  
- Ein Nutzer kann ein Produkt **nur einmal** bewerten.  
- Nutzer können ihre Bewertung **bearbeiten oder löschen**.  
- Der Durchschnittswert wird automatisch berechnet und auf der Produktseite angezeigt.  
- Bewertungen sind öffentlich sichtbar.

---

# 2.2 Altersverifikation für alkoholische Produkte

## Unklare Anforderung
Beim Aufrufen der Kategorie „Alkohol“ soll ein Alterscheck erscheinen.

## Klärungsfragen
1. Wie erfolgt die Verifikation (Geburtsdatum, Checkbox, Button)?  
2. Wird die Verifikation pro Session gespeichert?  
3. Was passiert, wenn der Nutzer nicht bestätigt?  
4. Muss die Verifikation beim Checkout erneut erfolgen?  
5. Wird der Zugriff auf einzelne Produkte oder ganze Kategorien blockiert?

## Detaillierte, testbare Anforderung
- Beim ersten Aufruf der Kategorie **„Alkohol“** erscheint ein **Modal**, in dem Nutzer bestätigen müssen, dass sie **18+** sind.  
- Ohne Bestätigung ist **kein Zugriff** auf alkoholische Produkte möglich.  
- Die Verifikation gilt für die **aktuelle Session**.  
- Beim Checkout wird die Altersverifikation **erneut geprüft**.  
- Wird die Verifikation abgelehnt, bleibt der Nutzer auf der vorherigen Seite.

---

# 2.3 Versandkostenregelung

## Unklare Anforderung
Versandkosten sollen ab einem bestimmten Bestellwert entfallen.

## Klärungsfragen
1. Ab welchem Betrag entfallen die Versandkosten?  
2. Bezieht sich der Betrag auf den Wert **vor** oder **nach** Rabatten?  
3. Wie hoch sind die Versandkosten unterhalb des Schwellenwerts?  
4. Soll die Berechnung dynamisch im Warenkorb angezeigt werden?  
5. Gibt es Ausnahmen (z. B. schwere Artikel)?

## Detaillierte, testbare Anforderung
- Unter **20 €** Bestellwert fallen **4,99 € Versandkosten** an.  
- Ab **20 €** (nach Rabatten) ist der Versand **kostenlos**.  
- Die Versandkosten werden **dynamisch im Warenkorb** angezeigt.  
- Die Berechnung aktualisiert sich automatisch bei:
  - Änderung der Menge  
  - Hinzufügen/Entfernen von Produkten  
  - Anwendung von Rabatten  
- Versandkosten werden im Checkout erneut angezeigt.

---
