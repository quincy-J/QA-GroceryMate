# Issues – GroceryMate

Dieses Dokument enthält alle während der Testdurchführung gefundenen Fehler.

---

## Issue 1 – Favoritenstatus wird nach Tab‑Wechsel nicht korrekt aktualisiert
**Schweregrad:** Mittel  
**Bereich:** Favoriten / State Management  

**Steps to Reproduce:**  
1. Produkt im Shop zu Favoriten hinzufügen  
2. Zur Seite „Favoriten“ wechseln  
3. Zurück zum Shop wechseln  
4. Herz‑Icon erneut klicken  

**Expected:** Favorit wird entfernt  
**Actual:** Fehlermeldung „failed to add to favorites“

---

## Issue 2 – Mengenfeld akzeptiert unlimitierte Eingaben (z. B. 1e+72)
**Schweregrad:** Hoch  
**Bereich:** Warenkorb / Validierung  

**Steps:**  
1. Produkt öffnen  
2. Im Mengenfeld „1e+72“ eingeben  
3. Add to Cart klicken  

**Expected:** Limitierung oder Fehlermeldung  
**Actual:** Wert wird akzeptiert

---

## Issue 3 – Kategorie‑Link „Salate“ unter Home funktioniert nicht
**Schweregrad:** Mittel  
**Bereich:** Navigation  

**Steps:**  
1. Home öffnen  
2. Auf „Salate“ klicken  

**Expected:** Kategorie öffnet sich  
**Actual:** Keine Reaktion

---

## Issue 4 – Sortierung nach Preis unterstützt keine absteigende Reihenfolge
**Schweregrad:** Niedrig  
**Bereich:** Sortierung  

**Steps:**  
1. Shop öffnen  
2. Sortierung nach Preis auswählen  

**Expected:** Aufsteigend und absteigend möglich  
**Actual:** Nur aufsteigend verfügbar

---

## Issue 5 – Sidebar „Filter by pricing“ sortiert Produkte nicht korrekt
**Schweregrad:** Mittel  
**Bereich:** Filter  

**Steps:**  
1. Sidebar öffnen  
2. Preisbereich auswählen  

**Expected:** Produkte korrekt gefiltert  
**Actual:** Reihenfolge inkonsistent

---

## Issue 6 – Add‑to‑Cart multipliziert Menge bei mehrfachen Klicks
**Schweregrad:** Mittel  
**Bereich:** Warenkorb  

**Steps:**  
1. Menge = 10 eingeben  
2. 5× auf „Add to Cart“ klicken  

**Expected:** Einmalige Addition  
**Actual:** 50 Stück im Warenkorb

---

## Issue 7 – Favoritenstatus im Shop nicht entfernbar nach Tab‑Wechsel
**Schweregrad:** Mittel  
**Bereich:** Favoriten  

**Steps:**  
1. Produkt favorisieren  
2. Zu Favoriten wechseln  
3. Zurück zum Shop  
4. Herz klicken  

**Expected:** Favorit wird entfernt  
**Actual:** Fehlermeldung „failed to add to favorites“

---

## Issue 8 – Versandkosten werden nicht angezeigt
**Schweregrad:** Hoch  
**Bereich:** Checkout / Warenkorb  

**Steps:**  
1. Produkt in den Warenkorb legen  
2. Warenkorb öffnen  

**Expected:** Versandkosten abhängig vom Warenkorbwert  
**Actual:** Keine Versandkosten sichtbar
