# Python Projects: features

Two short, standalone Python programs written in April 2024 during coursework. `ECGSequence.py` finds the position
of a number in the EKG sequence. `tic_tac_toe_blocker.py` returns the square that blocks a two-in-a-row in
tic-tac-toe. They are early learning exercises, kept public as a record, and this file describes them at that size.

**This is the source-of-truth features list.** Every PR that adds, changes, removes or switches off something a person
can see or use updates this file in the same PR (see "Keeping this file true").

- **Repo:** AlexRosen23/Python-Projects (public) · **Folder:** none (no local folder; edited through fresh clones)
- **Status:** Finished small exercises, no further work planned · **Version:** none · **`main`:** `a4ea858` (2026-11-15)
- **Last updated:** 2026-11-15, written from the code, README and git history.

**Status words** (a feature with no status word is live):
| Word | Means |
| --- | --- |
| *Live* | on `main` and works when run |
| *Planned* | named in the README's "what's next" list, not built |

## At a glance
| | |
| --- | --- |
| Stack | Python 3, standard library only (checked by the README with 3.9.6) |
| Code | 2 files, 45 and 44 lines (89 total) |
| Dependencies | none |
| Tests / CI | none; no workflow files |
| Merged PRs | 4 (all README, `.gitignore` or docs changes) |
| Commits | 8 on `main` |

## Contents
1. What it is and who it's for
2. How to run it
3. Architecture at a glance
4. Features
5. Integrations
6. Data and privacy
7. Tests and evidence
8. Known limits and gaps
9. Change log

## 1. What it is and who it's for

- Two small exercises in turning a precise rule into code.
- For readers who want to see where the owner's Python started. Not a library or a tool.

## 2. How to run it

Requirements: Python 3. Nothing to install.

```bash
git clone https://github.com/AlexRosen23/Python-Projects.git
cd Python-Projects
python3 ECGSequence.py
python3 -c "from tic_tac_toe_blocker import tic_tac_toe_blocker as b; print(b(0, 1))"
```

- `python3 ECGSequence.py` prints `4`, `9`, `13` (the examples sit under a `__main__` guard, so importing it prints nothing).
- `python3 tic_tac_toe_blocker.py` prints nothing: it only defines the function; its example is a comment.
- Environment variables, ports, launch config: none.

## 3. Architecture at a glance

| Path | What it is |
| --- | --- |
| `ECGSequence.py` | EKG sequence index finder |
| `tic_tac_toe_blocker.py` | tic-tac-toe blocking move |
| `README.md` | overview, how it was verified, limits |
| `FEATURES.md` | this feature list |
| `.gitignore` | keeps `__pycache__/`, `*.pyc`, `.venv/`, `venv/` and `.DS_Store` out of git |

The two files are independent. Neither imports the other.

## 4. Features

### EKG sequence (`ECGSequence.py`)
- **`ecg_seq_index(n)`**: returns the 0-based position of `n` in the EKG sequence (OEIS A064413). The sequence starts 1, 2, then each next term is the smallest unused positive integer that shares a factor greater than 1 with the previous term. `ECGSequence.py`
- **Generate only as far as needed**: the function extends the sequence until `n` appears, then stops. `ECGSequence.py`
- **Shared-factor check**: an inner helper tests two numbers by trial division from 2 up to the smaller one. `ECGSequence.py`
- **Fast set lookup**: a set of used numbers makes the "already used?" test constant-time; a list keeps the order for the final `index` call. `ECGSequence.py`
- **Input check**: `n < 1` raises `ValueError` instead of looping forever. `ECGSequence.py`
- **Built-in examples**: three calls at the bottom, under a `__main__` guard, print the positions of 3, 5 and 7 (expected `4`, `9`, `13`). `ECGSequence.py`

### Tic-tac-toe blocker (`tic_tac_toe_blocker.py`)
- **`tic_tac_toe_blocker(pos1, pos2)`**: takes two squares (0 to 8, numbered row by row) held by one player and returns the third square of the line that contains both. `tic_tac_toe_blocker.py`
- **Rule as data**: the 8 winning lines (3 rows, 3 columns, 2 diagonals) are a list; the function returns the remaining square of the first line holding both. `tic_tac_toe_blocker.py`
- **No-block answer**: returns `-1` when no line holds both squares, or when the squares are equal or outside 0 to 8. `tic_tac_toe_blocker.py`
- **Documented**: a docstring explains the parameters, the return value and the board numbering. `tic_tac_toe_blocker.py`

### Not built
- **Type checks** *(Planned, only "if revisited")*: neither function checks argument types.
- **Tests** *(Planned, only "if revisited")*: a few `pytest` cases from OEIS A064413.

## 5. Integrations

- Reference only: the EKG sequence definition at OEIS A064413 (oeis.org). No network calls from the code.
- No other repos, services or tools.

## 6. Data and privacy

- No data stored, read or sent. Both programs compute from their arguments.
- No secrets, accounts or personal data.

## 7. Tests and evidence

- No test suite. Counted from source on 2026-11-15, not run.
- Recorded evidence in `README.md` (2026-11-09, Python 3.9.6, macOS): `python3 ECGSequence.py` printed `4`, `9`, `13`; the first 20 positions matched OEIS A064413 (throwaway script, not committed); the blocker returned `(0,1)→2`, `(1,0)→2`, `(2,4)→6`, `(0,5)→-1`.
- Timing recorded there: finding 97 (position 181) takes about 0.01 s.
- No GitHub Actions workflows.

## 8. Known limits and gaps

- The blocker only handles one pair of squares; it does not look at the whole board or at which squares are already taken.
- The shared-factor test is quadratic-ish; fine for small `n`.
- No license file, so default copyright applies.

## 9. Change log

| Date | PR | Change |
| --- | --- | --- |
| 2026-11-18 | this PR | `ecg_seq_index` rejects `n < 1`; the blocker returns `-1` for bad squares; `__main__` guard on the examples; README map and counts refreshed. |
| 2026-11-15 | #4 | Added this file. |
| 2026-11-10 | #3 | README links the merged PR; added `.gitignore` for Python caches and virtual environments. |
| 2026-11-10 | #2 | Full README write-up (why, what works, verified limits). |
| 2026-11-07 | #1 | Professional README (overview, stack, run steps, build stats). |
| 2024-04-29 | none | `tic_tac_toe_blocker.py`, a first README, and `ECGSequence.py` (the original commits). |

## Keeping this file true

- **Same PR, same change:** a PR that changes a function, its output or the files here updates this file too.
- **Status moves with reality:** if a type check or test is added, move it out of "Not built".
- **Only what is true:** re-check the behaviour claims by running the examples before editing them.
- **Public repo rule:** this file is public. No private details, no secrets, no machine paths.
