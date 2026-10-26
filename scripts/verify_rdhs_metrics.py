import json

rdhs_2025_summary = {
    "project_owner": "Methode Duhujubumwe",
    "github": "dumethode",
    "survey": "2025 Rwanda Demographic and Health Survey (RDHS 2025)",
    "sample": {
        "clusters": 560,
        "urban_clusters": 198,
        "rural_clusters": 362,
        "households_selected": 14560,
        "households_occupied": 14434,
        "households_interviewed": 14427,
        "women_interviewed_15_49": 14283,
        "men_interviewed_15_59": 6548
    },
    "mortality_trends": {
        "mmr_baseline_30yr": 1071,
        "mmr_2020": 203,
        "mmr_2025": 149,
        "u5m_2000": 196,
        "u5m_2020": 45,
        "u5m_2025": 36,
        "u5m_2025_ci": [31, 41],
        "infant_2025": 27,
        "neonatal_2025": 17
    },
    "fertility_and_fp": {
        "tfr_1992": 6.2,
        "tfr_2020": 4.1,
        "tfr_2025": 3.7,
        "wanted_tfr_2025": 2.8,
        "cpr_any_married_2025": 69.3,
        "cpr_modern_married_2025": 64.2,
        "unmet_need_married_2025": 8.9,
        "total_demand_married_2025": 78.2
    }
}


def compute_transformations(data):
    m = data["mortality_trends"]
    f = data["fertility_and_fp"]
    mmr_drop_pct = round(
        (m["mmr_baseline_30yr"] - m["mmr_2025"]) / m["mmr_baseline_30yr"] * 100, 2)
    u5m_drop_pct = round(
        (m["u5m_2000"] - m["u5m_2025"]) / m["u5m_2000"] * 100, 2)
    neonatal_share_u5 = round((m["neonatal_2025"] / m["u5m_2025"]) * 100, 2)
    tfr_gap = round(f["tfr_2025"] - f["wanted_tfr_2025"], 2)
    demand_satisfied_modern = round(
        (f["cpr_modern_married_2025"] / f["total_demand_married_2025"]) * 100, 1)

    return {
        "mmr_30yr_reduction_percent": mmr_drop_pct,
        "u5m_2000_to_2025_reduction_percent": u5m_drop_pct,
        "neonatal_share_of_u5m_percent": neonatal_share_u5,
        "actual_minus_wanted_tfr_gap": tfr_gap,
        "demand_satisfied_by_modern_methods_percent": demand_satisfied_modern
    }


if __name__ == "__main__":
    results = compute_transformations(rdhs_2025_summary)
    print(json.dumps(results, indent=2))
