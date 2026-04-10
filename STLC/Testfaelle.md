# Testfälle – GroceryMate

Dieses Dokument enthält die Testfälle für die neuen Features.  
Format gemäß Vorgabe: Testentwurfsverfahren → Testfall → Eingabe → Erwartetes Ergebnis.

---

# 1. Bewertungssystem

**Testentwurfsverfahren:** Grenzwertanalyse (BVA), Äquivalenzklassenbildung (EP), Fehlerermessen, Use-Case-Test

### 1. BVA
**Testfall:** Bewertung mit 1 Stern (Minimum)  
- **Eingabe:** 1 Stern, kein Text  
- **Erwartet:** Bewertung wird gespeichert und angezeigt.

### 2. BVA
**Testfall:** Bewertung mit 5 Sternen (Maximum)  
- **Eingabe:** 5 Sterne, kein Text  
- **Erwartet:** Bewertung wird gespeichert und angezeigt.

### 3. BVA
**Testfall:** Bewertung mit genau 500 Zeichen  
- **Eingabe:** 5 Sterne, Text = 500 Zeichen  
- **Erwartet:** Bewertung wird gespeichert.

### 4. BVA
**Testfall:** Bewertung mit 501 Zeichen  
- **Eingabe:** 5 Sterne, Text = 501 Zeichen  
- **Erwartet:** Fehlermeldung „Maximal 500 Zeichen“.

### 5. EP
**Testfall:** Bewertung ohne Text  
- **Eingabe:** 4 Sterne, Text leer  
- **Erwartet:** Bewertung wird gespeichert.

### 6. Error Guessing
**Testfall:** Bewertung ohne Sterne  
- **Eingabe:** kein Stern ausgewählt  
- **Erwartet:** Fehlermeldung „Bitte Sterne auswählen“.

### 7. Error Guessing
**Testfall:** Bewertung mit ungültigen Zeichen  
- **Eingabe:** 5 Sterne, Text enthält HTML („<script>…“)  
- **Erwartet:** Fehlermeldung oder Sanitizing.

### 8. Use Case
**Testfall:** Bewertung bearbeiten  
- **Eingabe:** vorhandene Bewertung ändern  
- **Erwartet:** Änderung wird gespeichert und angezeigt.

### 9. Use Case
**Testfall:** Bewertung löschen  
- **Eingabe:** Bewertung löschen  
- **Erwartet:** Bewertung verschwindet, Durchschnitt aktualisiert sich.

### 10. Use Case
**Testfall:** Durchschnittswert aktualisiert sich  
- **Eingabe:** neue Bewertung abgeben  
- **Erwartet:** Sterne + Anzahl in Klammern aktualisieren sich.

---

# 2. Altersverifikation

**Testentwurfsverfahren:** BVA, EP, Error Guessing, Use-Case-Test

### 1. Use Case
**Testfall:** Modal erscheint beim Öffnen der Alkohol-Kategorie  
- **Eingabe:** Nutzer klickt auf „Alkohol“  
- **Erwartet:** Altersmodal erscheint.

### 2. EP
**Testfall:** Nutzer ist über 18  
- **Eingabe:** Geburtsdatum = heute – 20 Jahre  
- **Erwartet:** Zugriff erlaubt.

### 3. BVA
**Testfall:** Nutzer ist genau 18  
- **Eingabe:** Geburtsdatum = heute – 18 Jahre  
- **Erwartet:** Zugriff erlaubt.

### 4. BVA
**Testfall:** Nutzer ist knapp unter 18  
- **Eingabe:** Geburtsdatum = heute – 18 Jahre + 1 Tag  
- **Erwartet:** Zugriff verweigert.

### 5. Error Guessing
**Testfall:** Ungültiges Datumsformat  
- **Eingabe:** „1400“, „11-11-1700“, „11-11-3000“  
- **Erwartet:** Fehlermeldung „Ungültiges Datum“.

### 6. Use Case
**Testfall:** Ablehnung der Altersverifikation  
- **Eingabe:** Nutzer klickt „Nein“  
- **Erwartet:** Zugriff verweigert, Nutzer bleibt auf vorheriger Seite.

### 7. Session-Test
**Testfall:** Modal erscheint nicht erneut  
- **Eingabe:** Alkohol → Modal bestätigen → erneut Alkohol öffnen  
- **Erwartet:** Modal erscheint nicht.

---

# 3. Versandkosten

**Testentwurfsverfahren:** BVA, Use-Case-Test, Error Guessing

### 1. BVA
**Testfall:** Warenkorbwert = 19,99 €  
- **Eingabe:** Produkte im Wert von 19,99 €  
- **Erwartet:** Versandkosten = 4,99 €.

### 2. BVA
**Testfall:** Warenkorbwert = 20 €  
- **Eingabe:** Produkte im Wert von 20 €  
- **Erwartet:** Versandkosten = 0 €.

### 3. BVA
**Testfall:** Warenkorbwert > 20 €  
- **Eingabe:** Produkte im Wert von 25 €  
- **Erwartet:** Versandkosten = 0 €.

### 4. Use Case
**Testfall:** Dynamische Aktualisierung  
- **Eingabe:** Warenkorb steigt über 20 €  
- **Erwartet:** Versandkosten ändern sich von 4,99 € → 0 €.

### 5. Error Guessing
**Testfall:** Warenkorb fällt wieder unter 20 €  
- **Eingabe:** Produkte entfernen  
- **Erwartet:** Versandkosten ändern sich zurück auf 4,99 €.

---

# 4. Warenkorb nach Kauf

### Use Case
**Testfall:** Warenkorb wird nach Kauf geleert  
- **Eingabe:** Kauf abschließen  
- **Erwartet:** Warenkorb ist leer.