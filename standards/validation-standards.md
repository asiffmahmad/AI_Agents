# Validation & Quality Gates

Before an AI agent can consider a prompt execution "Complete," it MUST self-verify against the following quality gates:

1. **Completeness:** All required sections of the document or source code template are populated.
2. **Consistency:** No contradictions exist between the generated output and prerequisite documents (e.g., PRD, TRD, System Architecture).
3. **Dependency Validation:** Required upstream files exist and were successfully read.
4. **Assumption Review:** All implicit assumptions were explicitly documented in the Risk or Assumptions section.
