#!/usr/bin/node
/* make the none number NaN */

function findSecondBiggest()
{
    const args = process.argv.slice(2).map(Number);

    if (args.length <= 1)
    {
        console.log(0);
        return;
    }
    let max = -Infinity;
    let secondmax = -Infinity;

    for (const x of args)
    {
        if (x > max)
        {
            secondmax = max;
            max = x;
        }
        else if (x > secondmax && x < max) 
        {
            secondmax = x;
        }
    }
    console.log(secondmax);
}
findSecondBiggest();