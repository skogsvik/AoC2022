use crate::loaders::file_to_lines;
pub const DATA: &str = "input/aoc4";

pub type PairOfLimits = [u32; 4];

pub fn load(filename: impl AsRef<std::path::Path>) -> impl Iterator<Item = PairOfLimits> {
    file_to_lines(filename).map(|line| {
        let mut limits = line
            .split(',')
            .flat_map(|range| range.split('-').map(|n| n.parse().unwrap()));
        [
            limits.next().unwrap(), // start1
            limits.next().unwrap(), // end1
            limits.next().unwrap(), // start2
            limits.next().unwrap(), // end2
        ]
    })
}

pub fn answer1(ranges: impl Iterator<Item = PairOfLimits>) -> usize {
    ranges
        .filter(|[start1, end1, start2, end2]| {
            start1 <= start2 && end1 >= end2 || start2 <= start1 && end2 >= end1
        })
        .count()
}

pub fn answer2(ranges: impl Iterator<Item = PairOfLimits>) -> usize {
    ranges
        .filter(|[start1, end1, start2, end2]| {
            start1 <= start2 && start2 <= end1 || start2 <= start1 && start1 <= end2
        })
        .count()
}

#[cfg(test)]
mod tests {
    use super::*;

    const MOCK_DATA: [[u32; 4]; 6] = [
        [2, 4, 6, 8],
        [2, 3, 4, 5],
        [5, 7, 7, 9],
        [2, 8, 3, 7],
        [6, 6, 4, 6],
        [2, 6, 4, 8],
    ];

    #[test]
    fn test_answer1_mock_data() {
        assert_eq!(answer1(MOCK_DATA.iter().copied()), 2)
    }

    #[test]
    fn test_answer2_mock_data() {
        assert_eq!(answer2(MOCK_DATA.iter().copied()), 4)
    }

    #[test]
    fn test_answer1() {
        assert_eq!(answer1(load(DATA)), 569)
    }

    #[test]
    fn test_answer2() {
        assert_eq!(answer2(load(DATA)), 936)
    }
}
