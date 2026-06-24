# OopsGitHub

OopsGitHub 自动生成 GitHub 系列域名的 hosts 文件，目标是直接产出可用结果。

## 规则

- 每 6 小时通过 GitHub Actions 更新一次。
- DNS 查询使用 DoH：`https://public.dns.iij.jp/dns-query`。
- DNS 查询携带 EDNS Client Subnet：`101.110.0.0/18`，查询结果作为 GitHub 域名的候选 IP。
- 候选 IP 使用 `curl` 访问 `https://域名/` 的 443 端口测试。
- `curl` 测试时使用浏览器 User-Agent，并添加随机 `Client-IP`：`115.196.43.0/24`。
- 每个域名从可用候选 IP 中选择响应时间最优的 IP。

## 使用

复制下面内容到系统 hosts 文件末尾。

```bash
{hosts}
```

最后更新时间：`{update_time}`

hosts 文件位置：

- Windows：`C:\Windows\System32\drivers\etc\hosts`
- macOS：`/etc/hosts`
- Linux：`/etc/hosts`

刷新 DNS：

- Windows：`ipconfig /flushdns`
- macOS：`sudo killall -HUP mDNSResponder`
- Linux：`sudo nscd restart`

## 本地运行

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
python scripts/generate_hosts.py
```
