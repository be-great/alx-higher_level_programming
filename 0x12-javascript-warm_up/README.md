#  0x12. JavaScript - Warm up 
## Variables

```bash
    let x;
    x = "Bob";
    let arr = [1,'Bob','Steve',10];
```
## comments 
- like C
```bash
// comment
/*comment*/
```
## Operators
```bash
 +
 === // data with same value and type
```
## conditions

```bash
if (x === "chocolate")
{
    alert("ok");
}
else
{
    alert("whatever")
}
```
## Functions

```bash
function mult(x, y)
{
    return x + y;
}
mult(10, 11);
```

## Events
- listen on activity on the browser . Example when clicking on the page alert a message.
```bash
document.querySelector("html").addEventListener("click", function () {
  alert("Ouch! Stop poking me!");
});

```
## Examples
- change h1 text content
```bash
let x = document.querySelector("h1")
x.textContent = "HI ROBOT"
```
- Adding a personalized welcome message
```bash
let myButton = document.querySelector("button");
let myHeading = document.querySelector("h1");
function set()
{
    name = prompt("Enter your name ");
    localStorage.setItem("name",name);
    myHeading.textContent = `Hello,  ${name}`
}

if (!localStorage.getItem('name'))
{
    set();
}
else
{
    let name = localStorage.getItem('name');
    myHeading.textContent = `Hello,  ${name}`
}
mybutton.click = () =>
{
    set();
}
```
## What are differences between var, const and let

- Var : It function_scope varaible that can be ressigned.define a variable in the local scope
- const: Block_scoped like (if, while and for scope) can't be ressigned. defined a variable in a local scope.
- let : Block_scoped that can be ressigned
- var, const , var can be global if it's declared outside a scope. and local if declared inside function_scope.

## Style check
```bash
npm install semistandard
semistandard
```
