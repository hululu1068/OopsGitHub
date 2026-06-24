#!/usr/bin/env python3
from __future__ import annotations

import ipaddress
import json
import random
import statistics
import subprocess
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

import dns.edns
import dns.message
import dns.rdatatype


ROOT = Path(__file__).resolve().parents[1]
PROJECT_URL = "https://github.com/hululu1068/OopsGitHub"
HOSTS_UPDATE_URL = f"{PROJECT_URL}/raw/main/hosts"
SMARTDNS_UPDATE_URL = f"{PROJECT_URL}/raw/main/smartdns.conf"
SURGE_UPDATE_URL = f"{PROJECT_URL}/raw/main/surge.conf"
DOH_ENDPOINT = "https://public.dns.iij.jp/dns-query"
EDNS_CLIENT_SUBNET = "101.110.0.0"
EDNS_PREFIX = 18
CLIENT_IP_POOL = ipaddress.ip_network("115.196.43.0/24")
USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/149.0.0.0 Safari/537.36"
)

DNS_TIMEOUT_SECONDS = 8
CURL_CONNECT_TIMEOUT_SECONDS = 3
CURL_MAX_TIME_SECONDS = 8
CURL_ATTEMPTS = 2

GITHUB_DOMAINS = [
    "alive.github.com",
    "api.github.com",
    "api.individual.githubcopilot.com",
    "avatars.githubusercontent.com",
    "avatars0.githubusercontent.com",
    "avatars1.githubusercontent.com",
    "avatars2.githubusercontent.com",
    "avatars3.githubusercontent.com",
    "avatars4.githubusercontent.com",
    "avatars5.githubusercontent.com",
    "camo.githubusercontent.com",
    "central.github.com",
    "cloud.githubusercontent.com",
    "codeload.github.com",
    "collector.github.com",
    "desktop.githubusercontent.com",
    "education.github.com",
    "favicons.githubusercontent.com",
    "gist.github.com",
    "github-cloud.s3.amazonaws.com",
    "github-com.s3.amazonaws.com",
    "github-production-release-asset-2e65be.s3.amazonaws.com",
    "github-production-repository-file-5c1aeb.s3.amazonaws.com",
    "github-production-user-asset-6210df.s3.amazonaws.com",
    "github.blog",
    "github.com",
    "github.community",
    "github.dev",
    "github.githubassets.com",
    "github.global.ssl.fastly.net",
    "github.io",
    "github.map.fastly.net",
    "githubstatus.com",
    "live.github.com",
    "media.githubusercontent.com",
    "objects.githubusercontent.com",
    "pipelines.actions.githubusercontent.com",
    "private-user-images.githubusercontent.com",
    "raw.githubusercontent.com",
    "user-images.githubusercontent.com",
    "vscode.dev",
]


@dataclass(frozen=True)
class CurlResult:
    ip: str
    ok: bool
    http_code: int
    time_connect: float
    time_appconnect: float
    time_starttransfer: float
    time_total: float
    client_ip: str
    error: str = ""


@dataclass(frozen=True)
class SelectedHost:
    domain: str
    ips: list[str]
    candidates: list[str]
    curl_results: list[CurlResult]


def query_a_records(domain: str) -> list[str]:
    query = dns.message.make_query(domain, dns.rdatatype.A)
    query.use_edns(
        edns=0,
        payload=1232,
        options=[
            dns.edns.ECSOption(
                address=EDNS_CLIENT_SUBNET,
                srclen=EDNS_PREFIX,
                scopelen=0,
            )
        ],
    )

    request = urllib.request.Request(
        DOH_ENDPOINT,
        data=query.to_wire(),
        headers={
            "Accept": "application/dns-message",
            "Content-Type": "application/dns-message",
        },
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=DNS_TIMEOUT_SECONDS) as response:
        dns_response = dns.message.from_wire(response.read())

    ips: set[str] = set()
    for answer in dns_response.answer:
        for item in answer.items:
            if item.rdtype == dns.rdatatype.A:
                ips.add(item.address)
    return sorted(ips, key=ipaddress.ip_address)


def random_client_ip() -> str:
    return str(ipaddress.ip_address(random.randint(
        int(CLIENT_IP_POOL.network_address) + 1,
        int(CLIENT_IP_POOL.broadcast_address) - 1,
    )))


def curl_probe(domain: str, ip: str) -> CurlResult:
    client_ip = random_client_ip()
    write_out = "%{http_code}\t%{time_connect}\t%{time_appconnect}\t%{time_starttransfer}\t%{time_total}\t%{ssl_verify_result}"
    command = [
        "curl",
        "--silent",
        "--show-error",
        "--output",
        "/dev/null",
        "--write-out",
        write_out,
        "--connect-timeout",
        str(CURL_CONNECT_TIMEOUT_SECONDS),
        "--max-time",
        str(CURL_MAX_TIME_SECONDS),
        "--user-agent",
        USER_AGENT,
        "--header",
        f"Client-IP: {client_ip}",
        "--resolve",
        f"{domain}:443:{ip}",
        f"https://{domain}/",
    ]
    completed = subprocess.run(
        command,
        text=True,
        capture_output=True,
        check=False,
    )

    try:
        code, t_conn, t_tls, t_first, t_total, ssl_result = completed.stdout.strip().split("\t")
        http_code = int(code)
        time_connect = float(t_conn)
        time_appconnect = float(t_tls)
        time_starttransfer = float(t_first)
        time_total = float(t_total)
        ssl_ok = int(ssl_result) == 0
    except ValueError:
        return CurlResult(ip, False, 0, 0, 0, 0, 0, client_ip, completed.stderr.strip())

    ok = completed.returncode == 0 and ssl_ok and 200 <= http_code <= 500
    return CurlResult(
        ip=ip,
        ok=ok,
        http_code=http_code,
        time_connect=time_connect,
        time_appconnect=time_appconnect,
        time_starttransfer=time_starttransfer,
        time_total=time_total,
        client_ip=client_ip,
        error=completed.stderr.strip(),
    )


