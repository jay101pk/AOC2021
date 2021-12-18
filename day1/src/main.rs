use std::fs;

fn main() {
    let input = fs::read_to_string("input.txt").expect("Unknown file");

    let lines = input.lines();
    let data = convert_data(lines);
    part1(&data);
    part2(&data);
}

fn convert_data(lines : std::str::Lines) -> Vec<u32>
{
    let mut data : Vec<u32> = Vec::new();
    for elem in lines {
        data.push(elem.parse().expect("Not a number"));
    }

    return data;
}


fn part1(lines : & [u32]) {
    let mut previous = lines[0];
    let mut count = 0;
    for elem  in 1..lines.len(){
        if lines[elem] > previous {
            count += 1;
        }
        previous = lines[elem];
    }

    println!("Count: {}", count);
}


fn part2(lines : & [u32]) {
    let mut previous = lines[0] + lines[1] + lines[2];
    let mut count = 0; 
    for elem in 3..lines.len() {
        let cur = lines[elem] + lines[elem - 1] + lines[elem - 2]; 
        if cur > previous{
            count += 1;
        }
        previous =cur;
    }
    println!("Count part2: {}", count);
}
