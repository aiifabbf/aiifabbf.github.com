struct Solution;

use std::collections::VecDeque;
use std::f64;

impl Solution {
    pub fn verify_preorder(preorder: Vec<i32>) -> bool {
        let mut stack: VecDeque<(f64, f64)> = vec![(-f64::INFINITY, f64::INFINITY)].iter().cloned().collect();

        for v in preorder.iter() {

            while !stack.is_empty() && stack.back().unwrap().1 < (*v as f64) {
                stack.pop_back();
            }

            if !stack.is_empty() && stack.back().unwrap().0 < (*v as f64) && (*v as f64) < stack.back().unwrap().1 {
                let interval: (f64, f64) = stack.pop_back().unwrap();
                stack.push_back((*v as f64, interval.1));
                stack.push_back((interval.0, (*v as f64)));
            } else {
                return false;
            }
        }

        return true;
    }
}