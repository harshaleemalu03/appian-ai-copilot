# app.py

def get_case_context():
    return {
        "case_type": "Flood Insurance",
        "location": "Florida",
        "claim_amount": 75000
    }

def fetch_relevant_policy(context):
    if context["case_type"] == "Flood Insurance" and context["location"] == "Florida":
        return {
            "policy": "Florida Flood Insurance Policy 2024",
            "section": "Section 4.2",
            "summary": "On-site inspection is mandatory for high-value flood claims.",
            "source": "Page 18"
        }

def main():
    context = get_case_context()
    policy = fetch_relevant_policy(context)

    print("=== AI Compliance Assistant ===")
    print(f"Case Type: {context['case_type']}")
    print(f"Recommended Action: {policy['summary']}")
    print(f"Source: {policy['policy']} - {policy['section']}")

if __name__ == "__main__":
    main()
