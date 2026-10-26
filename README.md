# Rwanda Demographic and Health Survey (2025 RDHS) — Static & Dynamic Infographics

**Author & Project Owner:** Methode Duhujubumwe & Keira Mutoni  
**GitHub:** [@dumethode](https://github.com/dumethode) [@keira9](https://github.com/keira9) 
**Competition:** 2026 NISR Infographic Competition (National Institute of Statistics of Rwanda)  
**Module:** Mathematics for Machine Learning  

---

## 1. Executive Summary

This project transforms the official findings of the **2025 Rwanda Demographic and Health Survey (RDHS 2025)** into a paired **Static Infographic** (Figma / SVG) and **Dynamic Interactive Dashboard** (HTML5 / CSS3 / Vanilla JavaScript). It examines three decades of demographic and health transformation in Rwanda (1992–2025), connecting public health milestones with mathematical and statistical foundations including **Principal Component Analysis (PCA)** for wealth index construction, **95% confidence intervals** on mortality estimators, **Gini inequality coefficients**, and **relative risk ratios ($RR$)** for high-risk fertility behaviour.

---

## 2. Official Data Provenance

All statistics are sourced directly from the **National Institute of Statistics of Rwanda (NISR)** and the **Ministry of Health (MoH)**:

* **Primary Source:** National Institute of Statistics of Rwanda (NISR), Ministry of Health, and ICF. 2026. *Rwanda Demographic and Health Survey 2025 Final Report*. Kigali, Rwanda, and Maryland, USA: NISR and ICF. ISBN: `978-99977-43-10-7`.
* **Data Collection Period:** 5 June 2025 – 25 October 2025 across 560 enumeration area clusters (198 urban, 362 rural) in all 30 districts.
* **Sample Size:** 14,560 selected households (14,427 interviewed; 100.0% response rate of occupied households), 14,283 women aged 15–49 (99.2% response rate), and 6,548 men aged 15–59 (98.2% response rate).

---

## 3. Core Statistical Findings Visualized

| Indicator | 1992 / 2000 Baseline | 2019–20 RDHS | 2025 RDHS | Reference in 2025 RDHS Report |
| :--- | :--- | :--- | :--- | :--- |
| **Maternal Mortality Ratio (per 100k live births)** | 1,071 (30-yr baseline) | 203 | **149** | Foreword (p. xix), SDG Table (p. xxxiii) |
| **Under-5 Mortality Rate (per 1,000 live births)** | 196 (2000 RDHS) | 45 | **36** (CI: 31–41) | Figure 8.1 (p. 138), Table 8.1 (p. 141) |
| **Infant Mortality Rate (per 1,000 live births)** | 107 (2000 RDHS) | 33 | **27** (CI: 23–32) | Figure 8.1 (p. 138), Table 8.1 (p. 141) |
| **Neonatal Mortality Rate (per 1,000 live births)** | 44 (2000 RDHS) | 19 | **17** (CI: 13–20) | Figure 8.1 (p. 138), Table 8.1 (p. 141) |
| **Skilled Birth Attendance (%)** | — | >90% | **98.1%** | Foreword (p. xix), SDG 3.1.2 (p. xxxiii) |
| **Child Stunting Prevalence (Under 5, %)** | — | 33.0% | **26.8%** | Foreword (p. xix), SDG 2.2.1 (p. xxxiii) |
| **Total Fertility Rate (Children per Woman)** | 6.2 (1992 RDHS) | 4.1 | **3.7** (Wanted: 2.8) | Figure 5.1 (p. 80), Table 6.6 (p. 107) |
| **Median Birth Interval (Months)** | 32.7 (2010 RDHS) | 40.8 | **48.8** | Chapter 5 Key Findings (p. 79), Table 5.5 |
| **Married Contraceptive Prevalence (Any / Modern)** | 21.2% / 12.9% (1992) | 64.1% / 58.4% | **69.3% / 64.2%** | Table 7.4.1 (p. 121), Figure 7.1 (p. 110) |
| **Unmet Need for Family Planning (Married, %)** | 38.0% (1992 RDHS) | — | **8.9%** | Figure 7.6 (p. 115), Table 7.15.1 (p. 129) |
| **Household Electricity Access (%)** | — | — | **74.1%** | Table 2.1 (p. 17) |
| **Clean Cooking Fuel Reliance (HHs / Population)** | — | — | **6.5% / 4.7%** | Table 2.2 (p. 18), Table 2.4 (p. 19) |
| **Birth Registration (Children Under 5, %)** | — | 86.0% | **95.1%** | Map 2.1 (p. 13), Table 2.10 (p. 24) |
| **Health Insurance Coverage (De Jure Pop., %)** | — | 83.0% | **86.0%** | Table 2.14 (p. 28) |

---

## 4. Repository Structure & Execution

1. **Static Infographic (`assets/rdhs_2025_static_infographic.svg`)**: Vector graphic designed in Figma following NISR brand guidelines (`#0072BC`, `#00A8E8`, `#2E7D32`, `#0A2540`) and Imigongo cultural motifs.
2. **Dynamic Infographic (`index.html`)**: Interactive single-page statistical explorer featuring provincial filtering, urban-rural stratification, PCA wealth quintile comparisons, and historical trend toggles (1992–2025). Open `index.html` in any browser or deploy directly via GitHub Pages / Vercel.
3. **Mathematical Verification (`scripts/verify_rdhs_metrics.py`)**: Python verification suite computing rate-of-change metrics, weighted provincial proportions, and family planning demand satisfaction ratios.