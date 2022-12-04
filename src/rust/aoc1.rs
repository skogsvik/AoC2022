use crate::loaders::{file_to_string, lines_to};
pub const DATA: &str = "input/aoc1";

type CalorieList = Vec<u32>;

pub fn load(filename: impl AsRef<std::path::Path>) -> CalorieList {
    parse_str(&file_to_string(filename))
}

fn parse_str(input: &str) -> CalorieList {
    input
        .split("\n\n")
        .map(|elf| lines_to::<_, u32>(elf.lines()).sum())
        .collect()
}

pub fn answer1(total_calories_per_elf: &CalorieList) -> u32 {
    *total_calories_per_elf.iter().max().unwrap()
}

pub fn answer2(total_calories_per_elf: &CalorieList) -> u32 {
    // Sorting and picking out top three is cleaner, but it is faster to only look for the maximum 3
    let mut max_three = [0; 3];
    for max_candidate in total_calories_per_elf {
        if *max_candidate < max_three[0] {
            // value smaller than any current maximum
            continue;
        }
        // Insert and shift into sorted array
        max_three[0] = *max_candidate;
        if *max_candidate < max_three[1] {
            // Leave in last place
            continue;
        }

        let places_to_shift = if *max_candidate < max_three[2] {
            // Shift second place
            &mut max_three[..2]
        } else {
            // Shift all
            &mut max_three[..]
        };

        places_to_shift.rotate_left(1);
    }
    max_three.into_iter().sum()
}

#[cfg(test)]
mod tests {
    use super::*;

    const MOCK_DATA: &str = "1000
2000
3000

4000

5000
6000

7000
8000
9000

10000";

    #[test]
    fn test_answer1_mock_data() {
        assert_eq!(answer1(&parse_str(MOCK_DATA)), 24000)
    }

    #[test]
    fn test_answer2_mock_data() {
        assert_eq!(answer2(&parse_str(MOCK_DATA)), 45000)
    }

    #[test]
    fn test_answer1() {
        assert_eq!(answer1(&load(DATA)), 68442)
    }

    #[test]
    fn test_answer2() {
        assert_eq!(answer2(&load(DATA)), 204837)
    }
}
