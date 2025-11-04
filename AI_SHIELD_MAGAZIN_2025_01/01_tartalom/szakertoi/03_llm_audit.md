---
title: "LLM biztonsági audit módszertan"
category: "Szakértői Műhely"
readTime: "10 perc"
difficulty: "Expert"
tags: ["audit", "testing", "MITRE ATT&CK", "security assessment"]
---

## LLM biztonsági audit módszertan

Átfogó audit framework LLM alkalmazásokhoz.

### Pre-deployment Tesztek
- Prompt injection teszt suite (100+ variáció)
- Data leakage testing
- Model behavior consistency
- Input sanitization verification

### Runtime Monitoring
- Anomaly detection (deviation from baseline)
- Token usage patterns
- Failed authentication tracking
- Suspicious input flagging

### MITRE ATT&CK Mapping
LLM-specifikus attack matrix használata

**Python Audit Script:**
```python
def audit_llm_app(api_endpoint):
    results = {}
    results['injection'] = test_prompt_injection(api_endpoint)
    results['data_leak'] = test_data_leakage(api_endpoint)
    results['rate_limit'] = test_rate_limiting(api_endpoint)
    return generate_report(results)
```

### Post-incident Analysis
- Root cause analysis
- Timeline reconstruction
- Remediation verification

---
**Kapcsolódó:** Szakértői - Prompt injection védelem
