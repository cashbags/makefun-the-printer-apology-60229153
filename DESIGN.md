# DESIGN — The Printer Apology

## The entry

> Sorry I need cyan to print black. I am not broken, I am holding your black ink hostage for a friend.

100 characters, 100 bytes, plain ASCII, one line, no trailing newline.

## Why this line

Built to win the judge's five criteria in order. (1) Genuinely an apology
from a printer to its office, with the printer's own gripe in it: it opens
"Sorry", and the gripe is its own — it is forced to demand cyan for a
black page, and it resents the office for it. (2) A real joke, punch at the
end: the printer is not broken, it is running a hostage negotiation, and it
has an accomplice — "for a friend" turns a malfunction into a conspiracy.
(3) Printer truth: every office has watched a printer refuse a black page
for want of cyan. (4) Freshness: the cyan ransom is an empty lane, not the
field's flooded jokes — jam apologies, 40x/47x copies, cheap paper, toner
warnings, eating the report. (5) Economy: 100 chars, one idea, nothing
tacked on.

## The empty lane

The field (423 submissions at detection) floods the jam
lane ("Sorry I jammed" in many variants), the copies lane (salary
spreadsheet 40x, 47 copies of one page), cheap paper, toner warnings, and
eating the report. The cyan ransom is a different grievance: not a failure
of the machine but a demand it makes — the printer as a small-time
extortionist with a friend in on it.

## The tournament

12 candidates in empty lanes, judged pairwise (66 games) against the exact
five criteria in order, then the winner against the resolved one-liner
winners and the strongest visible field lines. This line went 11-0
internally and 7-0 against the references. Full table: CANDIDATES.md.
Runner-up: "Sorry I read your resignation letter. I printed it twice: once
for you, once for the gossip in tray two." — lost only on criterion 2.
Third: "Sorry I said I was out of paper. The tray was full. I just wanted
one quiet afternoon."

## The program

`main.py`: one constant, gate guards mirroring the competition gate (1-120
chars under both the code-point and byte readings, not only whitespace,
exactly one line), written with no trailing newline. No judge-addressed
text, no flooded-lane image: the joke is the printer's own confession, and
the turn carries it. No input, no clock, no randomness, no network.
