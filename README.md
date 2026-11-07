# Python Projects

Two short Python programs from my coursework at Indiana University: the EKG number sequence and a tic-tac-toe blocking move.

**Status:** Finished small exercises (2024) · **Stack:** Python 3 · Written by hand in 2024; README refreshed with [Claude Code](https://claude.com/claude-code) in 2026

## What it does

This is a small collection of standalone Python scripts written while studying at the Luddy School of Informatics, Computing, and Engineering. Each file is a short, self-contained program built around one idea. They were written by hand, without Claude Code or any AI assistant.

## Programs

- **`ECGSequence.py`** builds the EKG sequence (it starts 1, 2, 4, 6, 3, 9, ...). Each new term is the smallest number not yet used that shares a factor greater than 1 with the previous term. `ecg_seq_index(n)` returns the position of `n` in the sequence (0-based).
- **`tic_tac_toe_blocker.py`** takes two board positions (0 to 8) held by a player and returns the square that completes their line, or -1 if the two squares do not share a winning line.

## How it works

```
ECGSequence.py            sequence builder with a set for fast lookups
tic_tac_toe_blocker.py    checks the 8 winning lines for the two given squares
```

Both programs use plain Python and the standard library only.

## Run it locally

Prerequisite: Python 3.

```bash
python3 ECGSequence.py            # prints the indexes of 3, 5 and 7 in the sequence
python3 tic_tac_toe_blocker.py    # defines the function; the example call is commented out
```

## Project stats

| | |
|---|---|
| Timeline | 2024-04-29 → 2024-04-29 (first to last commit) |
| Commits | 3 |
| Active Claude Code time | not measured |
| Claude tokens | not measured |

No Claude Code session transcripts mention this repo, so time and tokens are not measured.

<details>
<summary>How these numbers were measured</summary>

Measured from Claude Code session transcripts (the `.jsonl` files Claude Code writes for every session and subagent) with a small read-only script. Each Claude response's `usage` record is counted once. A response counts toward this repo when its working directory is inside the repo (or a git worktree of it); for sessions started from a general folder, when its tool calls point into the repo, or else the project that session was last working on.

- **New-work tokens** = input tokens + tokens written to the prompt cache + output tokens.
- **Cache reads** are the conversation context that Claude re-reads from Anthropic's prompt cache on every turn. They are far larger than new work and are billed at about a tenth of the input price, so they are listed separately rather than added to the total.
- **Active time** joins transcript events that are at most 15 minutes apart into working intervals, then merges overlapping intervals so parallel sessions and subagents are not double counted. Idle gaps longer than 15 minutes are not counted.

All figures are approximate.

</details>

## Notes

These programs are early work and have no tests. Time and token usage are not measured because the code predates the Claude Code sessions on record.
