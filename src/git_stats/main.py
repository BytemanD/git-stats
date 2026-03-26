from datetime import datetime
from typing import Set, Tuple

import click
from pystonic.utils import dateutil
from rich import box
from rich.console import Console
from rich.table import Column, Table
from rich.text import Text

from git_stats.core import stats

console = Console()

def parse_date_range(date_range: Set[str]) -> Tuple[datetime, datetime]:
    """Parse date range"""
    if not date_range:
        return dateutil.thisday()
    if len(date_range) == 1:
        if date_range[0] in ["today", "thisday"]:
            return dateutil.thisday()
        if date_range[0] == "yesterday":
            return dateutil.yestoday()
        if date_range[0] == "thisweek":
            return dateutil.thisweek()
        if date_range[0] == "lastweek":
            return dateutil.lastweek()
        if date_range[0] == "thismonth":
            return dateutil.thismonth()
        if date_range[0] == "lastmonth":
            return dateutil.lastmonth()
        return datetime.strptime(
            date_range[0], dateutil.FORMAT_DATETIME
        ), datetime.now()
    elif len(date_range) == 2:
        return datetime.strptime(
            date_range[0], dateutil.FORMAT_DATETIME
        ), datetime.strptime(date_range[1], dateutil.FORMAT_DATETIME)

    raise ValueError("Invalid date range")

@click.group()
def app():
    """Git Stats Tools"""


@app.command()
@click.argument("date_range", nargs=-1, default=[], required=False)
def lines(date_range: Set[str]):
    """Count lines

    \b
    e.g.
        git-stats lines
        git-stats lines <today | yesterday | thisweek | thismonth>
        git-stats lines 2026-01-12 2026-01-22
        ...
    """
    try:
        since, until = parse_date_range(date_range)
    except ValueError:
        raise click.BadParameter("parse date range error")

    commits_total = stats.lines(since, until)

    console.print(
        f"{since:%Y-%m-%d %H:%M:%S} ~ {until:%Y-%m-%d %H:%M:%S}", style="cyan underline"
    )
    click.secho()

    table = Table(
        Column("Author"),
        Column("Added", justify="right"),
        Column("Removed", justify="right"),
        Column("Total", justify="right"),
        Column("Commits", justify="right"),
        title="Code lines",
        box=box.SIMPLE,
    )
    for author, commit in commits_total.items():
        table.add_row(
            author,
            Text(str(commit[0]), style="green"),
            Text(str(commit[1]), style="red"),
            Text(str(commit[2]), style="magenta"),
            str(commit[3]),
        )

    console.print(table)


def main() -> None:
    app()


if __name__ == "__main__":
    main()
