struct Solution;

use std::collections::HashMap;

impl Solution {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        let mut res: HashMap<String, Vec<String>> = HashMap::new();

        for v in strs {
            let chars: Vec<char> = v.chars().collect();
            chars.sort();
            let root: String = chars.join("");

            match res.get(&root) {
                Some(array) => {
                    array.push(v.clone());
                },
                None => {
                    res.insert(root, vec![v.clone()]);
                }
            }
        }

        return res.values().cloned().collect::<Vec<String>>();
    }
}