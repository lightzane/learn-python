# Learn First Class Functions

https://www.youtube.com/watch?v=kr0mpwqttM0

# Prerequisites:

- Python installed
- Nodejs installed

## First Class Functions

A Programming language is said to have a first-class function if it treats functions as first-class citizens.

## First Class Citizen (Programming)

A first-class citizen (somtimes called first-class objects) in a programming language is an entity which supports all the operations generally available to other entites. These operations typically include being passed as an argument, returned from a function, and assigned to a variable.

# Python

```bash
python main.py
```

```py
def square(x):
    return x * x

f = square(5)

print(square) # => <function square at 0x000002056C61D9E0>
print(f) # => 25
```

# Javascript

```bash
node main
```

```js
function square(x) {
  return x * x;
}

const f = square(5);

console.log(square); // => [Function: square]
console.log(f); // => 25
```

## Assigning function to a variable

```py
# main.py

def square(x):
    return x * x

f = square

print(square) # => <function square at 0x0000024EAFE1D9E0>
print(f(5)) # => 25
```

```js
// main.js

function square(x) {
  return x * x;
}

const f = square;

console.log(square); // => [Function: square]
console.log(f(5)); // 25
```

## Passing function as an argument

```py
# main.py

def square(x):
    return x * x

def my_map(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

squares = my_map(square, [1, 2, 3, 4, 5])

print(squares) # => [1, 4, 9, 16, 25]
```

```js
// main.js

function square(x) {
  return x * x;
}

function my_map(func, arg_list) {
  const result = [];
  for (const i of arg_list) {
    result.push(func(i));
  }
  return result;
}

const squares = my_map(square, [1, 2, 3, 4, 5]);

console.log(squares); // => [ 1, 4, 9, 16, 25 ]
```

## Returning function from a function

```py
# main.py

def logger(msg):

    def log_message():
        print('Log:', msg)

    return log_message

log_hi = logger('Hi!')
log_hi() # => Log: Hi!
```

```js
// main.js

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

function logger(msg) {
  function log_message() {
    console.log('Log:', msg);
  }

  return log_message;
}

const log_hi = logger('Hi!');
log_hi(); // => Log: Hi!
```

### Another example

```py
# main.py

def html_tag(tag):

    def wrap_text(msg):
        print(f'<{tag}>{msg}</{tag}>')

    return wrap_text

print_h1 = html_tag('h1')
print_h1('Test headline!') # => <h1>Test headline!</h1>
print_h1('Another Headline') # => <h1>Another Headline</h1>

print_p = html_tag('p')
print_p('Test Paragraph!') # => <p>Test Paragraph!</p>
```

```js
// main.js

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
```
