from datetime import datetime
from typing import List, Tuple

from git import Repo, Commit
from pydantic import BaseModel
from pystonic.utils import dateutil


def parse_date_range(date_range: Tuple[str]) -> Tuple[datetime, datetime]:
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


class CommitStats(BaseModel):
    author: str = ""
    added: int = 0
    removed: int = 0
    total: int = 0
    commits: int = 0


class CommitDetail(BaseModel):
    author: str = ""
    date: str = ""
    message: str = ""
    changes: List[str] = []

    @classmethod
    def from_git_commit(cls, commit: Commit):
        return cls(
            author=commit.author.name or commit.author.email or "Unknown",
            date=commit.authored_datetime.strftime(dateutil.FORMAT_DATETIME),
            message=(
                commit.message.decode("utf-8")
                if isinstance(commit.message, bytes)
                else str(commit.message)
            ),
            changes=[
                f"{x.change_type} {x.a_path}"
                for x in commit.diff(commit.parents[0] if commit.parents else None)
            ],
        )


def lines(since: datetime, until: datetime):
    repo = Repo()
    commit_stats: dict[str, CommitStats] = {}
    for commit in repo.iter_commits(since=since, until=until):
        author = commit.author.name or commit.author.email or "Unknown"
        total = commit.stats.total

        commit_stats.setdefault(author, CommitStats(author=author))

        commit_stats[author].added += total.get("insertions", 0)
        commit_stats[author].removed += total.get("deletions", 0)
        commit_stats[author].total += total.get("lines", 0)
        commit_stats[author].commits += 1

    return [x for x in commit_stats.values()]


def commits(since: datetime, until: datetime):
    repo = Repo()
    return [
        CommitDetail.from_git_commit(commit)
        for commit in repo.iter_commits(since=since, until=until)
    ]
