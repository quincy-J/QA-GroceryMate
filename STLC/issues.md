# Issues – GroceryMate

Dieses Dokument listet alle während der Testdurchführung gefundenen Fehler auf.

---

# 1. Bewertungssystem

## Issue 1: Bewertungstext wird nach erster Abgabe nicht angezeigt
- **Schweregrad:** Mittel
- **Reproduktion:**
  1. Produkt öffnen
  2. Bewertung mit Text abgeben
- **Erwartet:** Text erscheint sofort
- **Tatsächlich:** Text erscheint erst nach Bearbeiten
- **Status:** Offen

## Issue 2: Zeichenbegrenzung wird beim Editieren nicht enforced
- **Schweregrad:** Mittel
- **Reproduktion:** Bewertung bearbeiten → mehr als 500 Zeichen eingeben
- **Erwartet:** Fehlermeldung
- **Tatsächlich:** Text wird akzeptiert
- **Status:** Offen

## Issue 3: Bewertung > 500 Zeichen wird gespeichert
- **Schweregrad:** Hoch
- **Reproduktion:** Bewertung mit 600+ Zeichen abgeben
- **Erwartet:** Fehlermeldung
- **Tatsächlich:** Bewertung wird gespeichert
- **Status:** Offen

---

# 2. Altersverifikation

## Issue 4: Modal erscheint beim Klick auf „Shop“
- **Schweregrad:** Mittel
- **Erwartet:** Modal erscheint nur bei Alkohol
- **Tatsächlich:** Modal erscheint beim Öffnen des Shops

## Issue 5: Ungültige Daten werden akzeptiert
- **Schweregrad:** Hoch
- **Beispiele:** „1400“, „11-11-1700“, „11-11-3000“
- **Erwartet:** Fehlermeldung
- **Tatsächlich:** Zugriff erlaubt

## Issue 6: Ablehnung führt zu „Sorry no products“
- **Schweregrad:** Mittel
- **Erwartet:** Nutzer bleibt auf vorheriger Seite
- **Tatsächlich:** Weiterleitung auf leere Seite

---

# 3. Versandkosten

## Issue 7: Versandkosten aktualisieren sich nicht korrekt
- **Schweregrad:** Hoch
- **Reproduktion:** Warenkorb über 20 € → zurück unter 20 €
- **Erwartet:** Versandkosten = 4,99 €
- **Tatsächlich:** Versandkosten bleiben bei 0 €

---

# 4. Warenkorb

## Issue 8: Warenkorb wird nach Kauf nicht geleert
- **Schweregrad:** Mittel
- **Erwartet:** Warenkorb leer
- **Tatsächlich:** Produkte bleiben im Warenkorb