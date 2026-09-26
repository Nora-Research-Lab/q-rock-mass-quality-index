![NORA logo](https://i.ibb.co/0VJCC9Gf/IMG-20260114-WA0008.jpg)
 
# Q-Rock Mass Quality Index
 
*For geological engineers and tunnel designers: enter six rock mass parameters (RQD, joint set number, joint roughness, joint alteration, water conditions, and stress reduction) to instantly compute Barton's Q-value and get rock mass class with support recommendations.*
 
[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
 

## Overview
 
**Industry:** Geological Engineering
 
This tool implements the Q-system (Barton et al., 1974) for rock mass classification in tunneling and excavation engineering.

Inputs (all numerical, with dropdowns for categorical choices where applicable):
- RQD (Rock Quality Designation, %): numeric slider 0–100.
- Jn (Joint Set Number): dropdown with values 0.5 (massive), 1 (one set), 2 (two sets), 3 (three sets), 4 (four or more), 5 (crushed rock).
- Jr (Joint Roughness Number): dropdown with values 4 (discontinuous joints), 3 (rough/irregular), 2.5 (smooth undulating), 2 (filled/healed), 1.5 (rough planar), 1 (smooth planar), 0.5 (slickensided).
- Ja (Joint Alteration Number): dropdown with values 0.75 (tightly healed, hard), 1 (unweathered, surface staining only), 2 (slightly altered), 4 (moderately altered), 6 (highly altered), 8 (soft clay coatings), 10 (swelling clay).
- Jw (Joint Water Reduction Factor): dropdown with values 1 (dry), 0.66 (damp), 0.5 (wet), 0.33 (water inflow), 0.2 (high inflow).
- SRF (Stress Reduction Factor): dropdown with values 0.5 (low stress near surface), 1 (medium stress), 2 (high stress), 4 (very high stress), 8 (extremely high stress).

Calculation:
Q = (RQD / Jn) * (Jr / Ja) * (Jw / SRF)

Classification table (Barton):
- 0.001–0.01: Exceptionally poor
- 0.01–0.1: Extremely poor
- 0.1–1: Very poor
- 1–4: Poor
- 4–10: Fair
- 10–40: Good
- 40–100: Very good
- 100–1000: Extremely good
- >1000: Exceptionally good

Output:
- Numeric Q-value displayed prominently.
- Rock mass class (text).
- A simple horizontal color bar showing the Q range with a marker at the computed value.
- In a separate section, a support recommendation table (simplified from Barton): for the given Q and tunnel span (user provides tunnel span in meters as a numeric input), recommend support type: None / Spot bolting / Systematic bolting / Shotcrete and bolting / Steel sets and shotcrete. Recommendation logic based on common Q-support correlation lookup (e.g., for Q<0.01 and small span: steel sets; for Q>100: none).

UI layout: top section with input sliders/dropdowns; a 'Calculate' button; then outputs: Q-value, class, color bar, support recommendation.

No AI component; pure deterministic calculation and lookup.
 
## Run it
 
```bash
docker build -t q-rock-mass-quality-index .
docker run -p 7860:7860 q-rock-mass-quality-index
```
 
Then open http://localhost:7860 in your browser.
 
## About
 
This tool was generated and published automatically by the **NORA Earth Intelligence**
tool factory, an autonomous pipeline maintained by **NORA Research Lab** that turns
one idea per run into a small, working geoscience tool — end to end, with an
LLM writing and Docker-testing the code, and another model generating the
banner above.
 
- Platform: [https://noraearth.xyz](https://noraearth.xyz)
- Parent lab: [https://noraresearchlab.site](https://noraresearchlab.site)
 
Built 2026-09-26.
 
---
 
### Maintainer
 
**NORA Research Lab**
[![GitHub](https://img.shields.io/badge/GitHub-Nora--Research--Lab-181717?logo=github)](https://github.com/Nora-Research-Lab) [![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-NoraResearchLab-yellow)](https://huggingface.co/NoraResearchLab) [![LinkedIn](https://img.shields.io/badge/LinkedIn-NORA%20Research%20Lab-0A66C2?logo=linkedin)](https://www.linkedin.com/company/nora-research-lab) [![X](https://img.shields.io/badge/X-@noraresearchlab-000000?logo=x)](https://x.com/noraresearchlab) [![NORA Research Lab](https://img.shields.io/badge/Website-noraresearchlab.site-2ea44f)](https://noraresearchlab.site) [![NORA Earth Intelligence](https://img.shields.io/badge/Platform-noraearth.xyz-2ea44f)](https://noraearth.xyz)
