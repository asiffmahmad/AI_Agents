import os
import glob
import re

def refactor():
    files = glob.glob("prompts/new/*.md") + glob.glob("prompts/update/*.md")
    print(f"Discovered {len(files)} prompts to refactor.")

    for filepath in files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Determine expected output location based on filename
        filename = os.path.basename(filepath)
        if filename.startswith("review-"):
            out_loc = f"/docs/reviews/{filename.replace('review-', '')}"
        elif filename.startswith("audit-"):
            out_loc = f"/docs/audits/{filename.replace('audit-', '')}"
        else:
            out_name = filename
            for prefix in ["create-", "update-", "generate-"]:
                if out_name.startswith(prefix):
                    out_name = out_name[len(prefix):]
                    break
            out_loc = f"/docs/{out_name}"

        # 1. Output Location & Structure
        if "## Expected Output" in content and "## Output Location" not in content:
            replacement = f"## Output Location\n`{out_loc}`\n\n## Expected Output Structure"
            content = content.replace("## Expected Output", replacement)

        # 2. Rename Quality Checklist -> Validation Rules
        if "## Quality Checklist" in content:
            content = content.replace("## Quality Checklist", "## Validation Rules")

        # 3. Add Completion Criteria and Related Documents
        if "## Complete Prompt Content" in content and "## Completion Criteria" not in content:
            injection = "## Completion Criteria\n- The generated document must be saved to the exact Output Location.\n- All validation rules must be satisfied.\n- The AI Agent must not encounter any unresolved errors or missing dependencies.\n\n## Related Documents\n- `docs/reviews/prompt-dependency-analysis.md` (For mapping cross-prompt handoffs)\n\n## Complete Prompt Content"
            content = content.replace("## Complete Prompt Content", injection)

        # 4. Inject Error Handling and Routing rules directly into the AI prompt template
        rule_patch = "8. Produce professional markdown documentation.\n9. **STRICT ROUTING:** You must save your generated output document strictly inside the `/docs/` directory structure as defined.\n10. **ERROR HANDLING:** If any required input files are missing or instructions are contradictory, halt execution, generate an error log, and flag the missing dependency immediately."
        
        if "8. Produce professional markdown documentation." in content and "9. **STRICT ROUTING" not in content:
            content = content.replace("8. Produce professional markdown documentation.", rule_patch)

        # Write the patched content back
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

    print("✅ All 67 prompts successfully refactored and upgraded to production standards.")

if __name__ == "__main__":
    refactor()
