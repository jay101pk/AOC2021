use std::fs;

fn main() {
    let input = fs::read_to_string("input").expect("Unknow file");
    let draws: Vec<u32> = input
        .lines()
        .nth(0)
        .unwrap()
        .split(",")
        .map(|x| x.parse().unwrap())
        .collect();

    let mut boards: Vec<Vec<u32>> = Vec::new();
    let mut iter = input.lines().skip(1);
    for _ in 0..100 {
        iter.by_ref().next();
        let mut board: Vec<u32> = Vec::new();
        for _ in 0..5 {
            board.extend(
                iter.by_ref()
                    .next()
                    .unwrap()
                    .split_whitespace()
                    .map(|x| x.parse::<u32>().unwrap()),
            );
        }
        boards.push(board);
    }

    part1(&draws, &boards);
    part2(&draws, &boards);
}

fn check_bingo(board: &[bool]) -> bool {
    for i in 0..5 {
        if board
            .iter()
            .enumerate()
            .filter(|(x, _y)| (0..5).map(|z| z + i * 5).any(|z| z == *x))
            .all(|(_x, y)| *y)
        {
            return true;
        }
        if board
            .iter()
            .enumerate()
            .filter(|(x, _y)| (0..5).map(|z| i + z * 5).any(|z| z == *x))
            .all(|(_x, y)| *y)
        {
            return true;
        }
    }
    return false;
}

fn part1(draws: &[u32], boards: &[Vec<u32>]) {
    let mut marked: Vec<Vec<bool>> = vec![vec![false; 25]; 100];
    for draw in draws {
        for (i, board) in boards.iter().enumerate() {
            if let Some(j) = board.iter().position(|x| x == draw) {
                marked[i][j] = true;
            }
        }
        let mut found = false;
        for (i, (board, mark)) in boards.iter().zip(marked.iter()).enumerate() {
            if check_bingo(mark) {
                let sum: u32 = board
                    .iter()
                    .zip(mark.iter())
                    .filter(|&x| !x.1)
                    .map(|x| x.0)
                    .sum();
                println!("{}", sum * draw);
                found = true;
                break;
            }
        }
        if found {
            break;
        }
    }
}

fn part2(draws: &[u32], boards: &[Vec<u32>]) {
    let mut marked: Vec<Vec<bool>> = vec![vec![false; 25]; 100];
    let mut winBoard = 0;
    for draw in draws {
        for (i, board) in boards.iter().enumerate() {
            if let Some(j) = board.iter().position(|x| x == draw) {
                marked[i][j] = true;
            }
        }
        if boards
            .iter()
            .zip(marked.iter())
            .filter(|(_x, y)| check_bingo(y))
            .count()
            == 99
        {
            winBoard = boards
                .iter()
                .zip(marked.iter())
                .enumerate()
                .filter(|(_i, (_x, y))| !check_bingo(y))
                .next()
                .unwrap()
                .0;
            println!("{}", winBoard)
        }
        if boards
            .iter()
            .zip(marked.iter())
            .filter(|(_x, y)| check_bingo(y))
            .count()
            == 100
        {
            let a = &boards[winBoard];
            let b = &marked[winBoard];
            let sum = a.iter().zip(b).filter(|&x| !x.1).map(|x| x.0).sum::<u32>();
            println!("{} {}", winBoard, sum * draw);
            break;
        }
    }
}
