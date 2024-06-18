import typer
from rich.progress import Progress, SpinnerColumn, TextColumn

from pydev.llm.client import LLMClient


def prompt_llm(ctx: typer.Context, prompt: str) -> str:
    llm_client: LLMClient = ctx.meta["llm_client"]

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
    ) as progress:
        task = progress.add_task("Waiting for LLM response...", start=False)
        result = llm_client.invoke(prompt)
        progress.update(task, completed=True)

    return result
