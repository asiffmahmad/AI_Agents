import os

PROMPT_FILES = [
    # Foundation
    "project-context.md",
    "project-discovery-and-requirements-analysis.md",
    "project-glossary-and-domain-terminology.md",
    "project-risk-analysis.md",
    "minimum-viable-product-definition.md",
    # Product Documentation
    "create-product-requirements-document.md",
    "update-product-requirements-document.md",
    "create-business-requirements-document.md",
    "update-business-requirements-document.md",
    "create-feature-requirements-document.md",
    "update-feature-requirements-document.md",
    "create-user-stories-document.md",
    "update-user-stories-document.md",
    "create-acceptance-criteria-document.md",
    "update-acceptance-criteria-document.md",
    # User Experience Documentation
    "create-application-user-flow-document.md",
    "update-application-user-flow-document.md",
    "create-user-journey-document.md",
    "update-user-journey-document.md",
    "create-screen-navigation-document.md",
    "update-screen-navigation-document.md",
    "create-wireframe-description-document.md",
    "update-wireframe-description-document.md",
    # Technical Documentation
    "create-technical-requirements-document.md",
    "update-technical-requirements-document.md",
    "create-system-architecture-document.md",
    "update-system-architecture-document.md",
    "create-software-design-document.md",
    "update-software-design-document.md",
    "create-application-programming-interface-specification.md",
    "update-application-programming-interface-specification.md",
    "create-database-design-document.md",
    "update-database-design-document.md",
    "create-authentication-and-authorization-design-document.md",
    "update-authentication-and-authorization-design-document.md",
    "create-security-design-document.md",
    "update-security-design-document.md",
    "create-deployment-architecture-document.md",
    "update-deployment-architecture-document.md",
    # Planning
    "create-feature-implementation-plan.md",
    "update-feature-implementation-plan.md",
    "generate-development-tasks.md",
    "generate-development-subtasks.md",
    "generate-sprint-plan.md",
    "generate-release-plan.md",
    # Quality Assurance
    "create-testing-strategy-document.md",
    "update-testing-strategy-document.md",
    "generate-test-cases.md",
    "generate-end-to-end-test-scenarios.md",
    # Review Agents
    "review-source-code-quality.md",
    "review-system-architecture.md",
    "review-security-vulnerabilities.md",
    "review-performance-and-scalability.md",
    "review-project-documentation.md",
    "review-release-readiness.md",
    # Decision Tracking
    "create-architecture-decision-record.md",
    "update-architecture-decision-record.md",
    "create-technical-debt-register.md",
    "update-technical-debt-register.md",
    # Release Management
    "generate-change-log.md",
    "generate-release-notes.md",
    "create-production-deployment-checklist.md",
    "create-post-release-validation-checklist.md",
    # Auditing
    "audit-project-health.md",
    "audit-documentation-completeness.md",
    "audit-security-compliance.md",
    "audit-technical-debt.md"
]

AI_OPERATING_RULES = """
# AI Agent Operating Rules
1. Think before generating output.
2. Identify missing information.
3. Ask clarifying questions when necessary.
4. Preserve existing project knowledge.
5. Avoid making undocumented assumptions.
6. Reference related documents.
7. Maintain consistency across all project artifacts.
8. Produce professional markdown documentation.
"""

UPDATE_RULES = """
# Documentation Update Rules
* Preserve existing information
* Never overwrite decisions without justification
* Track modifications
* Record assumptions
* Record unresolved questions
* Highlight missing information
* Maintain document consistency
"""

