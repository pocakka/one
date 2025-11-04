---
title: "GDPR + AI Act = Mit kell tudnia magyar cégeknek?"
category: "Vállalati Fókusz"
readTime: "6 perc"
difficulty: "Haladó"
keyPoints:
  - GDPR és AI Act összehangolása
  - Magyar cégek konkrét kötelezettségei
  - Büntetési tételek és határidők
  - Gyakorlati megfelelési lépések
tags: ["GDPR", "AI Act", "jogi", "compliance", "NAIH"]
author: "AI Shield Szerkesztőség"
date: "2025 Január"
---

## GDPR + AI Act = Mit kell tudnia magyar cégeknek?

*2025-ben a magyar cégek kettős szabályozás alatt állnak: a 2018 óta érvényes GDPR (Általános Adatvédelmi Rendelet) és az újonnan érvényes EU AI Act. Mit jelent ez a gyakorlatban? Kinek mit kell tennie? Közérthető jogi összefoglaló - nem helyettesíti a jogi tanácsadást, de eligazítást ad.*

---

## ⚖️ A KÉT SZABÁLYOZÁS ÖSSZEHASONLÍTÁSA

| Szempont | GDPR | AI Act |
|----------|------|--------|
| **Mióta érvényes** | 2018. május 25. | 2024. augusztus 1. (fokozatos) |
| **Mit szabályoz** | Személyes adatok kezelése | AI rendszerek használata |
| **Ki ellenőrzi (HU)** | NAIH (Nemzeti Adatvédelmi Hatóság) | NAIH + új AI Hivatal (tervezés alatt) |
| **Bírság max** | 20M EUR vagy éves forgalom 4%-a | 35M EUR vagy éves forgalom 7%-a |
| **Magyar KKV érintett** | IGEN (minden cég) | IGEN (ha AI-t használ) |
| **Teljes hatály** | 2018-tól | 2027. augusztus 2. (fokozatos bevezetés) |

**Fontos:** A két szabályozás **együtt él** - nem helyettesíti egymást, kumulatívan kell megfelelni!

---

## 📜 GDPR + AI: A 4 FŐ KÖTELEZETTSÉG

### **1. ADATKEZELÉSI TÁJÉKOZTATÓ FRISSÍTÉSE**

**Mi a kötelezettség:**
Ha AI-t használsz, amely személyes adatokat dolgoz fel, ezt **írásban közölni kell** az érintettekkel.

**Példa (webshop ügyfélszolgálati chatbot):**

```markdown
## Adatkezelési Tájékoztatónk frissítése - AI használat

Weboldalunk mesterséges intelligencia (AI) alapú chatbotot
használ ügyfélszolgálati célokra.

AI szolgáltató: OpenAI Inc. (ChatGPT-4)

Milyen adatokat dolgoz fel az AI:
 - Név (ha megadod)
 - Email cím (ha megadod)
 - Beszélgetés szövege

Adatfeldolgozás helye: EU-n belül (GDPR compliant)

Adatmegőrzés: 30 nap, utána automatikus törlés

Jogaid:
 - Hozzáférés: kérheted az AI-ról rögzített beszélgetésedet
 - Törlés: kérheted azonnali törlést
 - Tiltakozás: kérheted, hogy ne AI válaszoljon, hanem ember

Kapcsolat adatvédelmi kérdésekben: gdpr@cegnev.hu
```

**Határidő:** Ha már használsz AI-t: AZONNAL frissítsd!

**Bírság ha nincs:** GDPR 13. cikk megsértése → 10M EUR vagy 2% forgalom

---

### **2. DATA PROCESSING AGREEMENT (DPA) MEGKÖTÉSE**

**Mi az a DPA:**
Adatfeldolgozási megállapodás - szerződés közted (adatkezelő) és az AI szolgáltató (adatfeldolgozó) között.

**GDPR 28. cikk követelménye:**
Minden külső szolgáltatóval (aki személyes adatokat dolgoz fel) írásban kell szerződni.

**Hogyan:**
- **ChatGPT/OpenAI:** Admin panelon belül van DPA aláírási lehetőség
- **Claude/Anthropic:** support@anthropic.com email → DPA kérés
- **Google Bard/Gemini:** Google Workspace admin console → DPA

**Mit tartalmaz:**
- Adatfeldolgozás célja, időtartama
- Adat biztonsági intézkedések
- Al-feldolgozók listája (subprocessors)
- Audit jogok
- Adattörlési garancia

**Határidő:** AI szolgáltatás élesítése ELŐTT!

**Bírság ha nincs:** GDPR 28. cikk megsértése → 10M EUR vagy 2% forgalom

---

### **3. ADATVÉDELMI HATÁSVIZSGÁLAT (DPIA) ELVÉGZÉSE**

**Mikor kötelező:**
Ha AI használatod **nagy kockázatú** (GDPR 35. cikk), pl.:
- Automatizált döntéshozatal (hitelelbírálás, álláspályázat szűrés)
- Nagy léptékű személyes adatok feldolgozása
- Érzékeny adatok (egészségügyi, biometrikus)

