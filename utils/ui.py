from rich.console import Console
from rich.panel import Panel
from rich.live import Live
from rich.spinner import Spinner
from rich.layout import Layout
import time


console = Console()


class AgentUI:

    def __init__(self):

        self.live = None

        self.current_stage = None

        self.current_message = ""

        self.completed = []

        self.logs = []

        self.stage_start_time = None

        self.stage_times = {}


    # START UI
    def start(self):

        self.live = Live(

            self.render(),

            console=console,

            refresh_per_second=10,

        )

        self.live.start()


    # STOP UI
    def stop(self):

        if self.live:

            self.live.stop()


    # UPDATE STAGE
    def update_stage(self, stage):

        now = time.time()

        if self.current_stage:

            duration = now - self.stage_start_time

            self.completed.append(self.current_stage)

            self.stage_times[self.current_stage] = duration

        self.current_stage = stage

        self.stage_start_time = now

        self.current_message = ""

        self.refresh()


    # ADD LOG
    def log(self, message):

        self.logs.append(message)

        self.logs = self.logs[-10:]

        self.current_message = message

        self.refresh()


    # UPDATE MESSAGE (alias)
    def update_message(self, message):

        self.log(message)


    # COMPLETE
    def complete(self):

        now = time.time()

        if self.current_stage:

            duration = now - self.stage_start_time

            self.completed.append(self.current_stage)

            self.stage_times[self.current_stage] = duration

        self.current_stage = None

        self.refresh(final=True)


    # REFRESH
    def refresh(self, final=False):

        if self.live:

            self.live.update(self.render(final))


    # RENDER UI
    def render(self, final=False):

        layout = Layout()


        # STATUS PANEL

        stage_lines = []

        for stage in self.completed:

            duration = self.stage_times.get(stage, 0)

            stage_lines.append(

                f"[green]✔[/green] {stage} [dim]({duration:.2f}s)[/dim]"

            )


        if self.current_stage and not final:

            spinner = Spinner(

                "dots",

                text=f"[yellow]{self.current_stage}[/yellow]\n[cyan]{self.current_message}[/cyan]"

            )

            stage_panel = Panel(

                spinner,

                border_style="cyan",

                title="Agent Status",

                height=6

            )

        else:

            stage_lines.append(

                "[bold green]✔ Completed[/bold green]"

            )

            stage_panel = Panel(

                "\n".join(stage_lines),

                border_style="green",

                title="Agent Status",

                height=6

            )


        # LOG PANEL

        log_text = "\n".join(

            f"[cyan]•[/cyan] {log}"

            for log in self.logs

        )


        log_panel = Panel(

            log_text,

            border_style="magenta",

            title="Logs",

            height=12

        )


        layout.split_column(

            stage_panel,

            log_panel

        )


        return layout


# HEADER
def show_header():

    console.print(

        Panel.fit(

            "[bold green]CODE GENERATOR AGENT[/bold green]\n"

            "[dim]AI Software Engineer[/dim]",

            border_style="green",

        )

    )