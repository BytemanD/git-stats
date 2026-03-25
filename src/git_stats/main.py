from typing import Tuple

import click
from git import Repo
from rich import box
from rich.console import Console
from rich.table import Table
from rich.text import Text

console = Console()


@click.group()
def app():
    """Git Stats Tools"""


@app.command()
def lines():
    """Count lines"""
    repo = Repo()
    commits_total: dict[str, Tuple[int, int, int]] = {}
    for commit in repo.iter_commits():
        author = commit.author.email
        total = commit.stats.total

        commits_total.setdefault(author, [0, 0, 0])
        commits_total[author][0] += total.get("insertions", 0)
        commits_total[author][1] += total.get("deletions", 0)
        commits_total[author][2] += total.get("lines", 0)

    table = Table(
        "Author", header_style="bold cyan", title="Commit lines", box=box.SIMPLE
    )
    table.add_column("Added", justify="right")
    table.add_column("Removed", justify="right")
    table.add_column("Total", justify="right")
    for author, commit in commits_total.items():
        table.add_row(
            author,
            Text(str(commit[0]), style="green"),
            Text(str(commit[1]), style="red"),
            str(commit[2]),
        )

    console.print(table)


def main() -> None:
    app()


if __name__ == "__main__":
    main()
