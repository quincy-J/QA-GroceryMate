# Testdurchführung – GroceryMate

Dieses Dokument enthält die Ergebnisse der manuellen Testdurchführung basierend auf den zuvor entworfenen Testfällen.

---

## Legende
- **PASS** = Test bestanden  
- **FAIL** = Test fehlgeschlagen  
- **N/A** = Funktion nicht implementiert / nicht testbar  

---

# 1. Bewertungssystem

Das Bewertungssystem ist weiterhin nicht implementiert.  
Eine Bewertung ist nur nach einem Kauf möglich, ein Kauf ist jedoch nicht möglich.

### BS‑01 – Bewertung mit 5 Sternen  
Status: **N/A**

### BS‑02 – Bewertung mit Text (300 Zeichen)  
Status: **N/A**

### BS‑03 – Bewertung über 300 Zeichen  
Status: **N/A**

---

# 2. Altersverifikation

### AV‑01 – Altersmodal erscheint  
Status: **PASS**

### AV‑02 – Zugriff verweigert  
Status: **PASS**

### AV‑03 – Zugriff nach Bestätigung  
Status: **PASS**

---

# 3. Versandkosten

Die Versandkostenfunktion ist laut Shopbeschreibung ab **20 €** relevant.  
Da der Warenkorb funktioniert, konnten die Tests durchgeführt werden.

### VK‑01 – Warenkorb unter 20 €  
Status: **FAIL**  
**Beobachtung:** Versandkosten werden nicht angezeigt.

### VK‑02 – Warenkorb genau 20 €  
Status: **FAIL**  
**Beobachtung:** Versandkosten werden nicht angezeigt.

### VK‑03 – Warenkorb über 20 €  
Status: **FAIL**  
**Beobachtung:** Versandkosten werden nicht angezeigt.

---

# 4. Favoritenfunktion

### FAV‑01 – Produkt zu Favoriten hinzufügen  
Status: **PASS**

### FAV‑02 – Produkt aus Favoriten entfernen  
Status: **PASS** (nur auf Favoriten‑Seite)

### FAV‑03 – Favoritenstatus im Shop nach Tab‑Wechsel  
Status: **FAIL**  
**Beobachtung:** Fehlermeldung „failed to add to favorites“

---

# 5. Mengenfeld

### QTY‑01 – Menge > 1000  
Status: **FAIL**  
**Beobachtung:** System akzeptiert astronomische Werte (z. B. 1e+72)

---

# 6. Sortierung & Filter

### SORT‑01 – Sortierung nach Preis (aufsteigend)  
Status: **PASS**

### SORT‑02 – Sortierung nach Preis (absteigend)  
Status: **FAIL**  
**Beobachtung:** Funktion nicht vorhanden

### FILTER‑01 – Sidebar „Filter by pricing“  
Status: **FAIL**  
**Beobachtung:** Sortierung ist inkonsistent / zufällig

---

# 7. Navigation

### NAV‑01 – Kategorie‑Link „Salate“ unter Home  
Status: **FAIL**  
**Beobachtung:** Link funktioniert nicht

---

# Zusammenfassung

| Bereich | PASS | FAIL | N/A |
|--------|------|------|-----|
| Bewertungssystem | 0 | 0 | 3 |
| Altersverifikation | 3 | 0 | 0 |
| Versandkosten | 0 | 3 | 0 |
| Favoriten | 2 | 1 | 0 |
| Mengenfeld | 0 | 1 | 0 |
| Sortierung/Filter | 1 | 2 | 0 |
| Navigation | 0 | 1 | 0 |
| **Gesamt** | **6** | **8** | **3** |

---

# Gefundene Fehler
Alle gefundenen Fehler sind im Dokument **Issues.md** beschrieben.