**Magyar KKV példák, amikor KELL:**
- ❌ Chatbot ügyfélszolgálat (csak név/email) → NEM kell DPIA
- ✅ AI alapú CV szűrés 500+ pályázatból → KELL DPIA
- ✅ AI arcfelismerés beléptető rendszer → KELL DPIA
- ✅ AI egészségügyi tanácsadó app → KELL DPIA

**Mit tartalmaz a DPIA:**
1. AI rendszer leírása (mit csinál, hogyan)
2. Adatfeldolgozás szükségessége és arányossága
3. Kockázatok felsorolása (mi mehet rosszul)
4. Kockázatcsökkentő intézkedések (hogyan védjük)
5. Érintettek és stakeholderek bevonása

**Kinek kell csinálnia:**
Adatvédelmi tisztviselő (DPO) vagy külső GDPR tanácsadó

**Határidő:** AI rendszer élesítése ELŐTT!

**Bírság ha nincs (de kellett volna):** GDPR 35. cikk megsértése → 10M EUR vagy 2% forgalom

---

### **4. AUTOMATIZÁLT DÖNTÉSHOZATAL TÁJÉKOZTATÁSA**

**Mi az automatizált döntés:**
Amikor **AI dönt helyetted emberi beavatkozás nélkül** és ez **jogkövetkezménnyel jár** az érintettre.

**Magyar példák:**
- ✅ AI eldönti: hitelkérelmet elutasít → AUTOMATIZÁLT DÖNTÉS
- ✅ AI eldönti: álláspályázót nem hív be interjúra → AUTOMATIZÁLT DÖNTÉS
- ❌ AI ajánl termékeket (de vevő dönt) → NEM automatizált döntés
- ❌ AI draftolja az emailt (de ember küldi el) → NEM automatizált döntés

**GDPR 22. cikk kötelezettség:**
1. **Tájékoztasd** az érintettet, hogy AI döntött róla
2. **Biztosítsd** az emberi felülvizsgálat lehetőségét
3. **Add meg** a logikát: hogyan döntött az AI (transparent AI)

**Gyakorlati megvalósítás:**

```markdown
## Tájékoztató - AI alapú döntéshozatal

Hitelkérelmének elbírálásában mesterséges intelligencia
(AI) rendszert alkalmazunk.

Az AI a következő adatok alapján értékeli:
 - Jövedelem
 - Hitelsztori
 - Meglévő tartozások

Ha az AI elutasító döntést hoz, Önnek JOGA van:
 1. Emberi felülvizsgálatot kérni (3 munkanapon belül)
 2. Megismerni a döntés indokát
 3. Saját álláspontját kifejteni

Kapcsolat: hitel-felulvizsgalat@bank.hu
```

**Határidő:** Döntés ELŐTT tájékoztatni!

**Bírság ha nincs:** GDPR 22. cikk megsértése → 20M EUR vagy 4% forgalom

---

## 🇪🇺 AI ACT: MAGYAR CÉGEK ÚJ KÖTELEZETTSÉGEI

### **AI Act Kockázati Kategóriák**

Az AI Act **kockázat alapú** - minél veszélyesebb az AI, annál több a követelmény.

| Kategória | Példa | Magyar KKV érintett? | Fő kötelezettség |
|-----------|-------|----------------------|------------------|
| **Tiltott** | Szociális pontozás, manipuláció | NEM (senki nem csinálhat) | Tiltás |
| **Magas kockázat** | CV szűrés AI, hitel scoring, biometrikus azonosítás | IGEN (ha ilyet használsz) | Regisztráció + audit + dokumentáció |
| **Korlátozott kockázat** | Chatbotok, deepfake | IGEN (sok cég) | Transzparencia (jelezni kell, hogy AI) |
| **Minimális kockázat** | AI spam filter, termékajánló | IGEN (legtöbb) | Nincs különös követelmény |

---

### **TRANSZPARENCIA KÖVETELMÉNY (Korlátozott kockázat)**

**Mi a kötelezettség:**
Ha chatbotot használsz, **egyértelművé kell tenni**, hogy az érintet AI-val beszél, nem emberrel.

**Példa implementáció:**

```markdown
Bot első üzenete:
"Helló! Én egy AI asszisztens vagyok, amely segít a
kérdéseidben. Ha emberi ügyfélszolgálatot szeretnél,
írd be: AGENT"
```

**Határidő:** 2025. február 2. (általános célú AI modellek szabályai)

**Bírság ha nincs:** AI Act 52. cikk megsértése → 15M EUR vagy 3% forgalom

---

### **REGISZTRÁCIÓ (Magas kockázat AI)**

**Kinek kötelező:**
Ha **magas kockázatú AI-t** használsz (hitel scoring, CV szűrés, biometria).

**Hova:**
EU AI Office adatbázis (magyar interface tervezés alatt, 2026 Q2)

