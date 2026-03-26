from datetime import datetime
from typing import Set, Tuple

from git import Repo
from pystonic.utils import dateutil


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


def lines(since: datetime, until: datetime):
    repo = Repo()
    commits_total: dict[str, Tuple[int, int, int, int]] = {}
    for commit in repo.iter_commits(since=since, until=until):
        author = commit.author.name or commit.author.email or "Unknown"
        total = commit.stats.total

        commits_total.setdefault(author, [0, 0, 0, 0])
        commits_total[author][0] += total.get("insertions", 0)
        commits_total[author][1] += total.get("deletions", 0)
        commits_total[author][2] += total.get("lines", 0)
        commits_total[author][3] += 1

    return commits_total
