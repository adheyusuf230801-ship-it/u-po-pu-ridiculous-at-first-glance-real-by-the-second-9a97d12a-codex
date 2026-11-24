"""Write the deterministic make.fun bounty entry."""

from pathlib import Path


SENTENCE = "Apartment developers pay us to rent robot upstairs neighbors for open houses: buyers laugh at the stomping, then pay a premium for quiet."


def main() -> None:
    output = Path("/output")
    output.mkdir(parents=True, exist_ok=True)
    (output / "entry.txt").write_text(SENTENCE, encoding="utf-8")


if __name__ == "__main__":
    main()
