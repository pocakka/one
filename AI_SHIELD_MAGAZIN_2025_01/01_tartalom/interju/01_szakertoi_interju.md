---
title: "Interjú: Dr. Kovács Anna - AI Biztonsági Vezető"
category: "Interjú"
readTime: "8 perc"
tags: ["interjú", "szakértő", "pénzügy", "enterprise"]
---

## Interjú: Dr. Kovács Anna - AI Biztonsági Vezető

*Dr. Kovács Anna (fiktív karakter) az egyik legnagyobb magyar bank AI biztonsági vezetője. 15 év cybersecurity tapasztalat, 3 év AI security specializáció. PhD információbiztonság.*

---

### 1. Hogyan kezdte az AI security területen?

**Kovács Anna:**
"2022-ben láttam, hogy a bankunk bevezetni készül egy AI chatbotot ügyfélszolgálathoz. Cybersecurity vezetőként azonnal észrevettem: ez új támadási felület. A hagyományos pentesting nem működött - kellett egy új megközelítés. Képeztem magam, MIT online kurzusok, OWASP LLM Top 10 tanulmányozása. 2023-ra már dedikált AI security csapatot építettem."

### 2. Legnagyobb kihívás 2025-ben?

**KA:**
"A gyors tempó. Minden 3 hónapban új AI funkció deployment. Fejlesztők nyomás alatt, biztonság gyakran 'később' marad. Feladatom meggyőzni őket: security nem akadály, hanem enabler. Ha biztonságos az AI, gyorsabban deployment-elhető, mert nincs post-incident cleanup."

### 3. Tanács kezdő vállalatoknak?

**KA:**
"Három dolog:
1. **Ne várj incidensig** - proaktív security from day one
2. **Képezd a fejlesztőidet** - nem elég egy security person, everyone's job
3. **OWASP LLM Top 10** - olvassátok el, implementáljátok. Ingyenes, hatékony."

### 4. Gyakori hibák, amiket látsz?

**KA:**
"Első: **Személyes adatok AI-ba töltése ellenőrzés nélkül**. Láttam céget, ahol ügyféladatok kerültek ChatGPT-be 'hogy gyorsabb legyen' - GDPR nightmare.

Második: **API kulcsok GitHub-on**. Junior dev commit-olja, bam, havi $10k AWS bill másnap.

Harmadik: **'Majd ha nagy leszünk, lesz security'** mentalitás. Startupok gyakran halasztják - aztán Series A-nál investor due diligence megbuktat."

### 5. Budget allokáció - mennyit költsünk AI securityre?

**KA:**
"Bank esetünkben: AI security költség = 15% teljes AI projektköltségből. Átlag KKV-nál: 5-10% reális. Ha 10M Ft-ot költesz AI fejlesztésre évente, 500k-1M Ft kell security-re.

ROI egyszerű: Egyetlen adatvédelmi bírság (átlag 2-5M Ft) több, mint amit security-re költesz 3 évben."

### 6. Team building - ki kell az AI security csapatba?

**KA:**
"Ideális csapat (15-20 fős céghez):
- **1 AI Security Lead** (ez én) - strategy, oversight
- **2 Security Engineers** - hands-on implementation, monitoring
- **1 Data Protection Specialist** - GDPR compliance
- **Minden fejlesztő** - security training, shared responsibility

Kis cégnél (5-10 fő): Egy 'Security Champion' elég, aki part-time ezt csinálja + external audit évente."

### 7. Tool stack - mit használtok?

**KA:**
"Production stack:
- **Lakera AI** - prompt injection real-time detection
- **WhyLabs** - LLM observability, hallucination tracking
- **HashiCorp Vault** - secrets management
- **Splunk** - SIEM, log aggregation
- **Custom Python scripts** - rate limiting, input sanitization

Összesen: ~$3000/hó (+ internal dev time). Kis cégeknek: WhyLabs free tier + Bitwarden + nyílt forráskódú monitoring = $0-200/hó."

### 8. Jövőkép 2026-ra?

**KA:**
"AI security mainstream lesz. Ahogy 2010-ben Web Application Firewall lett standard, 2026-ban 'AI Firewall' lesz minden production AI előtt.

Látom már: Regulatory pressure nő (AI Act), insuranceok cyber policy-hoz kérik AI security proof, ügyfelek is jobban figyelnek.

Predikció: 2027-re minden magyar nagybankban lesz dedikált AI security team."

### 9. Képzési stratégia - hogyan tartjátok naprakész a csapatot?

**KA:**
"Quarterly képzés kötelező minden fejlesztőnek. External trainert hívunk (50-100k Ft/alkalom), vagy én tartom belül.

Plus: Havi 'AI Security Newsletter' - összefoglalom új támadásokat, vulnerabilities, patches. 15 perc olvasás, mindenki up-to-date.

Költés: ~500k Ft/év training. Return: 0 significant AI security incident 2 éve."

### 10. Személyes AI használat - Te magad hogy használod biztonságosan?

**KA:**
"Otthon ChatGPT Plus-t használok (saját pénzből), de SOHA nem munkaügyes dolgokat. Email-t írok AI-val, de anonimizáltan: 'Egy kolléga kérdezi...' nem 'Júlia főnököm kérdezi...'.

API kulcsaimat Bitwarden-ben. Jelszavaimat 20+ karakter, egyedi mindenhol.

Gyerekeim (12 és 15) AI-t használnak iskolához, de felügyelettel - lásd AI Shield cikkünk 'ChatGPT a házi feladatban'.

AI hasznos, ha smart használod. Én megbízom benne munkához, de verify always."

---

## Záró gondolat

**AI Shield:** Mi a #1 tanácsod olvasóinknak?

**Kovács Anna:**
"**Start now.** Ne halaszd, hogy 'majd később lesz security'. Olvasd el ezt a magazint, implementálj legalább 5 basic dolgot (MFA, Data Training OFF, input sanitization, logging, incident plan). Ez 1-2 hét, 0-100k Ft, és 90%-ot megvéd. Légy proaktív, ne reaktív."

---

**Köszönjük Dr. Kovács Annának az interjút!**

*Disclaimer: Dr. Kovács Anna fiktív karakter, de válaszai valódi enterprise AI security best practice-eken alapulnak.*

---
**Kapcsolódó:** Vállalati - KKV biztonsági csomag, Szakértői - Enterprise governance
