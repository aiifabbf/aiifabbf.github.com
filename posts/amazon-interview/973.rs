pub struct Solution;

impl Solution {
    pub fn k_closest(points: Vec<Vec<i32>>, k: i32) -> Vec<Vec<i32>> {
        let mut points: Vec<Vec<i32>> = points.iter().cloned().collect();
        points.sort_by_key(|v: Vec<i32>| {
            v[0].pow(2) + v[1].pow(2)
        });
        return points[..k as usize].to_vec();
    }
}