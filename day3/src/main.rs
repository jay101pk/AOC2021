use std::fs;

fn main() {
    let input = fs::read_to_string("input").expect("Unknow file");
    let data = convert_data(input.lines());
    // data.iter().for_each(|x| println!("{}",x));
    part1(&data);
    let a = part2(&data, true) as u32;
    let b = part2(&data, false) as u32;
    println!("o2 {} co2 {} ans {}",a,b, a * b);
}

fn convert_data(input: std::str::Lines) -> Vec<u16> {
    let mut data = Vec::new();

    for line in input {
        data.push(usize::from_str_radix(line, 2).unwrap() as u16);
    }

    return data;
}

fn part1(data: &[u16]) {
    let num_bits = 12;
    let num_words = data.len();
    let mut gamma = 0;
    for i in 0..num_bits {
        let mut c = 0;
        for d in data {
            if (d >> i) % 2 == 1 {
                c += 1;
            }
        }
        if c >= num_words / 2 {
            gamma |= 1 << i;
        }
    }

    println!(
        "Gamma: {}. Beta {}. Ans {}",
        gamma,
        !gamma & 0xFFF,
        gamma * (!gamma & 0xFFF)
    )
}

fn part2(data: &[u16], filt: bool) -> u16 {
    let num_bits = 12;
    let mut num_words = 1000;

    let mut a = data.to_vec();
    let mut i = num_bits - 1;
    while i >= 0 && a.len() > 1 {
        let mut c = 0;
        let mut b: Vec<u16> = Vec::new();
        for d in a.clone() {
            if (d >> i) % 2 == 1 {
                c += 1;
            }
        }
        let r = if filt {
            if c as f32 >= num_words as f32 / 2.0 {
                1
            } else {
                0
            }
        } else {
            if c as f32 >= num_words as f32 / 2.0 {
                0
            } else {
                1
            }
        };
        for d in a.clone() {
            if (d >> i) % 2 == r {
                b.push(d);
            }
        }
        a = b;
        i -= 1;
        num_words = a.len();
    }

    return a[0];
}
