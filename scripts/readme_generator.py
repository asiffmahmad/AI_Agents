import os
import sys
import glob
import asyncio
from google.antigravity import Agent, LocalAgentConfig

def read_file(filepath):
    try:
        # Added utf-8 encoding per AI review recommendation
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"Error reading {filepath}: {e}"

async def main():
    print("Reading project files to build context...")
    
    base_dir = "java-crud-app"
    
    # Replaced hardcoded paths with glob patterns per AI review recommendation
    files_to_read = []
    files_to_read.extend(glob.glob(os.path.join(base_dir, "pom.xml")))
    files_to_read.extend(glob.glob(os.path.join(base_dir, "**/*.properties"), recursive=True))
    files_to_read.extend(glob.glob(os.path.join(base_dir, "**/*.java"), recursive=True))
    
    if not files_to_read:
        print(f"Warning: No source files found in {base_dir}. The README might lack detail.", file=sys.stderr)
        
    context = ""
    for file in files_to_read:
        content = read_file(file)
        context += f"\n\n--- File: {file} ---\n```\n{content}\n```"

    prompt = (
        "You are an expert technical writer and developer advocate. "
        "I have a simple Spring Boot Java CRUD application. "
        "Please generate a comprehensive, professional README.md file for this project. "
        "Include sections for: Project Title, Description, Tech Stack, Features, "
        "API Endpoints (with HTTP methods and paths based on the controller), and How to Run Locally. "
        "Do not include any chat formatting around your response, just output the raw markdown text for the README.md file.\n\n"
        "Here is the project code context:\n"
        f"{context}"
    )

    print("Generating README.md using Google Antigravity Agent...")
    try:
        # The API key is automatically picked up from the GEMINI_API_KEY environment variable.
        async with Agent(LocalAgentConfig()) as agent:
            response = await agent.chat(prompt)
            readme_content = await response.text()
            
            # Improved robustness of markdown fence stripping per AI review recommendation
            readme_content = readme_content.strip()
            if readme_content.startswith("```markdown"):
                readme_content = readme_content[11:]
            elif readme_content.startswith("```"):
                readme_content = readme_content[3:]
                
            readme_content = readme_content.strip()
            if readme_content.endswith("```"):
                readme_content = readme_content[:-3]
                
            readme_content = readme_content.strip()

            # Added utf-8 encoding per AI review recommendation
            with open("README.md", "w", encoding='utf-8') as f:
                f.write(readme_content)
                
            print("\nSuccessfully generated and saved to README.md!")
    except Exception as e:
        print(f"Failed to generate README: {e}")

if __name__ == "__main__":
    asyncio.run(main())
