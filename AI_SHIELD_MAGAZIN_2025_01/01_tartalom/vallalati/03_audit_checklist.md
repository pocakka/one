---
title: "30 perces AI biztonsági audit - Csináld magad!"
category: "Vállalati Fókusz"
readTime: "10 perc olvasás + 30 perc audit"
difficulty: "Haladó"
keyPoints:
  - Gyors, önállóan végrehajtható AI security checklist
  - 30 pontős ellenőrző lista 4 kategóriában
  - Pontozási rendszer: Zöld/Sárga/Piros
  - Azonnal action plan a hiányosságokra
tags: ["audit", "checklist", "DIY", "gyors értékelés", "KKV"]
author: "AI Shield Szerkesztőség"
date: "2025 Január"
---

## 30 perces AI biztonsági audit - Csináld magad!

*Nem kell drága external auditor - ezt a basic AI security check-et bármelyik KKV IT felelőse (vagy ügyvezető) meg tudja csinálni 30 perc alatt. Eredmény: konkrét pontszám és action plan.*

---

## HOGYAN HASZNÁLD EZT A CHECKLIST-ET?

1. **Időzítés:** Blokkol ki 30 percet, amikor nem zavarnak
2. **Eszközök:** Laptop, hozzáférés céges rendszerekhez, jegyzetfüzet
3. **Pontozás:** Minden kérdésnél jelöld: ✅ (megvan), ⚠️ (részben), ❌ (nincs)
4. **Végén:** Számold ki a pontokat, nézd meg a kategóriádat

**Pontozás:**
- ✅ = 1 pont
- ⚠️ = 0.5 pont
- ❌ = 0 pont

---

## 📋 CHECKLIST - 4 KATEGÓRIA

---

### 🔐 ALAPOK (10 pont)

| # | Kérdés | Ellenőrzés módja | Pont |
|---|--------|------------------|------|
| 1 | Van írásos AI használati szabályzatunk? | Dokumentum létezik + dolgozók ismerik? | [ ] |
| 2 | AI eszközök listája dokumentálva? | Excel/Notion lista: milyen AI-okat használunk? | [ ] |
| 3 | Minden dolgozó aláírta az AI policy-t? | HR mappa check | [ ] |
| 4 | AI képzésen részt vettek a dolgozók (legalább 1 óra)? | Képzési jelenlét lista | [ ] |
| 5 | Van kijelölt AI felelős személy? | Ki az, aki "AI security officer"? | [ ] |
| 6 | ChatGPT/Claude fiók business/team előfizetés (nem ingyenes)? | Fiók típus ellenőrzés | [ ] |
| 7 | ChatGPT "Data Training" opció KI van kapcsolva? | Settings → Data Controls | [ ] |
| 8 | Céges email domain használata AI regisztrációhoz (@cegnev.hu)? | Fiókok ellenőrzése | [ ] |
| 9 | Multi-factor authentication (MFA) bekapcsolva minden AI fióknál? | Próbáld meg belépni - kér-e 2FA kódot? | [ ] |
| 10 | Rendszeres jelszóváltás (legalább 6 havonta)? | Mikor volt utoljára? | [ ] |

**Alapok pontszám:** ___ / 10

---

### 🛡️ ADATVÉDELEM (8 pont)

| # | Kérdés | Ellenőrzés módja | Pont |
|---|--------|------------------|------|
| 11 | Listázva van, milyen adatok NEM oszthatók meg AI-val? | Van blacklist dokumentum? | [ ] |
| 12 | Ügyfél személyes adatok soha nem kerülnek AI-ba? | Random sample check: utolsó 10 AI chat history | [ ] |
| 13 | Anonimizálási folyamat létezik érzékeny adatokhoz? | Van protocol hogyan anonimizálunk? | [ ] |
| 14 | Data Processing Agreement (DPA) aláírva AI szolgáltatóval? | OpenAI/Anthropic DPA megvan? | [ ] |
| 15 | GDPR compliance audit elvégezve AI használatra? | Dokumentum vagy külső audit jelentés | [ ] |
| 16 | Ügyfél adatok törlési kérelme kezelhető AI kontextusban is? | Van protocol hogyan törlünk AI history-ból? | [ ] |
| 17 | AI által generált tartalom nem tartalmaz ügyfél adatokat? | Ellenőrizz 5 AI-generált emailt/dokumentumot | [ ] |
| 18 | Céges titkok (szerződések, IP) nem kerülnek AI-ba? | Dolgozók tudják: mit tilos megosztani? | [ ] |

