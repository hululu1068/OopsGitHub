# OopsGitHub

OopsGitHub 让 GitHub 访问更流畅!

- 每 6 小时通过 GitHub Actions 更新一次。
- 模拟真实的客户端请求。
- 每个域名保留最多两个响应时间最优的 IP。
- 同步支持 `hosts`、`smartdns.conf`、`surge.conf` 格式。可配置 `Surge` `Loon` `Mihomo` `Shadowrocket` `Quantumult X`使用。

## 使用

复制下面内容到系统 hosts 文件末尾。

```bash
# OopsGitHub Host Start
# Update time: 2026-06-24T10:55:33+00:00
# Project: https://github.com/hululu1068/OopsGitHub
# Update url: https://github.com/hululu1068/OopsGitHub/raw/main/hosts

140.82.113.26                 alive.github.com
20.27.177.116                 api.github.com
140.82.114.21                 api.individual.githubcopilot.com
185.199.111.133               avatars.githubusercontent.com
185.199.110.133               avatars.githubusercontent.com
185.199.111.133               avatars0.githubusercontent.com
185.199.109.133               avatars0.githubusercontent.com
185.199.111.133               avatars1.githubusercontent.com
185.199.110.133               avatars1.githubusercontent.com
185.199.108.133               avatars2.githubusercontent.com
185.199.111.133               avatars2.githubusercontent.com
185.199.111.133               avatars3.githubusercontent.com
185.199.110.133               avatars3.githubusercontent.com
185.199.110.133               avatars4.githubusercontent.com
185.199.108.133               avatars4.githubusercontent.com
185.199.111.133               avatars5.githubusercontent.com
185.199.110.133               avatars5.githubusercontent.com
185.199.110.133               camo.githubusercontent.com
185.199.111.133               camo.githubusercontent.com
140.82.114.21                 central.github.com
185.199.109.133               cloud.githubusercontent.com
185.199.110.133               cloud.githubusercontent.com
20.27.177.114                 codeload.github.com
# IP Address Not Found         collector.github.com
185.199.111.133               desktop.githubusercontent.com
185.199.109.133               desktop.githubusercontent.com
140.82.114.21                 education.github.com
# IP Address Not Found         favicons.githubusercontent.com
20.27.177.113                 gist.github.com
52.217.79.44                  github-cloud.s3.amazonaws.com
16.15.191.76                  github-cloud.s3.amazonaws.com
52.217.232.1                  github-com.s3.amazonaws.com
16.15.191.76                  github-com.s3.amazonaws.com
52.217.79.44                  github-production-release-asset-2e65be.s3.amazonaws.com
52.217.123.97                 github-production-release-asset-2e65be.s3.amazonaws.com
54.231.136.185                github-production-repository-file-5c1aeb.s3.amazonaws.com
52.217.79.44                  github-production-repository-file-5c1aeb.s3.amazonaws.com
52.217.232.1                  github-production-user-asset-6210df.s3.amazonaws.com
52.216.209.153                github-production-user-asset-6210df.s3.amazonaws.com
192.0.66.2                    github.blog
20.27.177.113                 github.com
140.82.113.18                 github.community
20.99.227.183                 github.dev
185.199.108.215               github.githubassets.com
185.199.110.215               github.githubassets.com
151.101.197.194               github.global.ssl.fastly.net
185.199.108.153               github.io
185.199.111.153               github.io
# IP Address Not Found         github.map.fastly.net
185.199.110.153               githubstatus.com
185.199.108.153               githubstatus.com
140.82.113.26                 live.github.com
185.199.111.133               media.githubusercontent.com
185.199.108.133               media.githubusercontent.com
185.199.110.133               objects.githubusercontent.com
185.199.109.133               objects.githubusercontent.com
13.107.42.16                  pipelines.actions.githubusercontent.com
185.199.111.133               private-user-images.githubusercontent.com
185.199.110.133               private-user-images.githubusercontent.com
185.199.109.133               raw.githubusercontent.com
185.199.108.133               raw.githubusercontent.com
185.199.108.133               user-images.githubusercontent.com
185.199.111.133               user-images.githubusercontent.com
150.171.109.150               vscode.dev

# OopsGitHub Host End
```

最后更新时间：`2026-06-24T10:55:33+00:00`

其他格式：

- SmartDNS：`https://github.com/hululu1068/OopsGitHub/raw/main/smartdns.conf`
- Surge：`https://github.com/hululu1068/OopsGitHub/raw/main/surge.conf`

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
