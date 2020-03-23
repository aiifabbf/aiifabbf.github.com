struct Solution;

impl Solution {
    pub fn convert(s: String, num_rows: i32) -> String {
        let queue = s.chars();
        let mut rows: Vec<Vec<char>> = vec![vec![]; num_rows as usize];

        for (i, v) in (0..num_rows as usize)
            .chain((1..num_rows as usize - 1).rev())
            .cycle()
            .zip(queue)
        {
            rows[i].push(v);
        }

        return rows
            .iter()
            .map(|v| v.iter().collect::<String>())
            .collect::<Vec<String>>()
            .join("");
    }
}

pub fn main() {
    println!("{:?}", Solution::convert("PAYPALISHIREING".to_string(), 3));
}
