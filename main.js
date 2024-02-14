// * Passing function as an argument
// function square(x) {
//   return x * x;
// }

// function my_map(func, arg_list) {
//   const result = [];
//   for (const i of arg_list) {
//     result.push(func(i));
//   }
//   return result;
// }

// const squares = my_map(square, [1, 2, 3, 4, 5]);

// console.log(squares); // => [ 1, 4, 9, 16, 25 ]

// * Returning function from a function
// function logger(msg) {
//   function log_message() {
//     console.log('Log:', msg);
//   }

//   return log_message;
// }

// const log_hi = logger('Hi!');
// log_hi(); // => Log: Hi!

// Another example
function html_tag(tag) {
  function wrap_text(msg) {
    console.log(`<${tag}>${msg}</${tag}>`);
  }

  return wrap_text;
}

const print_h1 = html_tag('h1');
print_h1('Test headline!'); // => <h1>Test headline!</h1>
print_h1('Another Headline'); // => <h1>Another Headline</h1>

const print_p = html_tag('p');
print_p('Test Paragraph!'); // => <p>Test Paragraph!</p>
