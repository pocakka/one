# AI Shield Magazin - 2025 Január (1. szám)

## 📖 Projekt Áttekintés

**AI Shield Magazin** - Professzionális AI biztonsági magazin magyar nyelven
- **Szám:** 2025/01 (Első szám)
- **Megjelenés:** 2025 Január
- **Terjedelem:** 26 cikk, ~35,000+ szó
- **Célközönség:** Családok, vállalatok, szakértők

---

## 📁 Projekt Struktúra

```
AI_SHIELD_MAGAZIN_2025_01/
├── 00_metadata/
│   ├── config.json                    # Magazin konfiguráció
│   └── style_guide.md                 # Szerkesztői stílus útmutató
│
├── 01_tartalom/                       # Összes cikk
│   ├── hirek/ (3 cikk)
│   ├── kezdoknek/ (4 cikk)
│   ├── csaladi/ (3 cikk)
│   ├── vallalati/ (5 cikk)
│   ├── szakertoi/ (4 cikk)
│   ├── termekkorkep/ (3 cikk)
│   ├── interju/ (1 cikk)
│   └── hasznos/ (3 cikk)
│
├── 02_kepek/                          # Képek, ikonok (placeholder)
│   ├── illusztraciok/
│   ├── infografika/
│   └── ikonok/
│
├── 03_sablonok/                       # Újrahasználható sablonok
│   ├── cikk_template.md
│   └── oldal_template.html
│
├── 04_vegleges/                       # Publikálásra kész
│   ├── MAGAZIN_TELJES.md             # Összefűzött teljes magazin
│   └── export/                        # Letölthető sablonok (placeholder)
│
└── README.md                          # Ez a fájl
```

---

## 🎯 Rovatok és Cikkek

### 📰 Hírek & Trendek (3 cikk)
- EU AI Act hatályba lépése - magyar vonatkozások
- ChatGPT Canvas funkció biztonsági kihívások
- 2026 AI biztonsági trendek előrejelzés

### 🌱 Kezdőknek (4 cikk)
- AI hallucináció magyarázata és védekezés
- Első AI asszisztens beállítása biztonságosan
- 5+1 leggyakoribb AI csalás
- AI Biztonság Kisszótár (20 kifejezés)

### 👨‍👩‍👧‍👦 Családi AI (3 cikk)
- ChatGPT használat házi feladatban - szabályok
- Nagyszülők és az AI (60+ kezdőknek)
- Családi AI szabálykönyv - család megbeszélési agenda

### 🏢 Vállalati Fókusz (5 cikk)
- KKV AI biztonsági csomag 0 forintból
- 2 millió forintos prompt hiba - esettanulmány
- 30 perces DIY AI biztonsági audit
- AI biztonsági költségvetés tervezés 2026-ra
- GDPR + AI Act jogi összefoglaló

### 🔬 Szakértői Műhely (4 cikk)
- Prompt injection védelem implementálása (Python/Node.js)
- Zero Trust AI architektúra
- LLM biztonsági audit módszertan
- Enterprise AI governance framework

### 🛡️ Termékkörkép (3 cikk)
- Top 10 AI biztonsági platform összehasonlítás
- Ingyenes és open source AI security eszközök
- Új startupokok az AI security piacon (2025 Q4/2026 Q1)

### 💬 Interjú (1 cikk)
- Dr. Kovács Anna - AI Biztonsági Vezető (fiktív, de valós best practices alapján)

### 🔧 Hasznos (3 cikk)
- Letölthető sablonok (policy, szerződések, checklists)
- AI Kockázati Térkép infografika leírás
- Következő szám előzetese (2026 február)

---

## 🚀 Hogyan Használd

### 1. Böngészés

**Online olvasáshoz:**
```bash
cd AI_SHIELD_MAGAZIN_2025_01
# Nyisd meg a 04_vegleges/MAGAZIN_TELJES.md fájlt
```

**Rovat szerinti olvasás:**
```bash
# Például csak a Kezdőknek rovatot:
cd 01_tartalom/kezdoknek
ls *.md
```

### 2. Markdown Megnyitása

**VSCode-ban:**
```bash
code AI_SHIELD_MAGAZIN_2025_01
```

**Markdown preview:**
- VSCode: `Ctrl+Shift+V` (Windows/Linux) vagy `Cmd+Shift+V` (Mac)

### 3. PDF Generálás (opcionális)

**Pandoc használatával:**
```bash
cd 04_vegleges
pandoc MAGAZIN_TELJES.md -o AI_Shield_2025_01.pdf \
  --pdf-engine=xelatex \
  -V geometry:margin=1in
```

