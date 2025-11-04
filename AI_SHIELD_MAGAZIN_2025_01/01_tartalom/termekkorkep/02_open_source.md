---
title: "Ingyenes és nyílt AI biztonsági eszközök"
category: "Termékkörkép"
readTime: "6 perc"
tags: ["open source", "ingyenes", "GitHub", "tools"]
---

## Ingyenes és nyílt AI biztonsági eszközök

### 1. **LangKit** by WhyLabs
- **GitHub:** https://github.com/whylabs/langkit
- **Mit csinál:** LLM monitoring, prompt injection detection, PII scanning
- **Telepítés:** `pip install langkit`
- **Use case:** Production LLM app monitoring
- **Közösség:** 2.5k stars, aktív fejlesztés

### 2. **NeMo Guardrails** by NVIDIA
- **GitHub:** https://github.com/NVIDIA/NeMo-Guardrails
- **Mit csinál:** Programmable guardrails LLM alkalmazásokhoz
- **Telepítés:** `pip install nemoguardrails`
- **Use case:** Safety constraints definiálása
- **Közösség:** 3k+ stars

### 3. **Garak** by NVIDIA
- **GitHub:** https://github.com/leondz/garak
- **Mit csinál:** LLM vulnerability scanner
- **Telepítés:** `pip install garak`
- **Use case:** Automated security testing
- **Közösség:** 1.5k stars

### 4. **PromptInject** (Research Tool)
- **GitHub:** https://github.com/agencyenterprise/PromptInject
- **Mit csinál:** Prompt injection test suite
- **Use case:** Red team testing
- **Közösség:** Research-backed

### 5. **AI Fairness 360** by IBM
- **GitHub:** https://github.com/Trusted-AI/AIF360
- **Mit csinál:** Bias detection, fairness metrics
- **Use case:** Model fairness evaluation
- **Közösség:** 2.3k stars

## Kezdő Csomag

**Docker Compose gyors start:**
```yaml
version: '3'
services:
  langkit:
    image: whylabs/langkit:latest
    ports:
      - "5000:5000"

  guardrails:
    image: nvidia/nemo-guardrails:latest
    volumes:
      - ./config:/config
```

**1 óra alatt éles monitoring!**

---
**Kapcsolódó:** Vállalati - KKV csomag 0 forintból
