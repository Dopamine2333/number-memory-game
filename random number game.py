import random
import time

def main():
    total_levels = 15
    digits = list("0123456789")

    print("🔢 Welcome to the Number Memory Game!")
    print("Repeat the sequence of numbers exactly — no spaces.")
    print("Levels 1–3: 3 seconds to answer.")
    print("Levels 4–15: 1 second per digit.\n")

    level = 1
    while level <= total_levels:
        sequence = [random.choice(digits) for _ in range(level)]
        sequence_str = ''.join(sequence)

        print(f"Level {level}")
        print("Watch carefully!")

        # Display each digit with a short delay
        for digit in sequence:
            print(digit, end='', flush=True)
            time.sleep(0.5)
        print("\n" + "-" * 30)

        # Set time limit
        time_limit = 3 if level <= 3 else level

        start_time = time.time()
        try:
            user_input = input("Enter the number sequence: ").strip()
        except:
            user_input = ""

        elapsed_time = time.time() - start_time

        if elapsed_time > time_limit:
            print(f"⏱ Too slow! You had {time_limit} seconds.")
            print("Restarting from level 1.\n")
            level = 1
            continue

        if user_input == sequence_str:
            print("✅ Correct!\n")
            level += 1
        else:
            print("❌ Wrong sequence!")
            print(f"The correct sequence was: {sequence_str}")
            print("Restarting from level 1.\n")
            level = 1

    print("🎉 Congratulations! You completed all 15 levels!")

if __name__ == "__main__":
    main()
