use std::{fmt::Debug, fs::File, io::prelude::*, path::Path, str::FromStr};

pub fn file_to_string(filename: impl AsRef<Path>) -> String {
    let mut content = String::new();
    File::open(filename)
        .expect("No such file")
        .read_to_string(&mut content)
        .expect("Unablet to read UTF-8 data");
    content
}

#[inline]
pub fn lines_to<I, T>(lines: I) -> impl Iterator<Item = T>
where
    I: Iterator,
    I::Item: AsRef<str>,
    T: FromStr,
    T::Err: Debug,
{
    lines.map(|l| l.as_ref().parse::<T>().expect("Failed to parse line"))
}
