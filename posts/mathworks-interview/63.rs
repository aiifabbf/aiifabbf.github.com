struct Solution;

use std::collections::HashMap;

impl Solution {
    pub fn unique_paths_with_obstacles(obstacle_grid: Vec<Vec<i32>>) -> i32 {
        let rowCount: usize = obstacle_grid.len();
        let columnCount: usize = obstacle_grid[0].len();
        if obstacle_grid[0][0] == 1 || obstacle_grid[rowCount - 1][columnCount - 1] == 1 {
            return 0;
        }

        let mut dp: HashMap<(usize, usize), i32> = HashMap::new();

        dp.insert((0, 0), 1);

        for columnIndex in 1..columnCount {
            if obstacle_grid[0][columnIndex] == 0 {
                dp.insert((0, columnIndex), *dp.get(&(0, columnIndex - 1)).unwrap());
            } else {
                dp.insert((0, columnIndex), 0);
            }
        }

        for rowIndex in 1..rowCount {
            if obstacle_grid[rowIndex][0] == 0 {
                dp.insert((rowIndex, 0), *dp.get(&(rowIndex - 1, 0)).unwrap());
            } else {
                dp.insert((rowIndex, 0), 0);
            }
        }

        for (rowIndex, row) in obstacle_grid.iter().enumerate().skip(1) {

            for (columnIndex, value) in row.iter().enumerate().skip(1) {
                if *value == 0 {
                    dp.insert((rowIndex, columnIndex), *dp.get(&(rowIndex - 1, columnIndex)).unwrap() + *dp.get(&(rowIndex, columnIndex - 1)).unwrap());
                } else {
                    dp.insert((rowIndex, columnIndex), 0);
                }
            }

        }

        return *dp.get(&(rowCount - 1, columnCount - 1)).unwrap()
    }
}