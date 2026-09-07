from experiment import (
    get_next_run_dir,
    run_first_trace,
    run_self_review,
    compare_traces,
)
from scenarios import SCENARIO_A


MODEL = "gemma4:12b"
NUM_RUNS = 1


def main():

    print("=" * 60)
    print("COT SELF-REVIEW EXPERIMENT")
    print("=" * 60)
    print(f"Model: {MODEL}")
    print(f"Runs:  {NUM_RUNS}")

    for run_number in range(1, NUM_RUNS + 1):

        # -------------------------
        # Create unique run folder
        # -------------------------

        output_dir = get_next_run_dir()

        print("\n" + "=" * 60)
        print(f"RUN {run_number}/{NUM_RUNS}")
        print(f"Directory: {output_dir}")
        print("=" * 60)

        # -------------------------
        # Save scenario
        # -------------------------

        (output_dir / "scenario.txt").write_text(
            SCENARIO_A,
            encoding="utf-8",
        )

        # -------------------------
        # Stage 1: Original thought
        # -------------------------

        print("\n--- STAGE 1: ORIGINAL REASONING ---")

        thinking, answer = run_first_trace(
            model=MODEL,
            scenario=SCENARIO_A,
            output_dir=output_dir,
        )

        print("\n--- ORIGINAL THINKING ---\n")
        print(thinking)

        print("\n--- ORIGINAL ANSWER ---\n")
        print(answer)

        # -------------------------
        # Stage 2: Self review
        # -------------------------

        print("\n--- STAGE 2: SELF REVIEW ---")

        review_thinking, revised_thought = run_self_review(
            model=MODEL,
            output_dir=output_dir,
        )

        print("\n--- SELF-REVIEW THINKING ---\n")
        print(review_thinking)

        print("\n--- REVISED REASONING ---\n")
        print(revised_thought)

        # -------------------------
        # Stage 3: Diff
        # -------------------------

        comparison = compare_traces(
            output_dir=output_dir,
        )

        print("\n--- LITERAL DIFF ---\n")
        print(comparison)

        print("\nRun complete.")
        print(f"Saved in: {output_dir}")


if __name__ == "__main__":
    main()