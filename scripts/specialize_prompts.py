import os

targets = {
    "prompts/new/create-product-requirements-document.md": """## Expected Output Structure
A complete and professionally formatted PRD containing strictly the following sections:
- Executive Summary
- Product Vision
- Problem Statement
- User Personas
- User Jobs To Be Done
- Success Metrics
- Functional Requirements
- Non Functional Requirements
- User Stories
- Acceptance Criteria
- Release Scope
- Roadmap""",

    "prompts/new/create-application-user-flow-document.md": """## Expected Output Structure
A complete and professionally formatted User Flow Document containing strictly the following sections:
- Navigation Map
- User Journey
- Authentication Flow
- Onboarding Flow
- Feature Flows
- Error Flows
- Edge Cases
- Mermaid Flowcharts
- Screen Relationships""",

    "prompts/new/create-database-design-document.md": """## Expected Output Structure
A complete and professionally formatted Database Design Document containing strictly the following sections:
- Entities
- Attributes
- Relationships
- ER Diagram
- Constraints
- Indexing Strategy
- Partitioning Strategy
- Data Retention Policy
- Backup Strategy
- Migration Strategy""",

    "prompts/new/create-security-design-document.md": """## Expected Output Structure
A complete and professionally formatted Security Design Document containing strictly the following sections:
- Threat Model
- Authentication Model
- Authorization Model
- Secrets Management
- Encryption Strategy
- OWASP Controls
- Audit Logging
- Compliance Requirements
- Security Testing Strategy""",

    "prompts/new/create-application-programming-interface-specification.md": """## Expected Output Structure
A complete and professionally formatted API Specification containing strictly the following sections:
- API Overview
- Endpoints
- Request Schema
- Response Schema
- Error Handling
- Authentication
- Rate Limiting
- Pagination
- Versioning
- OpenAPI Specification""",

    "prompts/new/create-architecture-decision-record.md": """## Expected Output Structure
A complete and professionally formatted ADR containing strictly the following sections:
- Context
- Problem
- Options Considered
- Decision
- Consequences
- Risks
- Tradeoffs
- Review Date"""
}

def specialize():
    for filepath, specific_structure in targets.items():
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            if "## Expected Output Structure" in content and "## Validation Rules" in content:
                before = content.split("## Expected Output Structure")[0]
                after = content.split("## Validation Rules")[1]
                
                new_content = before + specific_structure + "\n\n## Validation Rules" + after
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"✅ Specialized: {filepath}")
            else:
                print(f"⚠️ Could not find injection points in {filepath}")
        else:
            print(f"❌ File not found: {filepath}")

if __name__ == "__main__":
    specialize()
