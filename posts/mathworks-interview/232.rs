use std::collections::VecDeque;

struct MyQueue {
    stack: VecDeque<i32>,
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MyQueue {

    /** Initialize your data structure here. */
    fn new() -> Self {
        return MyQueue {
            stack: VecDeque::new(),
        };
    }
    
    /** Push element x to the back of queue. */
    fn push(&self, x: i32) {
        self.stack.push_back(x);
    }
    
    /** Removes the element from in front of queue and returns that element. */
    fn pop(&self) -> i32 {
        let mut queue: VecDeque<i32> = VecDeque::new();

        while !self.stack.is_empty() {
            queue.push_back(self.stack.pop_back().unwrap());
        }

        let res: i32 = queue.pop_back().unwrap();

        while !queue.is_empty() {
            self.stack.push_back(queue.pop_back().unwrap());
        }

        return res;
    }
    
    /** Get the front element. */
    fn peek(&self) -> i32 {
        let mut queue: VecDeque<i32> = VecDeque::new();

        while !self.stack.is_empty() {
            queue.push_back(self.stack.pop_back().unwrap());
        }

        let res: i32 = queue.pop_back().unwrap();
        queue.push_back(res);

        while !queue.is_empty() {
            self.stack.push_back(queue.pop_back().unwrap());
        }

        return res
    }
    
    /** Returns whether the queue is empty. */
    fn empty(&self) -> bool {
        return self.stack.is_empty();
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * let obj = MyQueue::new();
 * obj.push(x);
 * let ret_2: i32 = obj.pop();
 * let ret_3: i32 = obj.peek();
 * let ret_4: bool = obj.empty();
 */