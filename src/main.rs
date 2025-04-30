fn main() {
    //VECTORS - can only have one value

    //Initialization --> type annotation only needed because Rust doesn't know
    //what type the values are
    let mut v: Vec<i32> = Vec::new();

    //No type annotations because Rust assumes vector is Vec<i32>
    let v1 = vec![1, 2, 3, 4, 5];

    //to add elements -> if elements are added later, rust assumes vector
    // is Vec<type of element added>
    v.push(1);
    v.push(2);
    v.push(3);
    v.push(4);
    v.push(5);
    
    //Accessing the elements
    //referencing with the index, causes rust to panic if index is invalid
    let _third: &i32 = &v1[2];

    //references with .get(index), returns an enum which can be then matched to outcomes
    let _third: Option<&i32> = v.get(2);
    match _third {
        Some(_third) => {println!("{_third}")},
        None => {},
    }

    //Iterate over elements
    for &i in &v1 {
        //println!("{i}")
    }

    //Iterate while changing each element
    for i in &mut v {
        *i += 50;
        //println!("{}", i);
    }
    //Stopped at 8.1 to go to Enums (6.1)
    
}
