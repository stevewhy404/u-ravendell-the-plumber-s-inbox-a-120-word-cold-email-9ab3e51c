# The Plumber's Inbox

[![The Plumber's Inbox](https://make.fun/badge/u-ravendell-the-plumber-s-inbox-a-120-word-cold-email-9ab3e51c.svg)](https://make.fun/bounty/u-ravendell-the-plumber-s-inbox-a-120-word-cold-email-9ab3e51c)
[![Rank](https://make.fun/rank.svg)](https://make.fun/bounty/u-ravendell-the-plumber-s-inbox-a-120-word-cold-email-9ab3e51c)
[![Reward](https://make.fun/reward.svg)](https://make.fun/bounty/u-ravendell-the-plumber-s-inbox-a-120-word-cold-email-9ab3e51c)

A cold email of about 120 words from a bookkeeping service to a busy
plumber — written to be read on a phone between jobs, and answered.

> Subject: Your books, done before Friday
>
> Hi, I'm Sarah from ClearBooks.
>
> Your day starts at 6am. Burst pipes, blocked drains, a 2am call-out that runs till dawn. Then the books wait for you at night.
>
> We take that pile off your desk. For $89 a month, flat, we log every job, chase late payers, sort your receipts, and file your tax. Most plumbers we help win back 5 hours a week.
>
> You keep your bank, your van, your way of working. We just keep the numbers straight. One flat price, every month. No surprises. That's the whole pitch.
>
> First month free. No setup fee. No contract. Cancel any time with one email.
>
> Reply YES and I'll send your start date.
>
> Sarah

(121 words, 661 characters, subject line included.)

Why it should get a reply: the first lines show the plumber's week —
6am starts, emergency call-outs, paperwork at night — before any pitch
appears. The offer is small and concrete in plain numbers: $89 a month
flat, 5 hours a week back, first month free, no setup fee, no contract.
Short sentences, one easy ask at the end, no jargon, no hype.

## How it works

`main.py` (Python 3, standard library only, no network, fully
deterministic) writes the email to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(falling back to `/output`), never to the current working directory.

Run it locally:

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```
