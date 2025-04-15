from agents.cve_agent import analyze_cves
from agents.social_sentiment_agent import analyze_sentiment
from agents.risk_mapper import map_risks

def run_agents(show_reasoning=False, use_ollama=False):
    threats = analyze_cves() + analyze_sentiment()
    threats = map_risks(threats)

    if show_reasoning:
        for t in threats:
            print(f"[{t['Threat']}] Score: {t['Score']} | Reason: {t['Reasoning']} | Impact: {t.get('Impact')}")

    return threats
