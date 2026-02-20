# nodes/code_generator.py

import os

from langchain_ollama import ChatOllama

from agent.state import AgentState
from config.settings import settings
from utils.logger import info, success, error


llm = ChatOllama(
    model=settings.CODER_MODEL,
    base_url=settings.OLLAMA_BASE_URL,
    temperature=0
)


def code_generator_node(state: AgentState) -> AgentState:

    try:

        state.update_context("stage", "Generating Code")
        info("Stage: Generating Code")

        plan = state.get_context("project_plan")
        prompt = state.get_context("user_request")
        project_name = state.get_context("project_name")

        if not plan:
            raise ValueError("Plan missing")

        project_path = os.path.abspath(
            os.path.join(
                settings.GENERATED_PROJECTS_PATH,
                project_name
            )
        )

        state.update_context("project_path", project_path)

        os.makedirs(project_path, exist_ok=True)

        generated_files = []

        for filename in plan:

            info(f"Generating: {filename}")

            FILE_PROMPT = f"""
You are a senior software engineer.

USER REQUEST:
{prompt}

Generate COMPLETE code for this file:

{filename}

Rules:

Return ONLY code.

No markdown.

No backticks.

No explanation.

Only raw file content.
"""

            response = llm.invoke(FILE_PROMPT)

            code = response.content.strip()

            file_path = os.path.join(
                project_path,
                filename
            )

            os.makedirs(
                os.path.dirname(file_path),
                exist_ok=True
            )

            with open(
                file_path,
                "w",
                encoding="utf-8"
            ) as f:

                f.write(code)

            generated_files.append(file_path)

            success(f"Created: {file_path}")

        state.update_context(
            "generated_files",
            generated_files
        )

        success("All files generated successfully")

        return state


    except Exception as e:

        state.update_context("stage", "Error")

        error(str(e))

        raise e