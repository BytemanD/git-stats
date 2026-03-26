# Git Rich Stats

A Git statistics tool with rich terminal output, built with Click and Rich.

## Features

- **Code Lines Stats**: View code additions, deletions, and commit counts per author
- **Commit History**: Display commit details with changes
- **Flexible Date Filtering**: Filter by today, this week, this month, or custom date ranges
- **Beautiful Output**: Rich-formatted tables with colors and styling

## Installation

```bash
pip install git-rich-stats
```

Or install from source:

```bash
git clone https://github.com/BytemanD/git-stats.git
cd git-stats
pip install -e .
```

## Usage

### Code Lines

```bash
git-rich-stats lines [OPTIONS] [DATE_RANGE]...

# Examples:
git-rich-stats lines                    # Today's stats
git-rich-stats lines today              # Today's stats
git-rich-stats lines yesterday          # Yesterday's stats
git-rich-stats lines thisweek           # This week's stats
git-rich-stats lines lastweek           # Last week's stats
git-rich-stats lines thismonth           # This month's stats
git-rich-stats lines lastmonth          # Last month's stats
git-rich-stats lines 2026-01-12 2026-01-22  # Custom date range
```

### Commit History

```bash
git-rich-stats commits [OPTIONS] [DATE_RANGE]...

# Examples:
git-rich-stats commits today            # Today's commits
git-rich-stats commits thisweek         # This week's commits
git-rich-stats commits 2026-01-12 2026-01-22  # Custom date range
```

## Output Example

### Lines Command

```
2026-03-27 00:00:00 ~ 2026-03-27 23:59:59

            Code lines

 Author    Added  Removed   Total  Commits
──────────────────────────────────────────
 John Doe    150       30     180        5
 Jane         80       15      95        3
```

### Commits Command

2026-03-27 00:00:00 ~ 2026-03-27 23:59:59

                Commit Details
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┓
┃ Date             ┃ Author   ┃ Message                  ┃ Changes        ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━┩
│ 2026-03-27 10:30 │ John Doe │  fix: resolve login bug  │ M  src/auth.py │
│                  │          │                          │ M  tests/      │
└──────────────────┴──────────┴──────────────────────────┴────────────────┘
```

## Requirements

- Python >= 3.10
- click >= 8.3.1
- gitpython >= 3.1.46
- pystonic >= 0.1.7
- rich >= 14.3.3

## License

MIT