**Adatvédelem pontszám:** ___ / 8

---

### 🔒 HOZZÁFÉRÉSEK ÉS JOGOSULTSÁGOK (7 pont)

| # | Kérdés | Ellenőrzés módja | Pont |
|---|--------|------------------|------|
| 19 | API kulcsok biztonságos helyen tárolva (jelszókezelő, vault)? | Nem plain text fájlban vagy GitHub-on? | [ ] |
| 20 | API kulcsok rendszeres rotációja (legalább évente)? | Mikor generáltuk az aktuális kulcsot? | [ ] |
| 21 | Role-based access: nem mindenki admin az AI fiókokon? | Ki milyen jogosultsággal rendelkezik? | [ ] |
| 22 | Kilépett dolgozók AI hozzáférése azonnal visszavonva? | Van offboarding checklist AI-ra is? | [ ] |
| 23 | Rate limiting beállítva (API költségek kontrollja)? | OpenAI dashboard: van-e usage limit? | [ ] |
| 24 | Shared AI fiókok esetén ki látja a history-t? | Privacy szabályozva? | [ ] |
| 25 | Külső contractor/freelancer NEM használ AI-t céges adatokkal? | Szerződésben benne van ez a tiltás? | [ ] |

**Hozzáférések pontszám:** ___ / 7

---

### 📊 MONITORING ÉS DOKUMENTÁCIÓ (5 pont)

| # | Kérdés | Ellenőrzés módja | Pont |
|---|--------|------------------|------|
| 26 | AI usage logging aktív (ki, mikor, mit használt)? | Van log file vagy dashboard? | [ ] |
| 27 | Havi AI usage review meeting megtartva? | Naptárban látható recurring event? | [ ] |
| 28 | Incident response protocol létezik AI incidensekre? | Dokumentum: mi a teendő ha AI baj van? | [ ] |
| 29 | Biztonsági incidens (bármilyen) 24 órán belül jelentve? | Van jelentési csatorna (email, chat)? | [ ] |
| 30 | AI cost tracking (mennyit költünk havonta AI-ra)? | Tudjuk a pontos összeget? | [ ] |

**Monitoring pontszám:** ___ / 5

---

## 🎯 ÖSSZESÍTÉS ÉS ÉRTÉKELÉS

### Számold ki az össz pontszámodat:

- Alapok: ___ / 10
- Adatvédelem: ___ / 8
- Hozzáférések: ___ / 7
- Monitoring: ___ / 5

**ÖSSZESEN: ______ / 30**

---

## 📈 KATEGÓRIA MEGHATÁROZÁS

### 🟢 ZÖLD ZÓNA (25-30 pont) - KIVÁLÓ

**Értékelés:**
Gratulálunk! Az AI biztonsági helyzetetek jóval az átlag felett van. A legtöbb alapvető és haladó biztonsági gyakorlatot alkalmazz átok.

**Javasolt következő lépések:**
- [ ] 6 havonta ismételd meg ezt az auditot
- [ ] Fontold meg external penetration testet (professzionális audit)
- [ ] Oszd meg a best practice-eket más KKV-kkal (esetleg blog post?)

**Benchmark:** Top 15% magyar KKV-k között vagytok AI biztonságban.

---

### 🟡 SÁRGA ZÓNA (15-24 pont) - KÖZEPESEN JÓ, DE VAN MIT JAVÍTANI

