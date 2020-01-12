struct Solution;

use std::collections::HashMap;
use std::cmp::max;
use std::cmp::min;
use std::i32;

impl Solution {
    pub fn find_shortest_sub_array(nums: Vec<i32>) -> i32 {
        let mut counter: HashMap<i32, Vec<i32>> = HashMap::new();
        let mut maxFrequency: i32 = i32::MIN;

        for (i, v) in nums.iter().enumerate() {
            match counter.get_mut(v) {
                Some(value) => {
                    value[0] += 1;
                    value[2] = i as i32;
                    maxFrequency = max(maxFrequency, value[0]);
                }
                None => {
                    counter.insert(*v, vec![1, i as i32, i as i32]);
                    maxFrequency = max(maxFrequency, 1);
                }
            };
        }

        let mut res: i32 = i32::MAX;

        for (k, v) in counter.iter() {
            if v[0] == maxFrequency {
                res = min(res, v[2] - v[1] + 1);
            }
        }
        
        return res;
    }
}