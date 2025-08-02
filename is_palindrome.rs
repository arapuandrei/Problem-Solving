impl Solution {
    pub fn is_palindrome(xu: i32) -> bool {
        let mut copy = xu.clone();
        let mut new_number = 0;
        let mut x = xu.clone();
        while x>0 {
            new_number = new_number*10 + x%10;
            x=x/10;
        }
        return copy == new_number;
    }
}