**Értékelés:**
Alapok megvannak, de van néhány kritikus hiányosság. Nem vagy azonnali veszélyben, de 3-6 hónapon belül fejleszteni kell.

**Javasolt következő lépések:**
1. **Prioritizálj:** Nézd meg, melyik kategóriában a leggyengébb (Alapok/Adatvédelem/Hozzáférések/Monitoring)
2. **30 napos action plan:** Válaszd ki a 3 legkritikusabb hiányzó elemet (❌ vagy ⚠️), és javítsd ki 30 napon belül
3. **Képzés:** Fókuszálj dolgozói AI security képzésre (lásd: "KKV AI biztonsági csomag 0 forintból" cikk)

**Példa Action Plan:**
- Ha "Adatvédelem" gyenge: GDPR audit + DPA aláírás → 2 hét
- Ha "Monitoring" gyenge: Logging setup → 1 hét

**Benchmark:** Átlag magyar KKV szintjén vagytok.

---

### 🔴 PIROS ZÓNA (0-14 pont) - KRITIKUS, AZONNALI CSELEKVÉS KELL

**Értékelés:**
Komoly biztonsági hiányosságok vannak. Akár már most is lehet aktív kockázat (adatszivárgás, GDPR sértés, költségtúllépés).

**AZONNALI TEENDŐK (48 órán belül!):**

1. **STOP minden AI használatot**, amíg minimum biztonsági intézkedések nincsenek
2. **Sürgős meeting:** IT + management + HR - "AI security emergency"
3. **Quick wins (1 hét alatt):**
   - [ ] ChatGPT Data Training KI
   - [ ] MFA BE minden AI fióknál
   - [ ] Írásban közöld dolgozókkal: "Mi NEM osztható meg AI-val" (email)
   - [ ] API kulcsok password manager-be áthelyezés

4. **30 napos terv:**
   - [ ] AI használati szabályzat megírása (használd magazin sablonunkat)
   - [ ] Dolgozók aláírása
   - [ ] Alapvető logging setup

5. **90 napos terv:**
   - [ ] GDPR audit
   - [ ] Képzés dolgozóknak
   - [ ] Monitoring rendszer kiépítése

**Figyelm:** Ha 14 pont alatt vagy, fontold meg külső consultant-ot (1-2 napos intenzív audit, 100-300k Ft - megéri).

**Benchmark:** Alsó 20% - komoly kockázat alatt vagytok.

---

## 🔧 HIÁNYOSSÁGOK JAVÍTÁSA - GYORS TIPPEK

### Ha "Alapok" kategória gyenge:

**Leggyakoribb problémák:**
- Nincs AI policy → **Megoldás:** Használd magazinunk sablon szabályzatát (letölthető)
- Nincs képzés → **Megoldás:** 4 hetes képzési terv (lásd: "KKV AI csomag 0 Ft-ból")
- Ingyenes ChatGPT használat → **Megoldás:** Válts Team előfizetésre (munkavédelem + jobb adatvédelem)

**Időigény:** 1-2 hét
**Költség:** 20-100k Ft (főleg előfizetések)

---

### Ha "Adatvédelem" kategória gyenge:

**Leggyakoribb problémák:**
- Nem tudják, mit tilos megosztani → **Megoldás:** Készíts "Piros Lista"-t (lásd sablon)
- Nincs DPA → **Megoldás:** OpenAI/Anthropic admin panel-ben van DPA aláírási lehetőség
- GDPR audit hiányzik → **Megoldás:** Hire GDPR consultant 1 napra (50-100k Ft)

**Időigény:** 2-3 hét
**Költség:** 50-150k Ft

---

### Ha "Hozzáférések" kategória gyenge:

**Leggyakoribb problémák:**
- API kulcsok nem biztonságosan tárolva → **Megoldás:** Bitwarden (ingyenes 10 userig)
- Nincs role management → **Megoldás:** ChatGPT Team: admin vs. member roles
- Offboarding nincs → **Megoldás:** HR checklist + AI hozzáférések

**Időigény:** 1 hét
**Költség:** 0-20k Ft

