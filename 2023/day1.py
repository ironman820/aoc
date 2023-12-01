# --- Day 1: Trebuchet?! ---
# Something is wrong with global snow production, and you've been selected to
# take a look. The Elves have even given you a map; on it, they've used stars
# to mark the top fifty locations that are likely to be having problems.
#
# You've been doing this long enough to know that to restore snow operations,
# you need to check all fifty stars by December 25th.
#
# Collect stars by solving puzzles. Two puzzles will be made available on each
# day in the Advent calendar; the second puzzle is unlocked when you complete
# the first. Each puzzle grants one star. Good luck!
#
# You try to ask why they can't just use a weather machine ("not powerful
# enough") and where they're even sending you ("the sky") and why your map
# looks mostly blank ("you sure ask a lot of questions") and hang on did you
# just say the sky ("of course, where do you think snow comes from") when you
# realize that the Elves are already loading you into a trebuchet ("please
# hold still, we need to strap you in").
#
# As they're making the final adjustments, they discover that their
# calibration document (your puzzle input) has been amended by a very young
# Elf who was apparently just excited to show off her art skills. Consequently,
# the Elves are having trouble reading the values on the document.
#
# The newly-improved calibration document consists of lines of text; each line
# originally contained a specific calibration value that the Elves now need to
# recover. On each line, the calibration value can be found by combining the
# first digit and the last digit (in that order) to form a single two-digit
# number.
#
# For example:
#
# 1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet
# In this example, the calibration values of these four lines are 12, 38, 15,
# and 77. Adding these together produces 142.
#
# Consider your entire calibration document. What is the sum of all of the
# calibration values?


def calibrate():
    calibration_sum: int = 0
    with open("day1-input.txt", "r") as file:
        lines: list[str] = file.readlines()
    for code in lines:
        value = get_value(code)
        calibration_sum = calibration_sum + value
    print(f"The sum of all of the calibration values is: {calibration_sum}.")

    # --- Part Two ---
    # Your calculation isn't quite right. It looks like some of the digits are
    # actually spelled out with letters: one, two, three, four, five, six,
    # seven, eight, and nine also count as valid "digits".
    #
    # Equipped with this new information, you now need to find the real first
    # and last digit on each line. For example:
    #
    # two1nine
    # eightwothree
    # abcone2threexyz
    # xtwone3four
    # 4nineeightseven2
    # zoneight234
    # 7pqrstsixteen
    # In this example, the calibration values are 29, 83, 13, 24, 42, 14, and
    #  76. Adding these together produces 281.
    #
    # What is the sum of all of the calibration values?

    digits: dict[str, int] = {
        "one": 1,
        "two": 2,
        "six": 6,
        "four": 4,
        "five": 5,
        "nine": 9,
        "three": 3,
        "seven": 7,
        "eight": 8,
    }
    calibration_sum = 0
    for code in lines:
        code = code[:-1]  # 19qdlpmdrxone7sevennine
        for location in range(
            len(code) - 1
        ):  # 19qdlpmdrxone7sevennine - len = 23 - len-1 = 22 - range = 21
            for key, value in digits.items():
                length = len(key)  # len("one") = 3
                end = location + length - 1  # 21+3-1=23
                print(
                    f"location: {location}\ncode: {code}\ncode[:location]: {code[:location]}\nvalue: {value}\ncode[end + 1:]: {code[end + 1:]}"
                )
                if end > len(code):  # 23 > 23
                    continue
                if key != code[location:end]:  # code[21:23] - ine
                    continue
                code = (
                    code[:location] + str(value) + code[end + 1 :]
                )  # loc=19, end=23, value=nine, code[:loc]=19qdlpmdrxone7sevennine
        # for length in [3, 4, 5]:
        #     for location in range(len(code) - length):
        #         for key, value in digits.items():
        #             if len(key) > length:
        #                 continue
        #             if key != code[location : (location + length - 1)]:
        #                 continue
        #             code = code[:location] + str(value) + code[location + 1 :]
        value = get_value(code)
        calibration_sum = calibration_sum + value
    print(f"The true sum of all calibration values is: {calibration_sum}.")


def get_value(code: str) -> int:
    locs = [pos for pos, char in enumerate(code) if char in "123456789"]
    return int(f"{code[locs[0]]}{code[locs[-1]]}")


if __name__ == "__main__":
    calibrate()
