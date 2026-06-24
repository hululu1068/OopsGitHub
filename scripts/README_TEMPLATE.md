# OopsGitHub

OopsGitHub 让 GitHub 访问更流畅!

- 每 6 小时通过 GitHub Actions 更新一次。
- 模拟真实的客户端请求。
- 每个域名保留最多两个响应时间最优的 IP。
- 同步支持 `hosts`、`smartdns.conf`、`surge.conf` 格式。可配置 `Surge` `Loon` `Mihomo` `Shadowrocket` `Quantumult X`使用。

## 使用

复制下面内容到系统 hosts 文件末尾。

```bash
{hosts}
```

最后更新时间：`{update_time}`

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
