pub use crate::loaders::file_to_lines as load;
pub const DATA: &str = "input/aoc2";

const WIN: u32 = 6;
const DRAW: u32 = 3;

const LOSE: u32 = 0;
const ROCK: u32 = 1;
const PAPER: u32 = 2;
const SCISSORS: u32 = 3;

pub fn answer1<I>(rounds: I) -> u32
where
    I: Iterator,
    I::Item: AsRef<str>,
{
    rounds
        .map(|round| match round.as_ref() {
            "A X" => ROCK + DRAW,
            "B X" => ROCK + LOSE,
            "C X" => ROCK + WIN,
            "A Y" => PAPER + WIN,
            "B Y" => PAPER + DRAW,
            "C Y" => PAPER + LOSE,
            "A Z" => SCISSORS + LOSE,
            "B Z" => SCISSORS + WIN,
            "C Z" => SCISSORS + DRAW,
            _ => unreachable!("All game cases should be covered"),
        })
        .sum()
}

pub fn answer2<I>(rounds: I) -> u32
where
    I: Iterator,
    I::Item: AsRef<str>,
{
    rounds
        .map(|round| match round.as_ref() {
            "A X" => LOSE + SCISSORS,
            "B X" => LOSE + ROCK,
            "C X" => LOSE + PAPER,
            "A Y" => DRAW + ROCK,
            "B Y" => DRAW + PAPER,
            "C Y" => DRAW + SCISSORS,
            "A Z" => WIN + PAPER,
            "B Z" => WIN + SCISSORS,
            "C Z" => WIN + ROCK,
            _ => unreachable!("All game cases should be covered"),
        })
        .sum()
}

#[cfg(test)]
mod tests {
    use super::*;

    const MOCK_DATA: &str = "A Y\nB X\nC Z\n";

    #[test]
    fn test_answer1_mock_data() {
        assert_eq!(answer1(MOCK_DATA.lines()), 15)
    }

    #[test]
    fn test_answer2_mock_data() {
        assert_eq!(answer2(MOCK_DATA.lines()), 12)
    }

    #[test]
    fn test_answer1() {
        assert_eq!(answer1(load(DATA)), 11841)
    }

    #[test]
    fn test_answer2() {
        assert_eq!(answer2(load(DATA)), 13022)
    }
}
