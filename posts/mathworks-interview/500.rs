struct Solution;

use std::collections::HashMap;
use std::collections::HashSet;

impl Solution {
    pub fn find_words(words: Vec<String>) -> Vec<String> {
        let mut charRowMapping: HashMap<char, i32> = HashMap::new();
        charRowMapping.extend("qwertyuiop".chars().map(|v| (v, 0)));
        charRowMapping.extend("asdfghjkl".chars().map(|v| (v, 1)));
        charRowMapping.extend("zxcvbnm".chars().map(|v| (v, 2)));

        let mut res: Vec<String> = vec![];

        for word in words.iter() {
            let rows: HashSet<i32> = word.to_lowercase().chars().map(|v| *charRowMapping.get(&v).unwrap()).collect();
            if rows.len() == 1 {
                res.push(word.clone());
            }
        }

        return res;
    }
}