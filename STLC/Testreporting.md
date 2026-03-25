# Testreporting – GroceryMate

Dieses Dokument fasst alle während der Testdurchführung gefundenen Fehler zusammen.  
Die vollständigen Fehlerbeschreibungen befinden sich im GitHub‑Issues‑Tab sowie im Dokument *Issues.md*.

---

# Bewertungssystem
Das Bewertungssystem ist nicht implementiert.  
Keine Tests möglich → keine Fehler dokumentiert.

---

# Altersverifikation
Alle Testfälle wurden erfolgreich bestanden.  
Keine Fehler gefunden.

---

# Versandkosten
Die Versandkosten werden im Warenkorb nicht angezeigt, obwohl die Funktion laut Shopbeschreibung existieren sollte.

**Gefundener Fehler:**
- Versandkosten werden nicht angezeigt (Issue #1)

---

# Favoritenfunktion
Mehrere Fehler im Zusammenhang mit dem Favoritenstatus:

**Gefundene Fehler:**
- Favoritenstatus wird nach Tab‑Wechsel nicht korrekt aktualisiert  
- Favoritenstatus kann im Shop nicht entfernt werden (Fehlermeldung „failed to add to favorites“)

---

# Mengenfeld
Das Mengenfeld akzeptiert extrem große Werte (z. B. 1e+72).

**Gefundener Fehler:**
- Fehlende Eingabevalidierung für Mengenfeld

---

# Sortierung & Filter
Mehrere Probleme bei Sortierung und Filterung:

**Gefundene Fehler:**
- Sortierung nach Preis nur aufsteigend möglich  
- Sidebar‑Filter sortiert Produkte inkonsistent

---

# Navigation
**Gefundener Fehler:**
- Kategorie‑Link „Salate“ unter Home funktioniert nicht

---

# Fehlerübersicht

| Bereich | Anzahl Fehler |
|--------|---------------|
| Versandkosten | 1 |
| Favoriten | 2 |
| Mengenfeld | 1 |
| Sortierung/Filter | 2 |
| Navigation | 1 |
| **Gesamt** | **7** |

---

# Zusammenfassung
Während der Testdurchführung wurden mehrere Fehler im Live‑System gefunden.  
Alle Fehler wurden als GitHub Issues dokumentiert und sind reproduzierbar.