def generate_file_content(filename):
    title = filename.replace('.md', '').replace('-', ' ').title()
    
    # Defaults
    purpose = f"To instruct an AI agent to perform the {title.lower()} task."
    when_to_use = f"Invoke this prompt when the project requires a new or updated {title}."
    required_inputs = "- `project-context.md`\n- Current project state or user request"
    optional_inputs = "- Related domain documentation\n- Previous iteration of the document"
    expected_output = f"A complete and professionally formatted markdown file containing the {title}."
    quality_checklist = "- [ ] Follows all AI Operating Rules\n- [ ] Output is valid markdown\n- [ ] Maintains project consistency"
    
    prompt_specific_reqs = ""
    
    if "product-requirements-document" in filename:
        prompt_specific_reqs = """
Your output MUST include the following sections:
* Executive Summary
* Product Vision
* Business Goals
* Problem Statement
* Target Audience
* User Personas
* User Needs
* Success Metrics
* Functional Requirements
* Non Functional Requirements
* User Stories
* Acceptance Criteria
* Assumptions
* Constraints
* Risks
* Dependencies
* Out Of Scope
* Release Scope
* Future Roadmap
"""
    elif "technical-requirements-document" in filename:
        prompt_specific_reqs = """
Your output MUST include the following sections:
* Technical Overview
* Technology Stack
* Frontend Architecture
* Backend Architecture
* Database Architecture
* Infrastructure Design
* Security Requirements
* Authentication Design
* Authorization Design
* Logging Strategy
* Monitoring Strategy
* Scalability Strategy
* Performance Requirements
* Availability Requirements
* Reliability Requirements
* Integration Requirements
* Deployment Strategy
* Disaster Recovery Strategy
* Technical Risks
* Tradeoffs
"""
    elif "application-user-flow" in filename:
        prompt_specific_reqs = """
Your output MUST include the following sections:
* User Journey Map
* Application Navigation Structure
* Screen Hierarchy
* Authentication Flow
* Registration Flow
* Onboarding Flow
* Core Feature Flows
* CRUD Flows
* Error Flows
* Permission Based Flows
* Notification Flows
* Payment Flows
* Administrative Flows
* Edge Cases
* Alternative Paths

You must generate:
1. Textual flow diagrams
2. Mermaid flowcharts
3. Navigation maps
4. User journey descriptions
"""
    elif "architecture-decision-record" in filename:
        prompt_specific_reqs = """
Your output MUST include the following sections:
* Decision Title
* Status
* Context
* Problem Statement
* Alternatives Considered
* Decision
* Justification
* Consequences
* Risks
* Future Revisions
"""
    elif filename == "review-source-code-quality.md":
        prompt_specific_reqs = """
You must analyze the code for:
* Functional Bugs
* Logic Errors
* Security Vulnerabilities
* Authentication Issues
* Authorization Issues
* Performance Problems
* Scalability Problems
* Code Smells
* Maintainability Issues
* Test Coverage Gaps
* Documentation Gaps
* Dependency Risks

Every finding must include:
* Severity
* Explanation
* Evidence
* Recommended Fix
* Example Solution
"""
    elif filename == "project-context.md":
        purpose = "Master context file that every AI agent must read before executing any task."
        prompt_specific_reqs = """
You must maintain the following project knowledge in this document:
* Product Vision
* Business Objectives
* User Personas
* User Flows
* Technology Stack
* Architecture Decisions
* Coding Standards
* Security Standards
* Documentation Standards
* Deployment Standards
* Project Constraints
* Known Risks
"""

    if "update" in filename:
        prompt_specific_reqs += f"\n{UPDATE_RULES}"
        
    full_prompt = f"""You are an autonomous AI Agent operating in a software project repository.
You are acting as a Principal Software Architect, Product Manager, and Technical Writer.

Your task is to: {title}

{AI_OPERATING_RULES}

### Requirements
{prompt_specific_reqs if prompt_specific_reqs else "Ensure the document is highly detailed, professional, and accurate to the project context."}
"""

    content = f"""# {title} Prompt

## File Name
`{filename}`

## Purpose
{purpose}

## When To Use
{when_to_use}

## Required Inputs
{required_inputs}

## Optional Inputs
{optional_inputs}

## Expected Output
{expected_output}

## Quality Checklist
{quality_checklist}

## Complete Prompt Content

```markdown
{full_prompt.strip()}
```
"""
    return content

def main():
    out_dir = "prompts"
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
        
    for fname in PROMPT_FILES:
        filepath = os.path.join(out_dir, fname)
        with open(filepath, "w") as f:
            f.write(generate_file_content(fname))
    
    print(f"Successfully generated {len(PROMPT_FILES)} prompt files in '{out_dir}/'")

if __name__ == "__main__":
    main()