---

### Ha "Monitoring" kategória gyenge:

**Leggyakoribb problémák:**
- Nincs logging → **Megoldás:** ChatGPT Team admin dashboard már mutatja usage-t
- Nincs cost tracking → **Megoldás:** OpenAI/Anthropic dashboard + monthly budget alert
- Nincs incident protocol → **Megoldás:** Sablon incident response plan (magazinban)

**Időigény:** 1-2 hét
**Költség:** 0 Ft (alap eszközök ingyenesek)

---

## 📄 PIROS LISTA SABLON - "Mit NEM oszthatunk meg AI-val"

Nyomtasd ki és tedd ki az irodában látható helyre!

```
┌─────────────────────────────────────────────┐
│   🚫 TILOS MEGOSZTANI AI-VAL 🚫              │
│   [Cég neve] - AI Használati Tiltások       │
└─────────────────────────────────────────────┘

❌ SZEMÉLYES ADATOK:
 - Ügyfelek neve + címe/telefonja együtt
 - TAJ szám, személyi szám, útlevél szám
 - Bankszámla, hitelkártya adatok

❌ CÉGES TITKOK:
 - Szerződések teljes szövege
 - Árkalkulációk, beszállítói árak
 - Még nem publikált termék tervek
 - Belső stratégiai dokumentumok

❌ BIZTONSÁGI ADATOK:
 - Jelszavak (bármilyen rendszerhez)
 - API kulcsok
 - Szerver konfigurációk
 - Biztonsági audit jelentések

❌ PÉNZÜGYI RÉSZLETEK:
 - Pontos cég pénzügyi helyzet
 - Beszállítók árai
 - Ügyfél fizetési szokásai

🤔 HA NEM VAGY BIZTOS: NE OSZD MEG!
Kérdezz: [AI Felelős Neve] - [email/telefon]
```

---

## 🔄 ISMÉTLÉSI GYAKORISÁG

**Ajánlott audit ciklus:**

| Pontszámod | Következő audit | Miért? |
|------------|----------------|--------|
| 25-30 (Zöld) | 6 havonta | Stabil vagy, maintenance mode |
| 15-24 (Sárga) | 3 havonta | Fejlődsz, track progress |
| 0-14 (Piros) | Havonta | Kritikus javítások tracking-je |

---

## 💾 MENTSD EL AZ EREDMÉNYED!

Dokumentáld az audit eredményét:

```
AI BIZTONSÁGI AUDIT - EREDMÉNY

Dátum: _______________
Auditor: _______________ (ki végezte)

PONTSZÁMOK:
 - Alapok: ___ / 10
 - Adatvédelem: ___ / 8
 - Hozzáférések: ___ / 7
 - Monitoring: ___ / 5
 - ÖSSZESEN: ___ / 30

KATEGÓRIA: 🟢 Zöld / 🟡 Sárga / 🔴 Piros

TOP 3 HIÁNYOSSÁG:
1. _______________________________
2. _______________________________
3. _______________________________

ACTION PLAN (következő 30 nap):
□ _______________________________
□ _______________________________
□ _______________________________

Következő audit dátuma: ___________
```

**Tipp:** Tedd ezt a fájlt verziókezelés alá (Git) vagy shared drive-ra - így évente látod a fejlődést!

---

**Hasznos linkek:**
- [Letölthető audit checklist Excel formátumban](/04_vegleges/export/AI_Audit_Checklist.xlsx)
- [Piros Lista sablon PDF](/04_vegleges/export/AI_Piros_Lista.pdf)
- [Incident Response Protocol sablon](/04_vegleges/export/AI_Incident_Protocol.pdf)

**Kapcsolódó cikkek:**
- Vállalati Fókusz: "KKV AI biztonsági csomag 0 forintból"
- Vállalati Fókusz: "Hogyan került 2 millió forintba egy prompt - Magyar KKV sztori"
- Vállalati Fókusz: "GDPR + AI Act = Mit kell tudnia magyar cégeknek?"
