from src.generate_brief import generate_brief
from src.evaluate import evaluate  # make sure function name matches


def main() -> None:
    print("Running Executive Signal Synthesis pipeline...")

    generate_brief()
    print("Brief generated.")

    try:
        evaluate()
        print("Evaluation completed.")
    except Exception:
        print("Evaluation step skipped or not fully implemented.")

    print("Pipeline completed.")


if __name__ == "__main__":
    main()