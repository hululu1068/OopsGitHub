# OopsGitHub

OopsGitHub 让 GitHub 访问更流畅!

- 每 6 小时通过 GitHub Actions 更新一次。
- 模拟真实的客户端请求。
- 每个域名保留最多两个响应时间最优的 IP。
- 同步支持 `hosts`、`smartdns.conf`、`surge.sgmodule` 格式。可配置 `Surge` `Loon` `Mihomo` `Shadowrocket` `Quantumult X`使用。

## 使用

复制下面内容到系统 hosts 文件末尾。

```bash
# OopsGitHub Host Start
# Update time: 2026-07-19T19:01:31+00:00
# Project: https://github.com/hululu1068/OopsGitHub
# Update url: https://github.com/hululu1068/OopsGitHub/raw/main/hosts

20.27.177.113                 github.com
140.82.114.18                 github.community
192.0.66.2                    github.blog
20.99.227.183                 github.dev
185.199.108.153               github.io
185.199.110.153               github.io
185.199.110.153               githubstatus.com
185.199.109.153               githubstatus.com
# IP Address Not Found         githubassets.com
# IP Address Not Found         githubusercontent.com
140.82.114.30                 githubapp.com
140.82.114.29                 githubapp.com
185.199.111.153               githubnext.com
185.199.110.153               githubnext.com
# IP Address Not Found         githubpreview.dev
140.82.113.17                 githubhackathon.com
185.199.108.153               githubuniverse.com
185.199.110.153               githubuniverse.com
140.82.113.22                 education.github.com
185.199.111.153               myoctocat.com
185.199.110.153               myoctocat.com
185.199.108.153               opensource.guide
185.199.110.153               opensource.guide
140.82.114.17                 repo.new
23.227.38.65                  thegithubshop.com
20.27.177.116                 api.github.com
140.82.114.26                 alive.github.com
140.82.114.26                 live.github.com
140.82.113.22                 central.github.com
140.82.113.22                 collector.github.com
185.199.111.215               github.githubassets.com
185.199.108.215               github.githubassets.com
# IP Address Not Found         assets-cdn.github.com
151.101.197.194               github.global.ssl.fastly.net
# IP Address Not Found         github.map.fastly.net
185.199.109.133               favicons.githubusercontent.com
185.199.111.133               favicons.githubusercontent.com
185.199.109.133               raw.githubusercontent.com
185.199.110.133               raw.githubusercontent.com
185.199.111.133               media.githubusercontent.com
185.199.108.133               media.githubusercontent.com
185.199.108.133               objects.githubusercontent.com
185.199.111.133               objects.githubusercontent.com
185.199.108.133               cloud.githubusercontent.com
185.199.111.133               cloud.githubusercontent.com
185.199.109.133               camo.githubusercontent.com
185.199.111.133               camo.githubusercontent.com
185.199.111.133               user-images.githubusercontent.com
185.199.108.133               user-images.githubusercontent.com
185.199.110.133               private-user-images.githubusercontent.com
185.199.109.133               private-user-images.githubusercontent.com
185.199.109.133               avatars.githubusercontent.com
185.199.110.133               avatars.githubusercontent.com
185.199.108.133               avatars0.githubusercontent.com
185.199.109.133               avatars0.githubusercontent.com
185.199.109.133               avatars1.githubusercontent.com
185.199.111.133               avatars1.githubusercontent.com
185.199.111.133               avatars2.githubusercontent.com
185.199.108.133               avatars2.githubusercontent.com
185.199.110.133               avatars3.githubusercontent.com
185.199.109.133               avatars3.githubusercontent.com
185.199.110.133               avatars4.githubusercontent.com
185.199.111.133               avatars4.githubusercontent.com
185.199.111.133               avatars5.githubusercontent.com
185.199.108.133               avatars5.githubusercontent.com
20.27.177.114                 codeload.github.com
20.27.177.113                 gist.github.com
185.199.109.133               desktop.githubusercontent.com
185.199.111.133               desktop.githubusercontent.com
185.199.108.133               release-assets.githubusercontent.com
185.199.111.133               release-assets.githubusercontent.com
13.107.42.16                  pipelines.actions.githubusercontent.com
# IP Address Not Found         blob.core.windows.net
54.231.160.161                github-cloud.s3.amazonaws.com
16.15.253.129                 github-cloud.s3.amazonaws.com
54.231.160.161                github-com.s3.amazonaws.com
52.217.166.121                github-com.s3.amazonaws.com
54.231.160.161                github-production-release-asset-2e65be.s3.amazonaws.com
52.217.166.121                github-production-release-asset-2e65be.s3.amazonaws.com
54.231.160.161                github-production-repository-file-5c1aeb.s3.amazonaws.com
16.15.253.129                 github-production-repository-file-5c1aeb.s3.amazonaws.com
54.231.160.161                github-production-user-asset-6210df.s3.amazonaws.com
16.15.229.119                 github-production-user-asset-6210df.s3.amazonaws.com
# IP Address Not Found         githubcopilot.com
140.82.113.22                 api.individual.githubcopilot.com
20.27.177.117                 ghcr.io
140.82.112.18                 atom.io
140.82.114.17                 dependabot.com
140.82.114.21                 git.io
104.17.135.117                npmjs.com
104.17.134.117                npmjs.com
104.16.10.34                  npmjs.org
104.16.11.34                  npmjs.org
# IP Address Not Found         npm.community
47.79.66.58                   github-avatars.oss-cn-hongkong.aliyuncs.com
151.101.198.79                github-atom-io-herokuapp-com.freetls.fastly.net
150.171.109.145               vscode.dev
104.21.24.61                  rawgit.com
172.67.217.78                 rawgit.com
# IP Address Not Found         rawgithub.com

# OopsGitHub Host End
```

最后更新时间：`2026-07-19T19:01:31+00:00`

其他格式：

- SmartDNS：`https://github.com/hululu1068/OopsGitHub/raw/main/smartdns.conf`
- Surge：`https://github.com/hululu1068/OopsGitHub/raw/main/surge.sgmodule`

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
