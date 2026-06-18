import os
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

    print("Starting AI Code Review...")
    prompt = (
        "You are an expert Java and Spring Boot code reviewer. "
        "Please review the following git diff. Point out any bugs, "
        "security issues, or deviations from best practices. "
        "Keep your review concise and constructive.\n\n"
        f"```diff\n{diff_content}\n```"
    )

    # API Key is read from GEMINI_API_KEY env var automatically by LocalAgentConfig
    try:
        async with Agent(LocalAgentConfig()) as agent:
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
