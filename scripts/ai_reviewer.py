import os
import re
import sys
import subprocess
import asyncio
from google.antigravity import Agent, LocalAgentConfig

async def main():
    print("Extracting git diff for the most recent commit...")
    # Using HEAD~1 to get the changes made in the latest commit
    result = subprocess.run(['git', 'diff', 'HEAD~1', 'HEAD'], capture_output=True, text=True)
    if result.returncode != 0:
        print("Error getting git diff:")
        print(result.stderr)
        return

    diff_content = result.stdout
    if not diff_content.strip():
        print("No changes found in the last commit. Skipping AI review.")
        return

    # Extract changed files to determine necessary skills
    changed_files = re.findall(r'^diff --git a/(.*?) b/', diff_content, re.MULTILINE)
    
    needed_skills = set()
    for file in changed_files:
        if file.endswith('.java'):
            needed_skills.add('java-reviewer')
        elif file.endswith(('.ts', '.html')) and 'angular' in diff_content.lower():
            needed_skills.add('angular-reviewer')
        elif file.endswith(('.jsx', '.tsx', '.js', '.ts')):
            needed_skills.add('react-reviewer')
        elif file.endswith('.sql'):
            needed_skills.add('sql-reviewer')

    # Default to java if nothing matched but we want a review (fallback)
    if not needed_skills:
        needed_skills.add('java-reviewer')

    print(f"Detected file changes requiring the following skills: {', '.join(needed_skills)}")
    print("Starting AI Code Review...")
    
    skills_instruction = " and ".join([f"`{skill}`" for skill in needed_skills])

    prompt = (
        f"Please act as the {skills_instruction} and review the following git diff.\n"
        "Apply the strict rules defined in your assigned skill documents.\n\n"
        f"```diff\n{diff_content}\n```"
    )

    # Load the agent skills from the local 'skills' directory
    config = LocalAgentConfig(skills_paths=["skills"])
    try:
        async with Agent(config) as agent:
            response = await agent.chat(prompt)
            review = await response.text()
            
            print("\n" + "="*50)
            print("🤖 AI CODE REVIEW REPORT")
            print("="*50)
            print(review)
            print("="*50)
    except Exception as e:
        print(f"Failed to run AI review: {e}")
        # We don't want to fail the whole CI pipeline if the AI review fails
        # so we just print the error and exit gracefully.

if __name__ == "__main__":
    asyncio.run(main())