def pick_best(domain: str, candidates: list[str]) -> SelectedHost:
    results: list[CurlResult] = []
    tasks = [
        ip
        for ip in candidates
        for _ in range(CURL_ATTEMPTS)
    ]
    with ThreadPoolExecutor(max_workers=min(8, len(tasks))) as executor:
        results.extend(executor.map(lambda ip: curl_probe(domain, ip), tasks))

    successful = [result for result in results if result.ok]
    if not successful:
        return SelectedHost(domain, [], candidates, results)

    def score(ip: str) -> tuple[float, float, str]:
        ip_results = [result for result in successful if result.ip == ip]
        totals = [result.time_total for result in ip_results]
        first_bytes = [result.time_starttransfer for result in ip_results]
        return (
            statistics.median(totals),
            statistics.median(first_bytes),
            ip,
        )

    best_ips = sorted({result.ip for result in successful}, key=score)[:2]
    return SelectedHost(domain, best_ips, candidates, results)


def generate() -> tuple[str, list[SelectedHost]]:
    selected_hosts: list[SelectedHost] = []
    for index, domain in enumerate(GITHUB_DOMAINS, start=1):
        print(f"[{index}/{len(GITHUB_DOMAINS)}] resolve {domain}")
        try:
            candidates = query_a_records(domain)
        except Exception as exc:
            print(f"  DNS failed: {exc}")
            selected_hosts.append(SelectedHost(domain, [], [], []))
            continue

        if not candidates:
            print("  no A record")
            selected_hosts.append(SelectedHost(domain, [], [], []))
            continue

        selected = pick_best(domain, candidates)
        if selected.ips:
            print(f"  selected {', '.join(selected.ips)} from {', '.join(candidates)}")
        else:
            print(f"  no reachable candidate from {', '.join(candidates)}")
        selected_hosts.append(selected)

    update_time = datetime.now(timezone.utc).astimezone().replace(microsecond=0).isoformat()
    lines = [
        "# OopsGitHub Host Start",
        f"# Update time: {update_time}",
        f"# Project: {PROJECT_URL}",
        f"# Update url: {HOSTS_UPDATE_URL}",
        "",
    ]
    for selected in selected_hosts:
        if selected.ips:
            for ip in selected.ips:
                lines.append(f"{ip.ljust(30)}{selected.domain}")
        else:
            lines.append(f"# IP Address Not Found         {selected.domain}")
    lines.append("")
    lines.append("# OopsGitHub Host End")
    return "\n".join(lines) + "\n", selected_hosts, update_time


def format_smartdns(selected_hosts: list[SelectedHost], update_time: str) -> str:
    lines = [
        "# OopsGitHub SmartDNS",
        f"# Update time: {update_time}",
        f"# Project: {PROJECT_URL}",
        f"# Update url: {SMARTDNS_UPDATE_URL}",
        "",
    ]
    for selected in selected_hosts:
        for ip in selected.ips:
            lines.append(f"address /{selected.domain}/{ip}")
    return "\n".join(lines) + "\n"


def format_surge(selected_hosts: list[SelectedHost], update_time: str) -> str:
    lines = [
        "# OopsGitHub Surge",
        f"# Update time: {update_time}",
        f"# Project: {PROJECT_URL}",
        f"# Update url: {SURGE_UPDATE_URL}",
        "",
    ]
    for selected in selected_hosts:
        for ip in selected.ips:
            lines.append(f"{selected.domain} = {ip}")
    return "\n".join(lines) + "\n"


def write_readme(hosts_content: str, update_time: str) -> None:
    template_path = ROOT / "scripts" / "README_TEMPLATE.md"
    if not template_path.exists():
        return
    readme = template_path.read_text(encoding="utf-8")
    readme = readme.replace("{hosts}", hosts_content.strip())
    readme = readme.replace("{update_time}", update_time)
    (ROOT / "README.md").write_text(readme, encoding="utf-8")


def write_report(selected_hosts: list[SelectedHost]) -> None:
    report = []
    for selected in selected_hosts:
        report.append({
            "domain": selected.domain,
            "selected_ips": selected.ips,
            "candidates": selected.candidates,
            "curl_results": [
                {
                    "ip": result.ip,
                    "ok": result.ok,
                    "http_code": result.http_code,
                    "time_connect": result.time_connect,
                    "time_appconnect": result.time_appconnect,
                    "time_starttransfer": result.time_starttransfer,
                    "time_total": result.time_total,
                    "client_ip": result.client_ip,
                    "error": result.error,
                }
                for result in selected.curl_results
            ],
        })
    (ROOT / "report.json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def main() -> None:
    hosts_content, selected_hosts, update_time = generate()
    (ROOT / "hosts").write_text(hosts_content, encoding="utf-8")
    (ROOT / "smartdns.conf").write_text(format_smartdns(selected_hosts, update_time), encoding="utf-8")
    (ROOT / "surge.conf").write_text(format_surge(selected_hosts, update_time), encoding="utf-8")
    write_readme(hosts_content, update_time)
    write_report(selected_hosts)


if __name__ == "__main__":
    main()
