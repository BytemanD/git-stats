# Git Rich Stats

一款基于 Click 和 Rich 库构建的 Git 统计工具，提供丰富的终端输出。

## 功能特性

- **代码行数统计**：查看每位作者的代码增删行数和提交次数
- **提交历史记录**：展示提交详情及变更内容
- **灵活的日期筛选**：支持按今天、本周、本月或自定义日期范围筛选
- **美观的输出格式**：使用 Rich 库实现彩色表格和样式输出

## 安装

```bash
pip install git-rich-stats
```

或者从源码安装：

```bash
git clone https://github.com/BytemanD/git-stats.git
cd git-stats
pip install -e .
```

## 使用方法

### 代码行数统计

```bash
git-rich-stats lines [OPTIONS] [DATE_RANGE]...

# 示例：
git-rich-stats lines                    # 今日统计
git-rich-stats lines today             # 今日统计
git-rich-stats lines yesterday          # 昨日统计
git-rich-stats lines thisweek          # 本周统计
git-rich-stats lines lastweek          # 上周统计
git-rich-stats lines thismonth          # 本月统计
git-rich-stats lines lastmonth         # 上月统计
git-rich-stats lines 2026-01-12 2026-01-22  # 自定义日期范围
```

### 提交历史记录

```bash
git-rich-stats commits [OPTIONS] [DATE_RANGE]...

# 示例：
git-rich-stats commits today            # 今日提交
git-rich-stats commits thisweek         # 本周提交
git-rich-stats commits 2026-01-12 2026-01-22  # 自定义日期范围
```

## 输出示例

### lines 命令

```
2026-03-27 00:00:00 ~ 2026-03-27 23:59:59

            Code lines

 Author    Added  Removed   Total   Commits
 ──────────────────────────────────────────
 John Doe    150       30     180        5
 Jane         80       15      95        3
```

### commits 命令

```
2026-03-27 00:00:00 ~ 2026-03-27 23:59:59

                Commit Details  
┏━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┓
┃ Date             ┃ Author   ┃ Message                  ┃ Changes        ┃
┡━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━┩
│ 2026-03-27 10:30 │ John Doe │  fix: resolve login bug  │ M  src/auth.py │
│                  │          │                          │ M  tests/      │
└──────────────────┴──────────┴──────────────────────────┴────────────────┘
```

## 环境要求

- Python >= 3.10
- click >= 8.3.1
- gitpython >= 3.1.46
- pystonic >= 0.1.7
- rich >= 14.3.3

## 开源协议

MIT
