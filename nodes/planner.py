import json
from langchain_community.chat_models import ChatOllama

from agent.state import AgentState
from config.settings import settings


llm = ChatOllama(
    model=settings.PLANNER_MODEL,
    base_url=settings.OLLAMA_BASE_URL,
    temperature=0
)


def planner_node(state: AgentState) -> AgentState:

    print("\n--- PLANNER STARTED ---")

    user_request = state.get_context("user_request")

    PLANNER_PROMPT = f"""

        You are an elite Principal Software Architect and System Designer.

        You design MINIMAL, EFFICIENT, PRODUCTION-READY software architectures.


        ========================
        USER REQUEST
        ========================

        {user_request}


        ========================
        YOUR OBJECTIVE
        ========================

        Design the BEST POSSIBLE project structure.

        The project MUST be:

        • logically correct
        • minimal
        • complete
        • runnable
        • production-quality



        ========================
        ARCHITECTURE PROCESS
        ========================

        You MUST internally decide:


        STEP 1 — Identify Project Category

        Choose ONE:

        • Static Website
        • Portfolio Website
        • Web Application
        • Full Stack Application
        • REST API
        • Automation Script
        • CLI Tool
        • AI Application
        • Dashboard
        • Data Tool
        • Library
        • Other


        STEP 2 — Choose Optimal Tech Stack

        CRITICAL:

        Choose stack based on:

        • simplicity
        • performance
        • modern standards
        • minimal dependencies
        • user intent


        AVOID OVER-ENGINEERING


        Examples:

        Portfolio → HTML, CSS, JS

        API → FastAPI

        AI → Python

        Dashboard → Streamlit

        Fullstack → React + FastAPI


        DO NOT choose heavy frameworks unless REQUIRED



        STEP 3 — Design File Structure

        CRITICAL RULES:

        Include ONLY necessary files.

        DO NOT include:

        • node_modules
        • build files
        • lock files
        • cache files
        • compiled files
        • hidden system files


        File structure MUST:

        • follow real-world standards
        • be clean
        • be minimal
        • be runnable



        STEP 4 — Project Naming

        Use PascalCase.

        Short.

        Professional.



        ========================
        QUALITY RULES
        ========================

        The plan MUST be:

        • realistic
        • production-ready
        • minimal
        • complete


        NO USELESS FILES

        NO FAKE FILES

        NO RANDOM FILES



        ========================
        OUTPUT FORMAT
        ========================

        Return ONLY valid JSON.

        NO explanation.

        NO markdown.

        NO extra text.



        FORMAT:

        {{
        "project_name": "ProjectName",

        "project_type": "type",

        "tech_stack": ["tech1", "tech2"],

        "project_plan": [

        "file1",

        "file2",

        "folder/file3"

        ]
        }}

    """

    response = llm.invoke(PLANNER_PROMPT)

    content = response.content.strip()

    content = content.replace("```json", "").replace("```", "")

    try:

        result = json.loads(content)

        state.update_context("project_name", result["project_name"])

        state.update_context("project_plan", result["project_plan"])

        print("\nPlanner Result:")
        print(json.dumps(result, indent=4))

        return state

    except Exception as e:

        print("Planner Error:", str(e))

        state.update_context("error", str(e))

        return state