**Mit kell regisztrálni:**
- AI rendszer neve, célja
- Szolgáltató neve (OpenAI, stb.)
- Kockázatelemzés összefoglalója
- Conformity assessment (megfelelési értékelés)

**Határidő:** 2027. augusztus 2. (magas kockázatú AI rendszerek teljes szabályozása)

**Bírság ha nincs:** AI Act regisztráció hiánya → 35M EUR vagy 7% forgalom

---

## 📅 HATÁRIDŐK ÁTTEKINTÉSE

| Dátum | Mi lép életbe | Kit érint |
|-------|---------------|-----------|
| **2025. február 2.** | Általános célú AI modellek szabályai (pl. ChatGPT) | Service providers (OpenAI, Anthropic) |
| **2025. augusztus 2.** | Tiltott AI rendszerek tilalma | Minden cég (de ezt már nem csináltátok úgyis) |
| **2026. augusztus 2.** | Korlátozott kockázat AI szabályok (chatbot transparency) | Magyar KKV-k, akik chatbotot használnak |
| **2027. február 2.** | Magas kockázatú AI szabályok előfutára | CV szűrő, hitelező cégek |
| **2027. augusztus 2.** | TELJES AI Act hatályba lép | MINDEN AI használó cég |

---

## 🚨 BÜNTETÉSI TÉTELEK - Mennyit kockáztatsz?

### **GDPR bírságok (aktuális magyar esetek):**

- **2023:** Magyar webshop - 1.2M Ft (nem frissítette Adatkezelési Tájékoztatót)
- **2024:** Magyar HR cég - 3.5M Ft (CV-ket AI-val dolgozták fel DPIA nélkül)

### **AI Act bírságok (várható, 2026-tól):**

| Szabálysértés | Max bírság |
|---------------|-----------|
| Tiltott AI használata | 35M EUR vagy 7% forgalom |
| Magas kockázat AI regisztráció hiánya | 35M EUR vagy 7% forgalom |
| Transzparencia hiánya (chatbot nem jelzi, hogy AI) | 15M EUR vagy 3% forgalom |
| Adatszolgáltatás megtagadása hatóságnak | 7.5M EUR vagy 1.5% forgalom |

**Magyar KKV átszámítás példa:**

Példa cég: 500M Ft éves forgalom (kb. 1.3M EUR)
- 3% bírság = 39,000 EUR = **15M Ft** (!!)

**Nem kispénz.**

---

## ✅ GYAKORLATI TEENDŐK - 90 NAPOS ACTION PLAN

### **0-30. NAP: Felmérés**

- [ ] Listázd: milyen AI-okat használ a cég
- [ ] Kategorizáld: minimális/korlátozott/magas kockázat
- [ ] Ellenőrizd: személyes adatokat dolgoz fel-e az AI

### **31-60. NAP: Dokumentáció**

- [ ] Frissítsd az Adatkezelési Tájékoztatót
- [ ] Kötsd meg a DPA-t AI szolgáltatókkal
- [ ] Ha kell: végezz DPIA-t (hire GDPR consultant)

### **61-90. NAP: Implementáció**

- [ ] Chatbot: transzparencia üzenet beépítése ("Én egy AI vagyok")
- [ ] Magas kockázat AI: regisztráció előkészítése
- [ ] Dolgozók képzése: GDPR + AI Act compliance

---

## 💼 SEGÍTSÉG - Hova fordulhatsz?

**Ingyenes:**
- [NAIH honlap - GDPR útmutatók](https://naih.hu)
- [EU AI Act hivatalos szöveg magyarul](https://eur-lex.europa.eu/legal-content/HU/)
- AI Shield magazin (ezt olvasod!) - havonta frissülő tartalmak

**Fizetős (ajánlott):**
- **GDPR tanácsadó (1-2 óra konzultáció):** 30-80k Ft
- **AI Act compliance audit:** 100-300k Ft
- **Jogászi retainer (havi):** 50-150k Ft

> ⚠️ **FONTOS JOGI NYILATKOZAT:**
>
> Ez a cikk általános tájékoztatás, NEM minősül jogi tanácsadásnak.
> Konkrét jogi kérdésekkel fordulj ügyvédhez, GDPR specialistához.

---

**Hasznos linkek:**
- [NAIH - Nemzeti Adatvédelmi Hatóság](https://naih.hu)
- [EU AI Act teljes szövege (magyar)](https://eur-lex.europa.eu/legal-content/HU/)
- [AI Shield - GDPR+AI checklist letöltése](/04_vegleges/export/GDPR_AI_Checklist.pdf)

**Kapcsolódó cikkek:**
- Vállalati Fókusz: "30 perces AI biztonsági audit - Csináld magad!"
- Vállalati Fókusz: "KKV AI biztonsági csomag 0 forintból"
- Hírek & Trendek: "Az EU AI Act hatályba lépett - Mit jelent ez magyar felhasználóknak?"
