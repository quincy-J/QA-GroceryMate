# Anforderungen – GroceryMate (Release Features)

Dieses Dokument beschreibt die testbaren Anforderungen für die drei neuen Features der GroceryMate-Webanwendung.  
Alle Anforderungen sind präzise, messbar und dienen als Grundlage für die Testfallerstellung.

---

# 1. Bewertungssystem

## 1.1 Allgemeines Verhalten
- Nutzer kann ein Produkt mit **1 bis 5 Sternen** bewerten.
- Eine Bewertung besteht aus:
  - Sternebewertung (**Pflichtfeld**)
  - optionalem Text (**freiwillig**)
- Ein Nutzer kann **pro Produkt nur eine Bewertung** abgeben.
- Nutzer kann seine Bewertung **bearbeiten** und **löschen**.

## 1.2 Bewertungstext
- Der Bewertungstext ist **optional**.
- Der Bewertungstext darf **maximal 500 Zeichen** lang sein.
- Eingaben über 500 Zeichen müssen mit einer **Fehlermeldung** abgelehnt werden.
- Leerer Text ist erlaubt.
- Ungültige Eingaben (HTML-Tags, extrem lange Strings, SQL-Injection) müssen abgefangen werden.

## 1.3 Anzeige der Bewertung
- Nach dem Absenden wird die Bewertung **sofort** angezeigt.
- Die Bewertung zeigt:
  - Sterne (1–5)
  - Bewertungstext (falls vorhanden)
  - Datum (falls vorgesehen)

## 1.4 Durchschnittswert
- Das System berechnet den Durchschnitt aller Bewertungen automatisch.
- Der Durchschnitt wird **in Form von Sternsymbolen** angezeigt (z. B. ⭐⭐⭐⭐☆).
- Neben den Sternen wird die **Anzahl der Bewertungen in Klammern** angezeigt, z. B.:
  - ⭐⭐⭐⭐☆ (3)
- Der Durchschnitt aktualisiert sich nach:
  - neuer Bewertung
  - Bearbeitung
  - Löschung

---

# 2. Altersverifikation

## 2.1 Wann erscheint das Altersmodal?
- Das Altersverifikations-Modal erscheint **nur**, wenn der Nutzer eine **alkoholische Kategorie** öffnet.
- Es erscheint **nicht** beim Öffnen des Shops oder anderer Kategorien.

## 2.2 Eingabevalidierung
- Das Geburtsdatum muss im Format **TT-MM-JJJJ** eingegeben werden.
- Das Datum muss **realistisch** sein:
  - Jahr ≥ 1900
  - Jahr ≤ aktuelles Jahr
  - Datum darf nicht in der Zukunft liegen
- Nutzer muss **mindestens 18 Jahre alt** sein.

## 2.3 Verhalten bei Bestätigung
- Wenn der Nutzer bestätigt, dass er 18+ ist:
  - erhält er Zugriff auf alkoholische Produkte
  - das Modal erscheint **nicht erneut** während derselben Session

## 2.4 Verhalten bei Ablehnung
- Wenn der Nutzer angibt, **unter 18** zu sein:
  - wird der Zugriff verweigert
  - der Nutzer bleibt auf der vorherigen Seite
  - es wird eine Fehlermeldung angezeigt

## 2.5 Session-Verhalten
- Die Altersverifikation gilt **für die gesamte Session**.
- Das Modal erscheint erst wieder, wenn die Session endet oder gelöscht wird.
- **Keine erneute Prüfung beim Checkout** (nicht Teil der Aufgabenstellung).

---

# 3. Versandkostenregelung

## 3.1 Grundregel
- Warenkorbwert < 20 € → Versandkosten = **4,99 €**
- Warenkorbwert ≥ 20 € → Versandkosten = **0 €**

## 3.2 Dynamische Aktualisierung
- Versandkosten müssen **sofort aktualisiert** werden, wenn sich der Warenkorbwert ändert.
- Versandkosten müssen **immer sichtbar** sein.

## 3.3 Grenzwert
- Bei **genau 20 €** fallen **0 €** Versandkosten an.

---

# 4. Warenkorb nach Kauf

## 4.1 Verhalten nach Kauf
- Nach erfolgreichem Kauf wird der Warenkorb **automatisch geleert**.
- Der Nutzer darf keine alten Produkte im Warenkorb sehen.