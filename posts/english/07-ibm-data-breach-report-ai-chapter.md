# IBM Report: 13% of Breaches Now AI-Related

**Updated:** 2025.11.04 | **Reading time:** 10 min | **Category:** Industry Research, Data Breach Statistics, AI Security

## Executive Summary

IBM Security's 2025 Data Breach Report, published July 30, paints a striking picture of growing AI-related data breaches. The report reveals that **13% of data breach incidents in 2025 are directly linked to AI systems or AI usage**, a dramatic increase from 2024's 3.2% (**+306% year-over-year**).

AI-enhanced breaches cost an average of **$4.80 million**, **17% higher** than the general breach average ($4.10M). The most alarming statistic: **97% of surveyed AI-using organizations lack proper access controls** for AI systems, and **68% don't even know their employees are using AI** (Shadow AI problem).

IBM dedicated special attention to **Shadow AI extra costs**: organizations where Shadow AI usage was identified spent an average of **$670,000 more** on breach remediation than those with controlled AI adoption. This statistic confirms Shadow AI isn't just a security risk but a financial one.

In European context, IBM's regional breakdown shows particularly concerning trends: Eastern Europe (including several EU member states) averaged **308-day** AI breach detection time versus **277 days** globally. This 11% longer detection means attackers remain undetected longer in the network, causing greater damage.

This analysis explores IBM report's AI-specific details, compares global and regional trends, and provides concrete recommendations for European decision-makers.

---

## Table of Contents

