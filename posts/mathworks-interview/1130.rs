struct Solution;

use std::cmp::max;
use std::i32;

impl Solution {
    pub fn mct_from_leaf_values(arr: Vec<i32>) -> i32 {
        let mut arr = arr.clone();
        let mut res: i32 = 0;

        while arr.len() != 1 {
            let mut largestLeafValue: i32 = i32::MIN;
            let mut product: i32 = i32::MAX;
            let mut index: i32 = -1;

            for i in 0..arr.len() - 1 {
                let a = arr[i];
                let b = arr[i + 1];
                if a * b < product {
                    largestLeafValue = max(a, b);
                    product = a * b;
                    index = i as i32;
                }
            }

            arr.remove(index as usize);
            arr.remove(index as usize);
            arr.insert(index as usize, largestLeafValue);
            res = res + product;
        }

        return res;
    }
}