use std::io;

fn main() {
    let (n_intersections, shortcuts) = get_input();
    let shortest_paths = get_shortest_paths(n_intersections, shortcuts);
    output_result(shortest_paths);
}

fn get_input() -> (usize, Vec<usize>) {
    let mut buffer = String::new();
    let stdin = io::stdin();
    stdin.read_line(&mut buffer).unwrap();
    let n_intersections = buffer.lines().next().unwrap().parse::<usize>().unwrap();
    buffer.clear();
    stdin.read_line(&mut buffer).unwrap();
    let shortcuts = buffer.lines().next().unwrap().split(" ").map(|s| s.parse::<usize>().unwrap() - 1).collect();
    return (n_intersections, shortcuts)
}

fn output_result(shortest_paths: Vec<usize>) {
    let mut result = String::new();
    for path in shortest_paths {
        result.push_str(&path.to_string());
        result.push_str(" ");
    }
    result.pop();
    println!("{}", result);
}

fn get_shortest_paths(n_intersections: usize, shortcuts: Vec<usize>) -> Vec<usize> {
    let mut shortest_paths = vec![usize::MAX; n_intersections];
    shortest_paths[0] = 0;
    let mut places_to_check = vec![0];
    let mut shortest_path_count = 1;
    while shortest_path_count < n_intersections {
        if let Some(place_to_check) = places_to_check.pop(){
            if place_to_check > 1 && shortest_paths[place_to_check - 1] == usize::MAX {
                shortest_paths[place_to_check - 1] = shortest_paths[place_to_check] + 1;
                places_to_check.insert(0, place_to_check - 1);
                shortest_path_count += 1;
            }
            if place_to_check < n_intersections - 1 && shortest_paths[place_to_check + 1] == usize::MAX {
                shortest_paths[place_to_check + 1] = shortest_paths[place_to_check] + 1;
                places_to_check.insert(0, place_to_check + 1);
                shortest_path_count += 1;
            }
            if shortest_paths[shortcuts[place_to_check]] == usize::MAX {
                shortest_paths[shortcuts[place_to_check]] = shortest_paths[place_to_check] + 1;
                places_to_check.insert(0, shortcuts[place_to_check]);
                shortest_path_count += 1;
            }
        } else {
            panic!("no place to optimize form");
        }
    }
    return shortest_paths;
}