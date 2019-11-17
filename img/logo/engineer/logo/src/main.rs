#[allow(non_camel_case_types)]
type varo = usize;

fn peter<T: From<varo>>(x: &varo) -> T
{
    T::from(*x)
}

fn main()
{
    let engineer = 0;
    peter::<varo>(&engineer);
}
