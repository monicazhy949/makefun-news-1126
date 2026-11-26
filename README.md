# makefun-news-1126

[![Competition](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126)
[![Rank](https://make.fun/badge/news-image-20261126/monicazhy949/makefun-news-1126/rank.svg)](https://make.fun/bounty/news-image-20261126/leaderboard)
[![Reward](https://make.fun/badge/news-image-20261126/monicazhy949/makefun-news-1126/reward.svg)](https://make.fun/bounty/news-image-20261126)

A 1024×1024 newspaper front page summing up the world news of
**Thursday, 26 November 2026**, built from six real, sourced stories
reported that day:

1. **US proposes new tariffs on 14 countries** — Washington proposes
   tariffs on 14 nations, with 25% on Indian goods.
   (Reuters / The Hindu)
2. **Tanker fire near Cairo kills at least 30** — a fuel tanker crash
   sets off a huge fire on a highway near Cairo. (The Hindu)
3. **Kim urges wider nuclear weapons rollout** — Kim Jong Un calls for
   tactical nuclear arms to be deployed more widely. (Reuters / KCNA)
4. **Record migrant arrival in Canary Islands** — nearly 2,000 migrants
   reach the Canary Islands in a day, a record.
   (Associated Press)
5. **Chinese bomber nears Philippine coast** — a long-range bomber flies
   within 45 nautical miles of Luzon, Manila says.
   (Agence France-Presse)
6. **Thanksgiving parade postponed by storm** — New York calls off its
   Thanksgiving Day parade as a major storm hits.
   (Associated Press)

## Run it

`main.py` (Python 3.13, standard library only) copies `entry.png` to the
output directory. Outside the grader, `MAKEFUN_OUTPUT_DIR` stands in
for `/output`:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Running it twice writes identical bytes.

Revision note (26 November 2026): two decks were shortened so the full
sentence fits on the card — v1 clipped "India." and "record." off the
ends of the TRADE and MIGRATION cards. The facts are unchanged.
