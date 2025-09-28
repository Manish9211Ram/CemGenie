# CemGenie

**CemGenie — Generative AI platform for autonomous cement-plant optimization**

A prototype web app and design that integrates energy, quality, and sustainability insights for cement operations. The project includes a Streamlit prototype (`app.py`) and a project deck describing architecture, features and business case.

---

## Table of contents
- [Project summary](#project-summary)  
- [Features](#features)  
- [Quick demo / expected behavior](#quick-demo--expected-behavior)  
- [Files in this repo](#files-in-this-repo)  
- [How to run (local)](#how-to-run-local)  
- [Model details](#model-details)  
- [Architecture & tech stack](#architecture--tech-stack)  
- [Developer / Team](#developer--team)  
- [Contributing](#contributing)  
- [License & contact](#license--contact)

---

## Project summary
CemGenie is a Generative-AI powered prototype that aims to fuse data across raw-material handling, grinding, clinkerization and utilities to deliver proactive recommendations for energy efficiency, product quality and sustainability improvements. The prototype demonstrates cross-process intelligence (not just siloed rules) and showcases how generative/predictive models can stabilize production and reduce energy/CO₂ impact.

---

## Features
- **Energy optimization:** monitors energy vs CO₂ and suggests actions when ratio is sub-optimal. (Prototype metric and threshold logic in `app.py`).  
- **Quality prediction:** predicts Pass/Fail of cement batches using a saved model (app tries to load `quality_model.pkl` and falls back to a demo rule if model unavailable).  
- **Sustainability insights:** kiln & cooling efficiency metrics and automated warnings for high-energy scenarios and poor cooling.  
- **High-level platform components (from deck):** AI agents, Firebase dashboards, Vertex AI + Gemini for model training/deployment, IoT / PLCs ingestion, BigQuery / Pub/Sub streaming.  

---

## Quick demo / expected behavior
(Behavior documented from `app.py`)

- **Energy → CO₂ metric**: `energy_co2_ratio = energy_kwh / co2_tonnes`. If the ratio is `> 300` the app marks operation as efficient; otherwise it warns and suggests blend or kiln adjustments.  

- **Quality prediction demo rule (fallback)**: If `CaO > 50` **and** `Silica > 15` → **PASS**; else **FAIL**. When a real `quality_model.pkl` is present, the model is used instead.  

- **Sustainability checks**:
  - Temp-residence interaction = `kiln_temp * residence_time` → high values trigger energy-usage warning.
  - Cooling efficiency ratio = `clinker_temp / cooling_time` → high values trigger warnings about cracking risk.  

---

## Files in this repo
- `app.py` — Streamlit prototype web app (main demo UI & logic).  
- `CemGenie.pptx` — project slides: team, problem statement, architecture, features, cost comparison, tech stack and opportunity.  
- `quality_model.pkl` — (referenced by `app.py`) trained model file expected by the prototype (place in repo root to enable model-based predictions). See `app.py` for loading logic.  

---

## How to run (local)
1. Create a Python virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # macOS / Linux
   venv\Scripts\activate      # Windows
   ```

2. Install required packages:
   ```bash
   pip install streamlit pandas numpy joblib
   ```

3. Place the trained model `quality_model.pkl` in the same folder as `app.py` if you want real model predictions. If missing, the app uses the demo rule. (See `app.py` handling).  

4. Run the app:
   ```bash
   streamlit run app.py
   ```

5. Open the browser URL shown by Streamlit (typically `http://localhost:8501`).

---

## Model details
- `app.py` attempts to `joblib.load("quality_model.pkl")`. If loading fails, the app falls back to a deterministic demo rule (`CaO > 50` and `Silica > 15` → PASS). To enable ML predictions, provide a scikit-learn-compatible classifier saved via `joblib.dump`.  

**Suggested model training checklist**
- Input features expected by the app: `chemical_cao_pct`, `silica_pct`, `alumina_pct`. Build a classifier that accepts a single-row DataFrame with these columns.  
- Export model using `joblib.dump(model, "quality_model.pkl")`.

---

## Architecture & tech stack
The project deck highlights a cloud-native architecture that can include:
- **Generative AI**: Gemini models (for agent behavior / recommendations).  
- **Vertex AI**: model training & deployment.  
- **Streaming & storage**: Cloud Pub/Sub, BigQuery (telemetry and feature store).  
- **Dashboards & agents**: Firebase dashboards, Agent Builder for operator interactions.  
- **Edge / OT**: IoT sensors / PLCs for plant telemetry ingestion.  

---

## Repo structure (suggested)
```
CemGenie/
├─ app.py
├─ quality_model.pkl        # optional: put trained joblib model here
├─ requirements.txt         # create with `pip freeze > requirements.txt`
├─ data/                    # example datasets for training/analysis
├─ docs/
│  └─ CemGenie.pptx         # slide deck (prototype description)
└─ README.md
```

---

## Contribution
Contributions & ideas welcome. Typical contribution steps:
1. Fork the repo
2. Create a feature branch: `git checkout -b feat/your-feature`
3. Implement & test
4. Submit a pull request with clear description and screenshots (if UI chang
