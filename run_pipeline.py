from src.generate_brief import generate_brief


def main() -> None:
    print("Running Executive Signal Synthesis pipeline...")
    generate_brief()
    print("Pipeline completed.")


if __name__ == "__main__":
    main()