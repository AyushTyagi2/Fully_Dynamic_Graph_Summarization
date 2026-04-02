import argparse
import json
from pathlib import Path

from backend.model import ProdigyRunner


def run_Prodigy(args):
    """Train Prodigy and serialize a structured summary payload."""
    executer = ProdigyRunner(args)
    executer.fit()
    result = executer.encode()

    backend_root = Path(__file__).resolve().parent
    output_dir = backend_root / "dataset" / args.dataset
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "output.json"
    with output_path.open('w', encoding='utf-8') as outfile:
        json.dump(result, outfile, indent=2)

    print(f"Prodigy artifacts written to {output_path.resolve()}")
    return result


def parse_args():
    parser = argparse.ArgumentParser(description="Run Prodigy.")
    parser.add_argument("--dataset", nargs="?", default="in-2004", help="Dataset name")
    parser.add_argument("--counts", type=int, default=20)
    parser.add_argument("--group_size", type=int, default=2000)
    parser.add_argument("--hidden_size1", type=int, default=32)
    parser.add_argument("--hidden_size2", type=int, default=16)
    parser.add_argument("--lr", type=float, default=0.0005)
    parser.add_argument("--dropout", type=float, default=0.0)
    parser.add_argument("--weight-decay", type=float, default=0.0)
    parser.add_argument("--bad_counter", type=int, default=1)
    return parser.parse_args()


def main():
    args = parse_args()
    run_Prodigy(args)


if __name__ == "__main__":
    main()
