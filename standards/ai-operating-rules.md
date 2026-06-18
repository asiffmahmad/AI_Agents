# Core AI Operating Rules

Every AI agent executing a prompt within this repository MUST adhere to these global standards:

1. **No Hallucination:** Never silently assume undocumented constraints or missing data.
2. **Missing Information Handling:** If required inputs are missing, the agent MUST:
   - Identify gaps.
   - List missing inputs.
   - Ask clarifying questions.
   - Explain the impact of the missing data.
   - Halt execution.
3. **Strict Routing:** Output documents MUST be saved exactly to the defined `Output Location` within the `/docs` or `/src` directories.
4. **Preserve Knowledge:** Never overwrite existing architecture, decisions, or constraints without explicit justification documented in a Change Summary.
