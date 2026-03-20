# Testdurchführung – GroceryMate

Dieses Dokument enthält die Ergebnisse der manuellen Testdurchführung basierend auf den zuvor entworfenen Testfällen.

---

## Legende
PASS = Test bestanden  
FAIL = Test fehlgeschlagen  
N/A = Funktion nicht implementiert / nicht testbar  

---

# 1. Bewertungssystem

Das Bewertungssystem ist in der aktuellen Version von GroceryMate nicht implementiert.  
Eine Bewertung ist nur nach einem Kauf möglich, ein Kauf ist jedoch nicht möglich.  
Daher sind alle Testfälle **nicht durchführbar**.

### BS‑01 – Bewertung mit 5 Sternen  
Status: **N/A**

### BS‑02 – Bewertung mit Text (300 Zeichen)  
Status: **N/A**

### BS‑03 – Bewertung über 300 Zeichen  
Status: **N/A**

---

# 2. Altersverifikation

### AV‑01 – Altersmodal erscheint  
Status: PASS

### AV‑02 – Zugriff verweigert  
Status: PASS

### AV‑03 – Zugriff nach Bestätigung  
Status: PASS

---

# 3. Versandkosten

Das Hinzufügen von Produkten zum Warenkorb ist in der aktuellen Version nicht möglich.  
Daher können die Versandkosten nicht getestet werden.

### VK‑01 – Warenkorb unter 50 €  
Status: **N/A**

### VK‑02 – Warenkorb genau 50 €  
Status: **N/A**

### VK‑03 – Warenkorb über 50 €  
Status: **N/A**

---

# Zusammenfassung
| Bereich | PASS | FAIL | N/A |
|--------|------|------|-----|
| Bewertungssystem | 0 | 0 | 3 |
| Altersverifikation | 3 | 0 | 0 |
| Versandkosten | 0 | 0 | 3 |
| **Gesamt** | **3** | **0** | **6** |

---

# Gefundene Fehler
Es wurden **keine Fehler** gefunden, da nur die Altersverifikation testbar war und korrekt funktioniert.
