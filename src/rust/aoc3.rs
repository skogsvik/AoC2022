pub use crate::loaders::file_to_lines as load;
use itertools::Itertools;
use std::collections::HashSet;

pub const DATA: &str = "input/aoc3";

fn score(common_type: &char) -> u32 {
    match common_type {
        'a'..='z' => *common_type as u32 - 'a' as u32 + 1,
        'A'..='Z' => *common_type as u32 - 'A' as u32 + 27,
        _ => unreachable!("All types are in the ranges A..=Z or A..=z"),
    }
}

pub fn answer1<I>(rucksacks: I) -> u32
where
    I: Iterator,
    I::Item: AsRef<str>,
{
    rucksacks
        .map(|rucksack| {
            let rucksack = rucksack.as_ref();
            let (left, right) = rucksack.split_at(rucksack.len() / 2);
            let left: HashSet<_> = left.chars().collect();
            let right: HashSet<_> = right.chars().collect();
            let common = left.intersection(&right).exactly_one().unwrap();
            score(common)
        })
        .sum()
}

pub fn answer2<I>(rucksacks: I) -> u32
where
    I: Iterator,
    I::Item: AsRef<str>,
{
    rucksacks
        .chunks(3)
        .into_iter()
        .map(|rucksacks| {
            let mut rucksacks = rucksacks.map(|rucksack| rucksack.as_ref().chars().collect());
            let first = rucksacks.by_ref().next().unwrap();
            let others: Vec<HashSet<_>> = rucksacks.collect();
            let common = first
                .iter()
                .filter(|c| others.iter().all(|other| other.contains(c)))
                .exactly_one()
                .unwrap();
            score(common)
        })
        .sum()
}

#[cfg(test)]
mod tests {
    use super::*;

    const MOCK_DATA: [&str; 6] = [
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw",
    ];

    #[test]
    fn test_answer1_mock_data() {
        assert_eq!(answer1(MOCK_DATA.iter()), 157)
    }

    #[test]
    fn test_answer2_mock_data() {
        assert_eq!(answer2(MOCK_DATA.iter()), 70)
    }

    #[test]
    fn test_answer1() {
        assert_eq!(answer1(load(DATA)), 8123)
    }

    #[test]
    fn test_answer2() {
        assert_eq!(answer2(load(DATA)), 2620)
    }
}
