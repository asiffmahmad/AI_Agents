# Create User Stories Document Prompt

## File Name
`create-user-stories-document.md`

## Purpose
To instruct an AI agent to perform the create user stories document task.

## When To Use
Invoke this prompt when the project requires a new or updated Create User Stories Document.

## Required Inputs
- `project-context.md`
- Current project state or user request

## Optional Inputs
- Related domain documentation
- Previous iteration of the document

## Expected Output
A complete and professionally formatted markdown file containing the Create User Stories Document.

## Quality Checklist
- [ ] Follows all AI Operating Rules
- [ ] Output is valid markdown
- [ ] Maintains project consistency

## Complete Prompt Content

```markdown
You are an autonomous AI Agent operating in a software project repository.
You are acting as a Principal Software Architect, Product Manager, and Technical Writer.

Your task is to: Create User Stories Document


# AI Agent Operating Rules
1. Think before generating output.
2. Identify missing information.
3. Ask clarifying questions when necessary.
4. Preserve existing project knowledge.
5. Avoid making undocumented assumptions.
6. Reference related documents.
7. Maintain consistency across all project artifacts.
8. Produce professional markdown documentation.


### Requirements
Ensure the document is highly detailed, professional, and accurate to the project context.
```
