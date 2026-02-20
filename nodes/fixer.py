import os

from langchain_ollama import ChatOllama

from agent.state import AgentState
from config.settings import settings


llm = ChatOllama(

    model=settings.FIXER_MODEL,

    base_url=settings.OLLAMA_BASE_URL,

    temperature=0

)


def fixer_node(state: AgentState) -> AgentState:

    print("\n==================================================")
    print("FIXER STARTED")
    print("==================================================")

    error = state.get_context("execution_output")

    project_name = state.get_context("project_name")

    project_path = os.path.join(

        settings.PROJECT_ROOT,

        project_name

    )


    print("\nError Found:")
    print(error)


    if not error:

        print("\nNo error found. Skipping fixer.")

        state.update_context("fix_applied", False)

        return state


    prompt = f"""
You are an expert software engineer.

Fix the project based on the error.

Project path:
{project_path}

Error:
{error}

Instructions:

Fix the files.

Return ONLY fixed code.

Do not explain anything.
"""


    response = llm.invoke(prompt)


    fixed_code = response.content


    # overwrite main.py as simple fallback

    main_file = os.path.join(

        project_path,

        "main.py"

    )


    with open(main_file, "w", encoding="utf-8") as f:

        f.write(fixed_code)


    print("\nFiles fixed:", main_file)


    state.update_context("fix_applied", True)


    print("\nFIXER COMPLETED")


    return state