import asyncio
import os
import sys
from dotenv import load_dotenv

load_dotenv()

from browser_use import Agent
from browser_use.llm import ChatGoogle


async def main():
    # Ensure API key is available
    if not os.getenv("GOOGLE_API_KEY"):
        print("Error: GOOGLE_API_KEY not found in environment variables.")
        sys.exit(1)

    # Instantiate the Google Gemini model
    llm = ChatGoogle(model="gemini-2.5-flash")

    task = "Search Google for 'what is browser automation' and tell me the top 3 results"
    agent = Agent(task=task, llm=llm)

    try:
        history = await agent.run()
        print("\n=== Agent Output ===")
        print(history)

        # Save detailed history to history.txt
        with open("history.txt", "w", encoding="utf-8") as f:
            f.write("## Agent History\n\n")
            f.write(f"Visited URLs: {history.urls()}\n\n")
            f.write(f"Screenshots: {history.screenshot_paths()}\n\n")
            f.write(f"Actions: {history.action_names()}\n\n")
            f.write(f"Extracted Content: {history.extracted_content()}\n\n")
            f.write(f"Errors: {history.errors()}\n\n")
            f.write(f"Model Actions: {history.model_actions()}\n\n")
            f.write(f"Model Outputs: {history.model_outputs()}\n\n")
            f.write(f"Final Result: {history.final_result()}\n\n")
            f.write(f"Is Done: {history.is_done()}\n")
            f.write(f"Successful: {history.is_successful()}\n")
            f.write(f"Errors Present: {history.has_errors()}\n")
            f.write(f"Steps Taken: {history.number_of_steps()}\n")
            f.write(f"Duration (s): {history.total_duration_seconds()}\n")

        print("✅ Full history saved to history.txt")

    except Exception as e:
        print(f"Agent failed: {e}")


if __name__ == "__main__":
    asyncio.run(main())
