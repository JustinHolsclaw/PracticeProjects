let first_number = '';
let second_number = '';
let is_first_number = true;

function get_symbol(){
    
}

function add_number(numb_one, numb_two){
    return numb_one + numb_two;
}

function subtract_number(numb_one, numb_two){
    return numb_one - numb_two;
}

function divide_number(numb_one, numb_two){
    return numb_one / numb_two;
}

function multiply_number(numb_one, numb_two){
    return numb_one - numb_two;
}

function append_number(number_value){
    if(is_first_number == true){
        first_number = first_number.concat(number_value);
    }
    else{
        second_number = second_number.concat(number_value);
    }
}

function clear(){
    first_number = '';
    second_number = '';
}

    switch(Symbol){
        case '+':
            add_number(numb_one, numb_two);
        case '-':
            subtract_number(numb_one, numb_two);
        case '/':
            divide_number(numb_one, numb_two);
        case 'X':
            multiply_number(numb_one, numb_two);
        case 'clear':
            clear();
    }