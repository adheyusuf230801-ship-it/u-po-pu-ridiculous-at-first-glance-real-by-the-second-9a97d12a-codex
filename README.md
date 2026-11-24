# Robot Upstairs Neighbors

An entry for the make.fun bounty **Ridiculous at First Glance, Real by the Second**.
Apartment developers pay to rent noisy robot neighbors for open houses, where
buyers hear the value of soundproofing firsthand.

## Run

Requires Python 3.13 and its standard library only:

```sh
python3 main.py
```

The program creates `/output` if needed and writes this fixed sentence to
`/output/entry.txt` as UTF-8, without a trailing newline:

> Apartment developers pay us to rent robot upstairs neighbors for open houses: buyers laugh at the stomping, then pay a premium for quiet.

**Character count: 137 (limit: 200).** The program uses no randomness, network,
wall clock, or input files.

## Candidate selection

Scores are out of 5, in judge priority order: absurd but viable business,
originality, payment logic, sentence/pitch quality, and concrete detail.

| Candidate sentence | Characters | Scores | Assessment |
| --- | ---: | --- | --- |
| Apartment developers pay us to rent robot upstairs neighbors for open houses: buyers laugh at the stomping, then pay a premium for quiet. | 137 | 5/5/5/5/5 | Winner: developers clearly pay for the demonstration, and buyers convert the joke into a premium purchase. |
| We rent robot upstairs neighbors to developers, who pay us to stomp through model units; buyers laugh, then gladly pay extra for real soundproofing. | 148 | 5/4/5/5/5 | Clear transaction and punchline, though “real soundproofing” feels slightly explanatory. |
| Developers pay us to install robot upstairs neighbors in model apartments: buyers laugh at the noise, then pay more for the quiet. | 130 | 4/4/5/5/4 | Strong buyer turn, but installing the robots makes the service less obviously temporary and novel. |

## Verification

Run the program twice, deleting `/output/entry.txt` between runs, and compare
the resulting bytes. Both runs must produce the same 137-byte ASCII sentence
(also 137 Unicode characters), with no trailing newline.

Licensed under the MIT License; see LICENSE.
