#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import urllib.parse
import urllib.request
from collections import Counter
from pathlib import Path

USERNAME = os.environ.get("GITHUB_REPOSITORY_OWNER", "huangbogeng")
TOKEN = os.environ["GITHUB_TOKEN"]
OUTPUT = Path("assets/contributions.svg")

API = "https://api.github.com"
GRAPHQL = "https://api.github.com/graphql"


def request_json(url: str, *, method: str = "GET", payload: dict | None = None):
    data = None if payload is None else json.dumps(payload).encode()
    req = urllib.request.Request(
        url,
        data=data,
        method=method,
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": f"{USERNAME}-profile-metrics",
            "Content-Type": "application/json",
        },
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.load(resp)


def public_projects() -> int:
    page = 1
    total = 0
    while True:
        url = f"{API}/users/{USERNAME}/repos?type=owner&visibility=public&per_page=100&page={page}"
        repos = request_json(url)
        total += len(repos)
        if len(repos) < 100:
            return total
        page += 1


def merged_external_prs() -> list[dict]:
    query = f"is:pr is:merged author:{USERNAME}"
    items: list[dict] = []
    page = 1
    while True:
        params = urllib.parse.urlencode(
            {"q": query, "per_page": 100, "page": page, "sort": "updated", "order": "desc"}
        )
        result = request_json(f"{API}/search/issues?{params}")
        batch = result.get("items", [])
        items.extend(batch)
        if len(batch) < 100 or len(items) >= min(result.get("total_count", 0), 1000):
            break
        page += 1

    prefix = f"{API}/repos/"
    external = []
    for item in items:
        repo_url = item.get("repository_url", "")
        full_name = repo_url[len(prefix):] if repo_url.startswith(prefix) else ""
        owner = full_name.split("/", 1)[0] if "/" in full_name else ""
        if owner.lower() != USERNAME.lower():
            item["_repo"] = full_name
            external.append(item)
    return external


def last_year_contributions() -> int:
    query = """
    query($login: String!) {
      user(login: $login) {
        contributionsCollection {
          contributionCalendar { totalContributions }
        }
      }
    }
    """
    result = request_json(
        GRAPHQL,
        method="POST",
        payload={"query": query, "variables": {"login": USERNAME}},
    )
    return int(
        result["data"]["user"]["contributionsCollection"]["contributionCalendar"]["totalContributions"]
    )


def bucket(repo: str) -> str:
    owner, _, name = repo.partition("/")
    low = repo.lower()
    if owner.lower() == "aequiludium":
        return "Aequiludium"
    if owner.lower() == "point72":
        return "Point72"
    if "polars" in low or owner.lower() in {"abstractqqq", "pola-rs"}:
        return "Polars ecosystem"
    return "Other upstream"


def esc(text: str) -> str:
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def render_svg(projects: int, prs: list[dict], yearly: int) -> str:
    repos = sorted({p["_repo"] for p in prs if p.get("_repo")})
    counts = Counter(bucket(repo) for repo in (p["_repo"] for p in prs if p.get("_repo")))
    order = ["Aequiludium", "Polars ecosystem", "Point72", "Other upstream"]
    max_count = max([counts[k] for k in order] + [1])

    width = 900
    height = 330
    metric_x = [28, 248, 468, 688]
    metrics = [
        ("Public Projects", projects),
        ("Merged External PRs", len(prs)),
        ("Contributed Repos", len(repos)),
        ("Last-year Contributions", yearly),
    ]

    rows = []
    y0 = 196
    for i, name in enumerate(order):
        value = counts[name]
        bar_w = round(560 * value / max_count)
        y = y0 + i * 29
        rows.append(
            f'<text x="28" y="{y}" class="label">{esc(name)}</text>'
            f'<rect x="218" y="{y-13}" width="560" height="12" rx="6" class="track"/>'
            f'<rect x="218" y="{y-13}" width="{bar_w}" height="12" rx="6" class="bar b{i}"/>'
            f'<text x="804" y="{y}" class="count">{value}</text>'
        )

    metric_nodes = []
    for x, (label, value) in zip(metric_x, metrics):
        metric_nodes.append(
            f'<text x="{x}" y="83" class="metric">{value}</text>'
            f'<text x="{x}" y="108" class="small">{esc(label)}</text>'
        )

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="GitHub open-source contribution metrics">
<style>
  :root {{ color-scheme: light dark; }}
  .bg {{ fill: #ffffff; stroke: #d0d7de; }}
  .title {{ fill: #1f2328; font: 600 18px -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif; }}
  .metric {{ fill: #1f2328; font: 600 28px ui-monospace,SFMono-Regular,Consolas,monospace; }}
  .small,.label,.count {{ fill: #57606a; font: 13px -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif; }}
  .count {{ text-anchor: end; font-family: ui-monospace,SFMono-Regular,Consolas,monospace; }}
  .track {{ fill: #eaeef2; }}
  .bar {{ fill: #656d76; }}
  .b1 {{ fill: #7d8590; }}
  .b2 {{ fill: #8c959f; }}
  .b3 {{ fill: #afb8c1; }}
  .rule {{ stroke: #d8dee4; }}
  @media (prefers-color-scheme: dark) {{
    .bg {{ fill: #0d1117; stroke: #30363d; }}
    .title,.metric {{ fill: #e6edf3; }}
    .small,.label,.count {{ fill: #8d96a0; }}
    .track {{ fill: #21262d; }}
    .bar {{ fill: #8b949e; }}
    .b1 {{ fill: #7d8590; }}
    .b2 {{ fill: #6e7681; }}
    .b3 {{ fill: #484f58; }}
    .rule {{ stroke: #30363d; }}
  }}
</style>
<rect x="0.5" y="0.5" width="{width-1}" height="{height-1}" rx="8" class="bg"/>
<text x="28" y="38" class="title">Open-source activity</text>
{''.join(metric_nodes)}
<line x1="28" y1="137" x2="872" y2="137" class="rule"/>
<text x="28" y="168" class="small">Merged external PR distribution</text>
{''.join(rows)}
<text x="28" y="315" class="small">Automatically refreshed daily from GitHub.</text>
</svg>'''


def main() -> None:
    projects = public_projects()
    prs = merged_external_prs()
    yearly = last_year_contributions()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(render_svg(projects, prs, yearly), encoding="utf-8")
    print(
        f"projects={projects} merged_external_prs={len(prs)} "
        f"contributed_repos={len({p['_repo'] for p in prs})} yearly={yearly}"
    )


if __name__ == "__main__":
    main()
