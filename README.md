# AI-paper

从指定 B 站 UP 采集论文相关视频 → 抽取 arXiv/链接 → LLM 生成「原文 / 解析 / 可以做什么」→ 每天 **00:00** 自动提交并推送到本仓库。

仓库：https://github.com/caoh302930/AI-paper

## 目录结构

```
config/ups.yaml          # UP 名单（可追加）
papers/YYYY/MM/<id>/
  00_meta.md
  01_原文.md
  02_解析.md
  03_可以做什么.md
index.md                 # 总索引
state/seen.json          # 去重状态
scripts/run_daily.py     # 主流程
```

## 本地配置

```bash
cd /data/machine_learning/cmh/文本/paper/AI-paper
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # 填入 LLM_API_KEY 等
```

`.env` **不要提交**（已在 `.gitignore`）。

## 手动跑一次

```bash
./scripts/run.sh
```

## 定时任务（每天 00:00）

```bash
crontab -e
# 加入：
0 0 * * * /data/machine_learning/cmh/文本/paper/AI-paper/scripts/run.sh >> /data/machine_learning/cmh/文本/paper/AI-paper/logs/cron.log 2>&1
```

或执行：

```bash
./scripts/install_cron.sh
```

## 追加 UP

编辑 `config/ups.yaml`：

```yaml
ups:
  - mid: "581897590"
    name: "Agent智能体深度研究院"
    enabled: true
  - mid: "新的UID"
    name: "名字"
    enabled: true
```

## LLM

默认 OpenAI 兼容接口：

- `LLM_BASE_URL`
- `LLM_MODEL`
- `LLM_API_KEY`

## B 站采集说明

本机访问 `api.bilibili.com` 容易触发风控（返回验证码页）。请在 `.env` 配置：

```bash
BILI_COOKIE=SESSDATA=...; bili_jct=...; DedeUserID=...
```

Cookie 获取：浏览器登录 B 站 → F12 → Network → 任意请求 → Request Headers → Cookie。

可选备用：自建 [RSSHub](https://github.com/DIYgod/RSSHub) 后设置 `RSSHUB_URL`。
