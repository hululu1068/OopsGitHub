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
# OopsGitHub Host Start
# Update time: 2026-06-24T09:48:43+00:00
# DoH: https://public.dns.iij.jp/dns-query
# EDNS Client Subnet: 101.110.0.0/18
# Candidate IPs: queried by DoH with EDNS Client Subnet
# Curl test: HTTPS 443 with browser User-Agent and random Client-IP from 115.196.43.0/24
140.82.114.25                 alive.github.com
20.27.177.116                 api.github.com
140.82.113.21                 api.individual.githubcopilot.com
# IP Address Not Found         assets-cdn.github.com
185.199.111.133               avatars.githubusercontent.com
185.199.110.133               avatars0.githubusercontent.com
185.199.111.133               avatars1.githubusercontent.com
185.199.110.133               avatars2.githubusercontent.com
185.199.108.133               avatars3.githubusercontent.com
185.199.110.133               avatars4.githubusercontent.com
185.199.109.133               avatars5.githubusercontent.com
185.199.110.133               camo.githubusercontent.com
140.82.113.21                 central.github.com
185.199.109.133               cloud.githubusercontent.com
20.27.177.114                 codeload.github.com
140.82.113.21                 collector.github.com
185.199.108.133               desktop.githubusercontent.com
140.82.113.21                 education.github.com
# IP Address Not Found         favicons.githubusercontent.com
20.27.177.113                 gist.github.com
16.182.38.161                 github-cloud.s3.amazonaws.com
16.182.38.161                 github-com.s3.amazonaws.com
52.217.73.52                  github-production-release-asset-2e65be.s3.amazonaws.com
16.182.38.161                 github-production-repository-file-5c1aeb.s3.amazonaws.com
16.182.40.209                 github-production-user-asset-6210df.s3.amazonaws.com
192.0.66.2                    github.blog
20.27.177.113                 github.com
140.82.114.17                 github.community
20.99.227.183                 github.dev
185.199.108.215               github.githubassets.com
151.101.197.194               github.global.ssl.fastly.net
185.199.108.153               github.io
# IP Address Not Found         github.map.fastly.net
185.199.111.153               githubstatus.com
140.82.114.25                 live.github.com
185.199.108.133               media.githubusercontent.com
185.199.109.133               objects.githubusercontent.com
13.107.42.16                  pipelines.actions.githubusercontent.com
185.199.110.133               private-user-images.githubusercontent.com
185.199.109.133               raw.githubusercontent.com
185.199.109.133               user-images.githubusercontent.com
13.107.253.69                 vscode.dev
# OopsGitHub Host End
```

最后更新时间：`2026-06-24T09:48:43+00:00`

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
