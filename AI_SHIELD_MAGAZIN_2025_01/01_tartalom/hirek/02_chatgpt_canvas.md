---
title: "ChatGPT Canvas funkció: Új biztonsági kihívások"
category: "Hírek & Trendek"
readTime: "2 perc"
difficulty: "Kezdő"
keyPoints:
  - OpenAI új Canvas funkciója átírja az együttműködési élményt
  - Kódvégrehajtás és dokumentumszerkesztés új kockázatokat hoz
  - Elővigyázatosság kulcsfontosságú a használatban
tags: ["ChatGPT", "Canvas", "kód biztonság", "OpenAI"]
author: "AI Shield Szerkesztőség"
date: "2025 Január"
---

## ChatGPT Canvas funkció: Új biztonsági kihívások

*Az OpenAI 2024 októberében bemutatott Canvas funkciója új szintre emelte a ChatGPT használatát: közös munkaterületet biztosít dokumentumok és kód szerkesztéséhez. De a kényelemmel együtt új biztonsági szempontok is felmerülnek.*

### Mi az újdonság?

A ChatGPT Canvas egy **interaktív szerkesztőfelület**, amely lehetővé teszi, hogy ne csak chat-ablakban, hanem egy dedikált, szerkeszthető dokumentumban dolgozzunk együtt az AI-val. Két fő használati módja van:

**Írási mód:** Hosszú szövegek, cikkek, jelentések írása közösen. Az AI javaslatokat tesz, te pedig közvetlenül szerkesztheted a Canvas-on a szöveget, kiemelve a részeket, amiket változtatni szeretnél.

**Kódolási mód:** Programkód írása, debugolása és futtatása egyetlen felületen belül. Az AI segít a hibakeresésben, optimalizálásban, sőt kommenteket is generálhat a kódhoz.

A Canvas 2024 decemberétől érhető el minden ChatGPT Plus és Team előfizetőnek, valamint 2025 januárjától Enterprise és Edu felhasználóknak is.

### Biztonsági aggályok - Mire figyeljünk?

**1. Kódfuttatás veszélyei (100 szó)**

A Canvas kódolási módjában az AI **valódi kódot futtathat** a háttérben ellenőrzéshez. Ez azt jelenti:
- Rosszul megírt kód adatvesztést okozhat
- Külső API-k hívása során érzékeny adatok szivároghatnak ki
- Infinite loop vagy memory leak megakaszthatja a szekciót

**Példa:** Egy felhasználó bekérte céges adatbázisának elemzését Canvas-ban. Az AI által generált SQL query nem tartalmazott megfelelő limiteket, és 10 GB adat letöltését kezdeményezte - több ezer dollár AWS költséget generálva.

**2. Dokumentum tartalom expozíciója (70 szó)**

Canvas dokumentumok alapértelmezetten **nem titkosítottak end-to-end módon** - az OpenAI szerverei látják a tartalmat. Ez különösen kockázatos:
- Céges bizalmas anyagok szerkesztésekor
- Személyes adatok (nevék, címek, bankszámlák) beillesztésekor
- Titoktartási szerződés alatt álló projekteknél

**3. Verziózás és visszaállítás hiánya (60 szó)**

A Canvas **nem rendelkezik beépített verziókezelő rendszerrel**. Ha az AI rossz javaslatot tesz és felülírja a munkádat, nincs "undo history".

**Történt eset:** Egy író 4000 szavas esszéjét vesztette el, amikor a Canvas véletlenül egy korábbi, 500 szavas vázlattal írta felül a dokumentumot egy szinkronizálási hiba miatt.

### Ajánlások - Hogyan használjuk biztonságosan?

**DO - Ezeket tedd:**
- ✅ **Helyi másolat mindig:** Mentsd le a fontos dokumentumokat és kódokat lokálisan, ne csak Canvas-ban dolgozz
- ✅ **Adattisztítás:** Mielőtt Canvas-ba másolsz adatokat, anonymizáld őket (cseréld ki a neveket, email címeket, stb.)
- ✅ **Kód review:** Canvas által generált kódot MINDIG ellenőrizd emberi szemmel futtatás előtt
- ✅ **Sandbox környezet:** Kódot először izolált tesztkörnyezetben futtasd, ne production-ban

**DON'T - Ezeket NE tedd:**
- ❌ **Ne írj jelszavakat, API kulcsokat** Canvas dokumentumokba
- ❌ **Ne futtass production adatbázison** közvetlenül Canvas-ban generált query-ket
- ❌ **Ne oszd meg nyilvánosan** a Canvas linkeket - alapértelmezetten privátak, de egy véletlen share katasztrofális lehet
- ❌ **Ne használd céges compliance nélkül** vállalati környezetben

> 🎯 **VESZÉLY vs. LEHETŐSÉG**

| Kockázat | Megoldás | Haszon |
|----------|----------|--------|
| Kód futtatás hibái | Sandbox tesztelés | Gyorsabb fejlesztés |
| Adat expozíció | Adat anonymizálás | Közös munka egyszerűsége |
| Verziózás hiánya | Gyakori lokális mentés | Real-time együttműködés |
| API költségek | Rate limit beállítás | Azonnali feedback |

> ⚠️ **FIGYELEM - CANVAS PRO TIPP**
>
> Használd a "Private Mode"-ot (ha elérhető): OpenAI 2025 elejétől vezeti be a ChatGPT Enterprise felhasználóknak, amely garantálja, hogy a Canvas tartalmak nem kerülnek be a model training adatokba.

---

**Hasznos linkek:**
- [OpenAI Canvas hivatalos dokumentáció](https://help.openai.com/canvas)
- [Canvas biztonsági best practices](https://platform.openai.com/docs/security)

**Kapcsolódó cikkek:**
- Kezdőknek: "Első AI asszisztensem - Lépésről lépésre biztonságosan"
- Vállalati Fókusz: "30 perces AI biztonsági audit - Csináld magad!"
