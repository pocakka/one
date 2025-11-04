# AI Security Magazine

**A mesterséges intelligencia biztonságának szakmai magazinja**

## 📖 Projekt leírás

Ez egy professzionális AI Security magazin, amely havonta jelenik meg és széles közönséget szólít meg - a kíváncsi laikusoktól az üzleti vezetőkön át a hardcore biztonsági szakemberekig.

### Célközönség
- 🔍 Kíváncsi laikusok
- 💼 Üzleti vezetők (CEO, CFO, CTO, CISO)
- 🛡️ Biztonsági szakemberek
- 🔬 Kutatók és fejlesztők
- 🎓 Diákok és karrierváltók

## 📂 Projekt struktúra

```
magazine/
├── content/          # Magazin tartalom
│   ├── issue-01.html # HTML verzió
│   └── issue-01.tex  # LaTeX verzió (alternatív)
├── templates/        # Template fájlok
│   └── magazine.cls  # LaTeX class
├── output/           # Generált PDF-ek
│   └── AI_Security_Magazine_Issue_01.pdf
├── images/           # Képek és grafika (jövőbeli)
├── generate_pdf.py   # PDF generáló szkript
└── README.md         # Ez a fájl
```

## 🚀 Használat

### PDF generálás

```bash
# Navigálj a magazine könyvtárba
cd magazine/

# Futtasd a PDF generátort
python3 generate_pdf.py
```

A generált PDF a `output/` könyvtárban lesz elérhető.

### Követelmények

```bash
pip install weasyprint
```

## 📋 1. szám tartalma

1. **AI Security Világ** - Hírek, trendek, statisztikák
2. **Interjú** - Bruce Schneier az AI biztonságról
3. **Kutatás & Innováció** - Adversarial Machine Learning
4. **Fenyegetések Radar** - Q3 2025 Threat Landscape
5. **Gyakorlati Útmutató** - AI Security 101
6. **Üzleti Nézőpont** - ROI és stratégia
7. **Eszköztár** - Top AI Security eszközök
8. **Képzés & Karrier** - Hogyan válj AI Security szakemberré
9. **Közösség** - Konferenciák és networking

## 🎨 Design jellemzők

- **Formátum:** A4 PDF
- **Színvilág:** Professzionális kék-piros paletta
- **Tipográfia:** Georgia serif font a jó olvashatóságért
- **Elemek:** Info boxok, warning boxok, tip boxok, kód példák
- **Stílus:** Modern, magazine-szerű, könnyen olvasható

## 🔄 Jövőbeli számok

A magazin havonta jelenik meg. Tervezett témák:
- Quantum AI és kriptográfia
- Zero Trust Architecture AI rendszerekhez
- LLM guardrails implementálása
- AI governance és compliance

## 📧 Kapcsolat

- **Email:** newsletter@aisecuritymagazine.com
- **Web:** www.aisecuritymagazine.com
- **LinkedIn:** @AISecurityMag

## 📄 Licenc

Ez a projekt oktatási és demonstrációs célokat szolgál.

---

**AI Security Magazine** - Ahol a mesterséges intelligencia találkozik a kiberbiztonsággal 🔒