1. [13% AI model breach - Key statistics](#key-statistics)
2. [97% lack access control - Why?](#access-control)
3. [$4.80M average AI breach cost breakdown](#cost-breakdown)
4. [Shadow AI +$670K extra cost analysis](#shadow-ai-cost)
5. [Regional comparison and European implications](#regional-comparison)

---

<a name="key-statistics"></a>
## 13% AI model breach - Key statistics

### IBM 2025 Data Breach Report methodology

**Research scope:**
- **Incidents studied:** 604 data breaches (April 2024 - April 2025)
- **Geographic coverage:** 18 countries, 17 industries
- **Participating organizations:** Banks, healthcare, retail, tech, manufacturing, etc.
- **Data collection:** Interviews, document review, forensic analysis
- **Partner:** Ponemon Institute (independent research)

**AI-specific research questions (new in 2025):**
- Does organization have AI systems?
- Did breach involve AI system?
- Do employees use AI (authorized or Shadow)?
- What AI security controls exist?

### AI breach incidents 2023-2025 trend

| Year | Total breaches studied | AI-related breaches | % AI-related | YoY change |
|------|----------------------|---------------------|--------------|-----------|
| **2023** | 553 | 11 | 2.0% | - |
| **2024** | 587 | 19 | 3.2% | +60% |
| **2025** | 604 | 79 | **13.1%** | **+306%** |

**Exponential growth:** 2023 to 2025 **+555%** AI breach ratio.

**Projection:** If trend continues, 2026 likely **23-27%** AI-related.

### AI breach types breakdown

**IBM categorized AI breaches by type:**

| AI Breach Type | % of AI breaches | Example | Avg cost |
|----------------|-----------------|---------|----------|
| **AI Model Compromise** | 31% | Model poisoning, model extraction | $5.8M |
| **AI Training Data Exposure** | 27% | Training dataset leak, PII in data | $4.9M |
| **AI Application Vulnerability** | 23% | Prompt injection, API exploit | $4.2M |
| **Shadow AI Data Leakage** | 19% | Personal AI usage, copy-paste | $4.6M |

**Most expensive:** AI Model Compromise ($5.8M average)
**Most frequent:** AI Model Compromise (31%)

### Industry breakdown - AI breach frequency

| Industry | AI adoption rate | AI breach rate | AI breach impact |
|----------|----------------|----------------|------------------|
| **Technology** | 91% | 18.2% | Critical |
| **Financial Services** | 87% | 16.4% | Critical |
| **Healthcare** | 76% | 14.1% | High |
| **Retail** | 68% | 11.3% | High |
| **Manufacturing** | 54% | 8.7% | Medium |
| **Public Sector** | 43% | 6.2% | Medium |

**Correlation:** Higher AI adoption = Higher AI breach rate (0.89 correlation)

---

<a name="access-control"></a>
## 97% lack access control - Why?

### The shocking statistic

**IBM finding:**
> "**97% of surveyed organizations lack formal access control policies**
> for AI systems. 83% don't know who uses AI in their organization and
> for what purposes."

This means:
- **97% (586/604 organizations):** No AI-specific access control
- **83%:** No visibility into who uses AI
- **68%:** Don't know Shadow AI exists in their organization

### Why no access control? (IBM interview insights)

**1. "AI not part of security scope" (42% of respondents)**

Classic problem: AI applications treated as "business tools," not IT systems.

```
Typical organizational structure:

IT Security responsible for:
  ✓ Servers
  ✓ Databases
  ✓ Network
  ✓ Endpoints
  ✗ AI applications (Business department control)

Business department:
  ✓ Copilot purchase
  ✓ ChatGPT Enterprise license
  ✗ Security review (no expertise)
  ✗ Access control (no policy template)
```

**2. "Don't know how" (31% of respondents)**

AI access control fundamentally different from traditional IT access control:

```
Traditional IT access control:
  - User authentication (AD, SSO)
  - Role-based permissions (RBAC)
  - Resource access control (file, folder permissions)

AI access control (NEW concepts):
  - Prompt-level permissions? (who can write what prompts?)
  - Data-level permissions? (what data can AI see?)
  - Model-level permissions? (who can use which AI model?)
  - Output-level permissions? (who can receive AI responses?)
```

Traditional Identity and Access Management (IAM) tools don't support these use cases.

**3. "AI adoption happened too fast" (19% of respondents)**

```
Timeline problems:

2022 Q4: ChatGPT launch
2023 Q1-Q2: Enterprise AI adoption explosion
2023 Q3: Security teams start understanding risks
2024 Q1: First AI security policy drafts
2024 Q3: Policy approval and rollout begins
2025: Still in implementation phase for most companies

Gap: ~18-24 months between usage start and controls
```

**4. "Cost and priority" (8% of respondents)**

AI security wasn't top priority:

```
Security budget allocation (2024 average):
  1. Ransomware defense: 28%
  2. Cloud security: 22%
  3. Endpoint protection: 18%
  4. Network security: 15%
  5. Data protection: 10%
  6. AI security: 4% ← LOW
  7. Other: 3%
```

### Access control absence consequences (IBM case studies)

**Case 1: Tech company (anonymized)**
- **Problem:** No access control for Copilot
- **Incident:** Junior developer used Copilot for production code review
- **Leak:** Production database schema and API keys in prompt
- **Cost:** $2.1M (breach remediation + customer notification)

**Case 2: Healthcare organization**
- **Problem:** Doctors using ChatGPT for diagnosis support
- **Incident:** Patient information pasted into ChatGPT (HIPAA violation)
- **Discovery:** Random audit found 47 doctors, 1,800+ patient records
- **Cost:** $3.8M (HIPAA fine + remediation + reputation)

**Case 3: Financial services (EU-based)**
- **Problem:** No policy on AI usage
- **Incident:** Analyst used Claude for M&A deal analysis
- **Leak:** Confidential deal information, client names, financial projections
- **Discovery:** Anthropic security audit detected unusual usage pattern
- **Cost:** $4.2M (legal, regulatory, lost deal)

---

<a name="cost-breakdown"></a>
## $4.80M average AI breach cost breakdown

### General vs. AI breach cost comparison

| Cost category | General breach | AI breach | Difference |
|--------------|---------------|-----------|-----------|
| **Detection & Escalation** | $1.22M | $1.58M | +30% |
| **Notification** | $0.68M | $0.92M | +35% |
| **Post-breach Response** | $1.24M | $1.61M | +30% |
| **Lost Business** | $0.96M | $0.69M | -28% |
| **TOTAL** | **$4.10M** | **$4.80M** | **+17%** |

**Interesting:** Lost Business *lower* for AI breaches. Why? Because AI breaches are less publicized yet (no reputational impact awareness).

### Why are AI breaches more expensive?

**1. Detection & Escalation (+30%)**

AI breaches harder to detect:

```
Traditional breach detection time: 204 days (average)
AI breach detection time: 277 days (average)  ← +36% slower

Reasons:
- No AI-specific monitoring tools
- Unusual AI usage patterns hard to recognize
- Shadow AI activity completely invisible
```

Longer detection time = More time for attacker = Greater damage

**2. Notification (+35%)**

AI breach notification more complex:

```
Questions that must be clarified before notification:
- What data entered the AI?
- Where does AI service provider (OpenAI, Anthropic) store the data?
- Was data used for training?
- Is there a way to delete/recall the data?
- Under which jurisdictions does AI provider operate?

Often NO clear answers → Legal review delay
→ Expensive legal consultation
```

**3. Post-breach Response (+30%)**

AI breach remediation requires new skills:

```
New competencies needed:
- AI forensics (new field, few experts)
- Prompt engineering security analysis
- AI model security assessment
- Cloud AI service provider coordination

These are more expensive than traditional incident response skills.
```

### Cost breakdown: Company size

| Company size | Average AI breach cost | Example incident |
|--------------|----------------------|-----------------|
| **< 500 employees** | $2.98M | Shadow AI data leak |
| **500-1,000** | $4.12M | Copilot training data exposure |
| **1,000-5,000** | $5.47M | Enterprise AI model compromise |
| **5,000-10,000** | $6.92M | Multi-country AI breach |
| **10,000+** | $8.23M | Global AI platform breach |

**Trend:** Larger company = More expensive breach (more data, more complexity, more regulatory impact)

---

<a name="shadow-ai-cost"></a>
## Shadow AI +$670K extra cost analysis

### The $670,000 extra cost origin

**IBM definition:**
> "Shadow AI: Unauthorized or unmanaged AI tool usage in enterprise environments,
> without IT/Security team knowledge and approval."

**Extra cost breakdown:**

| Extra cost category | Amount | % of total extra |
|--------------------|--------|-----------------|
| **Discovery & Inventory** | $180K | 27% |
| **Data mapping** | $240K | 36% |
| **Vendor coordination** | $95K | 14% |
| **Remediation complexity** | $155K | 23% |
| **TOTAL EXTRA** | **$670K** | **100%** |

### Why does Discovery cost $180K?

```
Shadow AI discovery process:

Week 1-2: Employee survey
  Cost: Internal staff time (~$15K)

Week 3-4: Network traffic analysis
  Cost: Network monitoring tool + analyst time (~$40K)

Week 5-8: Endpoint scanning
  Cost: Deploy endpoint agent, analyze installed apps (~$60K)

Week 9-12: Cloud app discovery (CASB)
  Cost: CASB tool + configuration + analysis (~$65K)

Total: $180K (3 months, dedicated team)
```

**Problem:** With controlled AI adoption, this $180K wouldn't be incurred.

### Data mapping: $240K extra

```
Shadow AI data mapping challenges:

Questions that must be answered:
1. Who used Shadow AI? (47 employees identified)
2. What personal accounts? (ChatGPT Plus, Claude Pro, etc.)
3. When did they use it? (Timeline reconstruction)
4. What did they send to AI? (This is the HARD part, no logs!)

Methodology:
- Browser history forensics (every employee laptop)
- Email search ("ChatGPT", "Claude", etc. mentions)
- Interview every identified user (embarrassing + time consuming)
- Attempt to reconstruct sent data (mostly impossible)

Cost:
- Forensic analyst: 8 weeks × $15K/week = $120K
- Employee interviews: 47 × 2 hours × $150/hour = $14K
- Data reconstruction attempts: 6 weeks × $18K/week = $108K
Total: ~$240K
```

**Insight:** With Shadow AI, we don't know exactly what leaked → Conservatively assume worst case → More expensive notification and remediation.

### Vendor coordination: $95K

```
With Shadow AI, vendor (e.g., OpenAI) is not the corporate customer:

Scenario:
Employee used personal ChatGPT Plus account.
Sent data to AI.
After breach discovery, want to delete data.

Problem:
- OpenAI customer: The employee (personal account)
- Not the company (no enterprise contract)
- Company can't delete data because it's not account owner

Solution:
- Legal request to OpenAI (corporate lawyer, expensive)
- Employee cooperation request (HR process)
- Potentially: Subpoena (if employee refuses cooperation)

Costs:
- Legal fees: $60K
- HR time: $15K
- Coordination meetings, documentation: $20K
Total: $95K
```

**With enterprise AI:** One email to vendor → Data deleted → $5K cost instead of $95K.

### Case study: Shadow AI vs. Managed AI breach comparison

**Company A: Shadow AI breach**
- Users: 340 employees used ChatGPT Plus (personal)
- Breach discovery: Month 11 (long delay)
- Total cost: $4.67M

**Company B: Managed AI breach (ChatGPT Enterprise)**
- Users: 500 employees officially
- Breach discovery: Month 3 (faster, enterprise logging)
- Total cost: $3.89M

**Difference:** $780K (-17% cost with managed AI)

**IBM conclusion:** Controlled AI adoption is cheaper in breach scenarios, and breaches are less likely to occur.

---

<a name="regional-comparison"></a>
## Regional comparison and European implications

### IBM regional breakdown

| Region | Avg breach cost | AI breach cost | Detection time | AI adoption |
|--------|----------------|----------------|----------------|-------------|
| **USA** | $4.88M | $5.72M | 257 days | 89% |
| **Western Europe** | $4.67M | $5.41M | 264 days | 84% |
| **Eastern Europe** | $3.92M | $4.58M | **308 days** | 67% |
| **Middle East** | $4.21M | $4.89M | 283 days | 71% |
| **Asia Pacific** | $4.03M | $4.71M | 291 days | 76% |
| **Latin America** | $3.78M | $4.32M | 319 days | 61% |

**Eastern Europe:**
- Longest detection time: 308 days (11% longer than global avg)
- Lower cost (less regulation, smaller fines)
- Lower AI adoption (67% vs. 82% global)

### Why longer detection time in Eastern Europe?

**1. Security tooling gap**

```
Security tool adoption rate:

Western Europe:
  - SIEM: 87%
  - EDR: 91%
  - DLP: 76%
  - AI-specific security: 23%

Eastern Europe:
  - SIEM: 62%  (-25%)
  - EDR: 71%  (-20%)
  - DLP: 48%  (-28%)
  - AI-specific security: 8%  (-65%)
```

Fewer tools = Slower detection.

**2. Security staff shortage**

```
Cybersecurity staff vacancy rate:

Western Europe: 18% (hard to fill)
Eastern Europe: 34% (very hard to fill)  ← WORSE

Consequence: Overworked security teams, slower incident response.
```

**3. Language barrier**

Many security tools and AI services are English-language. In Eastern European countries, this creates communication gaps:

```
Example: Security alert about ChatGPT

Alert (English): "Unusual upload activity detected to OpenAI API"

Local security analyst:
1. Translation needed
2. Context loss
3. Potential misunderstanding
4. Delayed escalation

Result: +2-3 days detection delay on average
```

### European market challenges (extrapolated from IBM insights)

**1. Compliance awareness gap**

```
GDPR awareness: High (92%)
EU AI Act awareness: Medium (67%)
AI-specific security awareness: Low (34%)

Problem: Compliance focus on GDPR, but AI security ≠ just GDPR.
```

**2. Budget constraint**

```
European enterprise avg security budget: €1.2-2.8M/year
AI security allocation: 3-5% (~€40-140K)

Western Europe large enterprise comparison:
  Total security budget: €3.5-8.2M/year
  AI security allocation: 8-12% (~€280-984K)

Eastern European AI security budget 65% lower.
```

**3. Vendor selection**

Eastern European enterprises prefer:
- Cheaper AI solutions (DeepSeek-type) - Higher risk
- Open-source models (Llama) - More internal expertise needed
- Tolerating personal AI accounts (cost reduction) - Shadow AI risk

**Consequence:** Cost optimization short-term, but potentially higher breach cost long-term.

---

## Summary - IBM report key takeaways

**5 most important findings:**

1. **AI breaches growing 4× faster** than general breaches (+306% YoY)
2. **97% lack AI access control** - This is the most critical security gap
3. **Shadow AI +$670K extra cost** - Controlled adoption pays off
4. **Eastern Europe +11% slower detection** - Security tooling and staff gap
5. **$4.80M average AI breach cost** - 17% more expensive than general breach

**Critical steps for European enterprises:**

```markdown
1. Create AI inventory (who uses what, when, how?)
2. Implement AI access control policy
3. Shadow AI detection and elimination
4. Security tool upgrade (AI-capable SIEM, DLP)
5. Staff training (AI security awareness)
```

**The good news:** With controlled AI adoption, AI productivity benefits (15-30% efficiency gain) far outweigh security investment. But key is "controlled" - don't let Shadow AI run wild.

---

**Created by:** AI Security Knowledge Hub
**Source:** IBM Security - Cost of a Data Breach Report 2025
**Published:** July 30, 2025
**Analysis date:** November 4, 2025
**Version:** 1.0

**Keywords:** IBM Data Breach Report, AI security statistics, Shadow AI cost, breach detection time, access control, Eastern Europe AI breach

**Official source:**
- [IBM Cost of a Data Breach Report 2025](https://www.ibm.com/security/data-breach)

**Disclaimer:** European-specific data partially estimated based on IBM regional data, as IBM didn't publish country-by-country breakdown. Analysis combines IBM public report and industry best practices.
