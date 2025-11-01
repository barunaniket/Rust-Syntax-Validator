fn main() {
    let x;
    let mut y;
    let x = 42;
    let mut y = 3.14;
    
    if x > 0 {
        println!("Positive");
    } else {
        println!("Not positive");
    }
    
    let mut counter = 0;
    while counter < 5 {
        counter = counter + 1;
    }
    
    for i in numbers {
        println!("{}", i);
    }
}

fn calculate(a: i32, b: i32) -> i32 {
    a + b
}

struct Point {
    x: i32,
    y: i32,
}

impl Point {
    fn new(x: i32, y: i32) -> Point {
        Point { x, y }
    }
}