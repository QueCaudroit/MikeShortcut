use std::io;

fn main() {
    let mut buffer = String::new();
    let mut stdin = io::stdin();
    stdin.read_line(&mut buffer)?;
    
    println!("Hello, world!");
}
