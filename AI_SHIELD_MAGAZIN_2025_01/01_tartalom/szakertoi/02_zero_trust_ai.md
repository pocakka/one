---
title: "Zero Trust AI architektúra építése"
category: "Szakértői Műhely"
readTime: "10 perc"
difficulty: "Expert"
keyPoints:
  - Zero Trust alapelvek AI környezetben
  - Architektúra komponensek és kapcsolatok
  - Implementációs lépések és eszközök
  - Monitoring és maintenance stratégiák
tags: ["zero trust", "architektúra", "enterprise", "security design"]
author: "AI Shield Szerkesztőség"
date: "2025 Január"
---

## Zero Trust AI architektúra építése

*Zero Trust modell alkalmazása AI rendszerekben: "Never trust, always verify" megközelítés step-by-step útmutatóval.*

## Zero Trust Alapelvek AI-ban

**3 pillér:**
1. **Verify explicitly** - Minden kérés autentikációja és authorizációja
2. **Least privilege access** - Minimális szükséges jogosultság
3. **Assume breach** - Tervezz úgy, mintha már compromised lenne a rendszer

## Architektúra Komponensek

```
┌─────────────────────────────────────────────┐
│         USER / APPLICATION                  │
└──────────────┬──────────────────────────────┘
               │
         ┌─────▼─────┐
         │  Identity  │ ← Authentication (OAuth 2.0, SAML)
         │  Provider  │
         └─────┬──────┘
               │
         ┌─────▼──────┐
         │  API       │ ← Rate Limiting, Request Validation
         │  Gateway   │
         └─────┬──────┘
               │
    ┌──────────┼───────────┐
    │          │           │
┌───▼───┐  ┌───▼───┐  ┌───▼───┐
│ LLM   │  │Policy │  │ Data  │
│Service│  │Engine │  │ Vault │
└───────┘  └───────┘  └───────┘
    │          │           │
    └──────────┼───────────┘
               │
         ┌─────▼──────┐
         │ Monitoring │ ← SIEM, Logging, Alerts
         │   & Audit  │
         └────────────┘
```

### 1. Identity Layer
- MFA kötelező minden usernek
- Service accounts external identity provider-rel (Okta, Azure AD)
- Token rotation 1 órás TTL

### 2. API Gateway
- Input/output validation
- Rate limiting per user/service
- TLS 1.3 mandatory
- Request signing (HMAC-SHA256)

### 3. Policy Engine
- Attribute-Based Access Control (ABAC)
- Real-time policy evaluation
- Explicit deny by default

### 4. Data Vault
- Encryption at rest (AES-256)
- Encryption in transit (TLS 1.3)
- Secrets rotation automated

### 5. Monitoring
- Minden API call loggolva
- Anomaly detection ML-lel
- Real-time alerting

## Implementációs Lépések

**Week 1-2: Foundation**
- [ ] Identity provider setup (Okta/Auth0)
- [ ] API Gateway deploy (Kong/AWS API Gateway)
- [ ] Certificate infrastructure (Let's Encrypt/private CA)

**Week 3-4: Security Policies**
- [ ] ABAC policy definition
- [ ] Policy engine setup (Open Policy Agent)
- [ ] Test policies dry-run

**Week 5-6: Data & Secrets**
- [ ] Vault deployment (HashiCorp Vault)
- [ ] Secret migration
- [ ] Encryption key rotation setup

**Week 7-8: Monitoring**
- [ ] SIEM integration (Splunk/ELK)
- [ ] Anomaly detection (Datadog/custom)
- [ ] Alert rules configuration

## Terraform Example

```hcl
# API Gateway with authentication
resource "aws_api_gateway_rest_api" "ai_api" {
  name        = "ai-zero-trust-api"
  description = "Zero Trust AI API"

  endpoint_configuration {
    types = ["REGIONAL"]
  }
}

resource "aws_api_gateway_authorizer" "cognito" {
  name          = "cognito-authorizer"
  rest_api_id   = aws_api_gateway_rest_api.ai_api.id
  type          = "COGNITO_USER_POOLS"
  provider_arns = [aws_cognito_user_pool.ai_users.arn]
}

# Rate limiting
resource "aws_api_gateway_usage_plan" "basic" {
  name = "basic-plan"

  throttle_settings {
    rate_limit  = 100
    burst_limit = 200
  }

  quota_settings {
    limit  = 10000
    period = "DAY"
  }
}
```

## Monitoring & Maintenance

**Daily:**
- Review security alerts
- Check failed auth attempts

**Weekly:**
- Audit logs review
- Policy effectiveness check

**Monthly:**
- Rotate secrets/keys
- Update dependencies
- Security scan

## Checklist

- [ ] MFA enabled for all users
- [ ] API Gateway authentication active
- [ ] TLS 1.3 enforced
- [ ] Secrets in Vault, not code
- [ ] Logging captures all API calls
- [ ] Anomaly detection running
- [ ] Incident response plan documented
- [ ] Disaster recovery tested

---

**Kapcsolódó:**
- Szakértői: "LLM biztonsági audit módszertan"
- Vállalati: "30 perces AI biztonsági audit"
