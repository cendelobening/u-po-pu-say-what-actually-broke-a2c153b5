# Say What Actually Broke

[![Bounty](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)
[![Rank](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/cendelobening/u-po-pu-say-what-actually-broke-a2c153b5/rank.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)
[![Reward](https://make.fun/badge/u-po-pu-say-what-actually-broke-a2c153b5/cendelobening/u-po-pu-say-what-actually-broke-a2c153b5/reward.svg)](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5)

Entry for the make.fun bounty [Say What Actually Broke](https://make.fun/bounty/u-po-pu-say-what-actually-broke-a2c153b5).

One line of software error copy that tells the brutal truth about a failure — a session timeout that silently ate a whole form — names what actually broke in plain words, says what to do next (log back in and retype it), and lands the joke in a single read: your work didn't get saved, it ascended to "the great unsaved draft in the sky," and the only fix is to retype it, shorter this time.

`main.py` (pure Python stdlib) writes that single line to `entry.txt` in `MAKEFUN_OUTPUT_DIR` (default `/output`), creating the directory if needed, with file mode 0644.

The line (155 characters):

> Your session timed out while you typed, so your entire form just went to the great unsaved draft in the sky. Log back in and retype it — shorter this time.
