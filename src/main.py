import argparse
from agents.portfolio_manager import run_agents

def main():
    parser = argparse.ArgumentParser(description="ShadowGrid Threat Fusion CLI")
    parser.add_argument("--show-reasoning", action="store_true", help="Display agent reasoning")
    parser.add_argument("--ollama", action="store_true", help="Use local LLMs via Ollama")
    args = parser.parse_args()

    run_agents(show_reasoning=args.show_reasoning, use_ollama=args.ollama)

if __name__ == "__main__":
    main()
