impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        // Pair each number with its original index
        let mut nums_with_index: Vec<(i32, usize)> = nums.iter().cloned().zip(0..).collect();

        // Sort the array based on the number values
        nums_with_index.sort_by_key(|k| k.0);

        let mut f = 0;
        let mut l = nums_with_index.len() - 1;

        while f < l {
            let sum = nums_with_index[f].0 + nums_with_index[l].0;
            if sum < target {
                f += 1;
            } else if sum > target {
                l -= 1;
            } else {
                // Return the original indices
                return vec![nums_with_index[f].1 as i32, nums_with_index[l].1 as i32];
            }
        }

        vec![]
    }
}
