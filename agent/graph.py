import time

from agent.state import AgentState

from nodes.planner import planner_node
from nodes.code_generator import code_generator_node
from nodes.executor import executor_node
from nodes.fixer import fixer_node
from nodes.github_push import github_push_node


def run_agent(user_request: str, auto_push=True, ui=None):

    state = AgentState()

    state.update_context("user_request", user_request)

    start_time = time.time()

    try:

        # =====================
        # PLANNER
        # =====================

        if ui:
            ui.update_stage("Planning")
            ui.update_message("Designing architecture")
            ui.log("Planner started")

        state = planner_node(state)

        if state.get_context("error"):
            if ui:
                ui.log(state.get_context("error"))
            return state

        # =====================
        # CODE GENERATOR
        # =====================

        if ui:
            ui.update_stage("Generating Code")
            ui.update_message("Writing project files")
            ui.log("Code generation started")

        state = code_generator_node(state)

        # =====================
        # EXECUTOR
        # =====================

        if ui:
            ui.update_stage("Executing")
            ui.update_message("Running project")
            ui.log("Execution started")

        state = executor_node(state)

        # =====================
        # FIXER
        # =====================

        if not state.get_context("execution_success"):

            if ui:
                ui.update_stage("Fixing Errors")
                ui.update_message("Repairing project")
                ui.log("Fixer started")

            state = fixer_node(state)

        # =====================
        # GITHUB PUSH
        # =====================

        if auto_push:

            push = input("\nPush to GitHub? (yes/no): ")

            if push.lower() == "yes":

                if ui:
                    ui.update_stage("Uploading")
                    ui.update_message("Pushing to GitHub")
                    ui.log("Uploading started")

                state = github_push_node(state)

        # =====================
        # COMPLETE
        # =====================

        total = round(time.time() - start_time, 2)

        if ui:
            ui.complete()
            ui.log(f"Total Time: {total} sec")

        return state

    except Exception as e:

        if ui:
            ui.log(f"Crash: {str(e)}")

        state.update_context("error", str(e))

        return state