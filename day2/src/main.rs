use std::fs;
use regex::Regex;

#[derive(Debug)]
enum Dir {
    Forward,
    Down,
    Up
}

fn main() {
    let input = fs::read_to_string("data.txt").expect("File not found");
    let data = convert_data(input.lines());
    // data.iter().for_each(|val| {println!("{:?}", val)});
    part1(&data);
    part2(&data);
}

fn convert_data(lines : std::str::Lines) -> Vec<(Dir, u32)>
{
    let mut data = Vec::new();

    let re = Regex::new(r"(\w+)\s(\d+)").unwrap();

    for line in lines {
        let m = re.captures(line).unwrap();
        let d = m.get(1).unwrap().as_str();
        let di = match d {
            "forward" => Dir::Forward,
            "down" => Dir::Down,
            "up" => Dir::Up,
            _ => Dir::Forward
        };
        let n : u32 = m.get(2).unwrap().as_str().parse().unwrap();

        data.push((di, n));
    }

    return data;
}


fn part1(data : & [(Dir, u32)]) {
    let mut depth = 0;
    let mut horz = 0;
    
    for d in data {
        match d.0 {
            Dir::Forward => horz += d.1,
            Dir::Up => depth -= d.1,
            Dir::Down => depth += d.1,
        }
    }

    println!("Ans: {}", depth * horz);

}


fn part2(data : &[(Dir, u32)]) {
    let mut depth = 0;
    let mut horz = 0;
    let mut ang = 0;

    for d in data {
        match d.0 {
            Dir::Forward => {horz += d.1;
            depth += d.1 * ang;
            },
            Dir::Up => ang -= d.1,
            Dir::Down => ang += d.1,
        }
    }

    println!("Ans part2: {}", depth * horz);
}