**Vagy:**
Használj online markdown to PDF convertert (pl. https://www.markdowntopdf.com/)

---

## 📊 Statisztikák

| Metrika | Érték |
|---------|-------|
| **Rovatok** | 8 |
| **Cikkek összesen** | 26 |
| **Szószám** | ~35,000+ |
| **Olvasási idő** | ~180 perc |
| **Kód példák** | 15+ |
| **Táblázatok** | 30+ |
| **Sablonok** | 10+ |
| **Infografikák** | 5+ (leírás formátumban) |

---

## 🛠️ Technikai Részletek

### Markdown Standard
- **Format:** GitHub-Flavored Markdown (GFM)
- **Kód blokkok:** Syntax highlighting támogatás (Python, JavaScript, Bash, YAML)
- **Táblázatok:** Markdown táblázat szintaxis

### Metadata Format
- **YAML Front Matter:** Minden cikkben
- **Tartalom:** title, category, readTime, difficulty, keyPoints, tags, author, date

### Licensz
- **Tartalom:** Creative Commons BY-NC-SA 4.0
- **Kód példák:** MIT License
- **Sablonok:** CC0 (Public Domain)

---

## 🔧 Szerkesztői Használat

### Új Cikk Hozzáadása

1. Másolj egy template-et:
```bash
cp 03_sablonok/cikk_template.md 01_tartalom/ROVAT/uj_cikk.md
```

2. Töltsd ki a YAML metadatát

3. Írd meg a tartalmat a `style_guide.md` szerint

4. Add hozzá a `MAGAZIN_TELJES.md` tartalomjegyzékhez

### Stílus útmutató
Lásd: `00_metadata/style_guide.md`

**Főbb szabályok:**
- Hangnem: szakmai de közérthető
- Bekezdés max 4 sor
- Listák: 3-5 elem ideális
- Címek: SEO-optimalizált
- Linkek: internal és external

---

## 🌐 Online Publikálás

### GitHub Pages (opcionális)

```bash
# Ha GitHub Pages-re akarod tenni:
git init
git add .
git commit -m "AI Shield Magazin 2025/01"
git branch -M main
git remote add origin https://github.com/YOURNAME/ai-shield-magazin.git
git push -u origin main

# Majd GitHub Settings → Pages → Source: main branch
```

### Weboldal Generálás

**MkDocs használatával:**
```bash
pip install mkdocs mkdocs-material
mkdocs new .
# Konfiguráld mkdocs.yml-t
mkdocs serve  # Local preview
mkdocs build  # HTML generálás
```

---

## 📞 Kapcsolat és Hozzájárulás

### Visszajelzés

**Email:** info@aishield.hu
**GitHub Issues:** Ha találsz hibát vagy van javaslatod

### Hozzájárulás (Contributing)

1. Fork-old a repo-t
2. Hozz létre feature branch-et (`git checkout -b feature/UjCikk`)
3. Commit-old változtatásaidat
4. Push-old a branch-re
5. Nyiss Pull Request-et

**Contribution guidelines:**
- Kövesd a `style_guide.md`-t
- Magyar helyesírás ellenőrzés
- GDPR compliant tartalmak
- Forrás megjelölés külső információknál

---

## 📅 Verzió Történet

| Verzió | Dátum | Változások |
|--------|-------|------------|
| **1.0** | 2025 Január | Első kiadás - 26 cikk, 8 rovat |

---

## 🙏 Köszönetnyilvánítás

**Köszönet a következőknek:**
- OWASP LLM Top 10 projektnek
- OpenAI, Anthropic dokumentációért
- Magyar GDPR szakértői közösségnek
- Minden open source AI security project-nek

---

## ⚖️ Licensz

**Tartalom:**
- CC BY-NC-SA 4.0 (Creative Commons Attribution-NonCommercial-ShareAlike)
- Szabadon megosztható, módosítható non-commercial célokra
- Forrás megjelölés kötelező

**Kód példák:**
- MIT License
- Szabadon használható, módosítható kereskedelmi célra is

**Sablonok:**
- CC0 (Public Domain)
- Korlátozás nélkül használhatók

---

## 🎯 Következő Lépések

**Ha Olvasó Vagy:**
1. Olvasd el az "MAGAZIN_TELJES.md"-t
2. Töltsd le a sablonokat a `04_vegleges/export` mappából
3. Iratkozz fel a következő számra: info@aishield.hu

**Ha Szerkesztő Vagy:**
1. Tanulmányozd a `style_guide.md`-t
2. Nézd meg a meglévő cikkek struktúráját
3. Javasolj témákat a következő számhoz

**Ha Fejlesztő Vagy:**
1. Fork-old a repo-t
2. Generálj HTML/PDF verziót
3. Építs automation-t (CI/CD)

---

## 📚 További Források

**Külső linkek:**
- [OWASP LLM Top 10](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- [EU AI Act (magyar)](https://eur-lex.europa.eu/legal-content/HU/)
- [NAIH - Magyar Adatvédelmi Hatóság](https://naih.hu)
- [OpenAI Safety Best Practices](https://platform.openai.com/docs/guides/safety-best-practices)

---

**🛡️ AI Shield Magazin - Védelem az AI korszakban**

*Minden hónapban friss tartalmak AI biztonságról, magyar nyelven.*

**2025 Január | 1. szám | READY TO PUBLISH ✅**
