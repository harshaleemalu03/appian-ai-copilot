# app.py
import json

# Sample input cases (can be replaced with real JSON input)
sample_cases = [
    {
        "case_id": "CASE_10245",
        "case_type": "Flood Insurance",
        "location": "Florida",
        "claim_amount": 75000,
        "property_type": "Residential",
        "incident_date": "2024-08-12",
        "priority": "High"
    },
    {
        "case_id": "CASE_10246",
        "case_type": "Flood Insurance",
        "location": "California",
        "claim_amount": 40000,
        "property_type": "Commercial",
        "incident_date": "2024-07-05",
        "priority": "Medium"
    },
    {
        "case_id": "CASE_10247",
        "case_type": "Fire Insurance",
        "location": "Texas",
        "claim_amount": 120000,
        "property_type": "Residential",
        "incident_date": "2024-06-20",
        "priority": "High"
    }
]

# Simulated policy database (like a vector knowledge base)
policy_db = [
    {
        "type": "Flood Insurance",
        "location": "Florida",
        "section": "4.2",
        "summary": "On-site inspection is mandatory for high-value flood claims.",
        "page": 18
    },
    {
        "type": "Flood Insurance",
        "location": "California",
        "section": "3.1",
        "summary": "Inspection optional for claims below $50,000.",
        "page": 12
    },
    {
        "type": "Fire Insurance",
        "location": "Texas",
        "section": "5.3",
        "summary": "Immediate verification required for all high-value fire claims.",
        "page": 22
    }
]

def fetch_relevant_policy(context):
    """
    Simulate semantic vector search:
    - Match case type first
    - Then match location if possible
    - Otherwise fallback to type match
    """
    matches = [p for p in policy_db if p["type"] == context["case_type"]]
    if not matches:
        return None
    # Try to match location
    loc_match = next((p for p in matches if p["location"] == context["location"]), None)
    if loc_match:
        return loc_match
    # Fallback: first match by type
    return matches[0]

def main():
    for context in sample_cases:
        policy = fetch_relevant_policy(context)
        if policy:
            output = {
                "case_id": context["case_id"],
                "recommended_action": policy["summary"],
                "source_document": f"{policy['type']} Policy 2024",
                "section": policy["section"],
                "page": policy["page"]
            }
            print("\n=== AI Compliance Assistant ===")
            print(json.dumps(output, indent=4))
        else:
            print(f"\nNo policy found for case {context['case_id']}")

if __name__ == "__main__":
    main()
