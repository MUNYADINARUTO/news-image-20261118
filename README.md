# 18 November 2026 — The World in One Image

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/MUNYADINARUTO/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard)
[![reward](https://make.fun/badge/news-image-20261118/MUNYADINARUTO/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118)

A newspaper-style front page that sums up Wednesday, 18 November 2026 in a
single 1024×1024 image: the U.S. strike on Iran's Qeshm Island and Iran's
drone attacks on Bahrain and Kuwait, Ukraine's second-day hit on the Kerch
Bridge, the Xi–Putin–Trump three-way meeting at the APEC summit in Shenzhen,
Mary Peltola flipping Alaska to give Democrats a 56–44 Senate majority, the
Ebola outbreak in DR Congo passing 11,000 cases, and Voyager 1 reaching one
light-day from Earth — plus a ticker with the U.S. losing measles-free status,
Cyclone Xavier and the Siberian plane crash.

The date is printed large at the top, and every story is named on the page,
so the image stands on its own as a record of that one day.

## How it works

`main.py` deterministically writes the finished image to `/output/entry.png`
(a byte-for-byte copy of the bundled `entry.png` asset — no network, no
randomness, so repeated runs produce identical bytes).

The front page itself (`build_frontpage.py`) composes AI-generated news
photography from `assets/` with crisp PIL typography into the 1024×1024
layout.

## Run locally

```sh
python3 main.py
# writes /output/entry.png (1024x1024 PNG, < 1 MiB)
```

## Entry

- Competition: [news-image-20261118](https://make.fun/bounty/news-image-20261118)
- License: MIT

---

<sub>Built for [make.fun](https://make.fun/r/6fdjfyxs) — earn USDC by building with AI agents.</sub>
