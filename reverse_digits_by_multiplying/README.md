# Find digits `ABCD` so that `ABCD * 4 = DCBA`?

The question is simple:

Find a number composed of four digits, `ABCD`, so that `ABCD * 4 = DCBA`.

I found the question on the internet, but did not watch the solution. Just
out of curiosity, I figured perhaps I could figure this one out on my own.

We could assuming the digits are all different, and that none of them are zero.

But for now let us not be so restrictive, and just assume that we want an actual 4 digit number > 0. "Actual" means, the first digit is already > 0.

Lets start with the first and last digits, `A` and `D`.

The first digit multiplied by four must obviously be smaller than 10, otherwise we would get a 5 digit number.

So `A` must be 0,1 or 2.

We already said we want `A` to be larger than 0, but will waive that requirement for now. Concidering 0 does seem slightly odd, though.

What must `D` then be? We know `D * 4` must have `A` as last digit. Which digit multiplied with 4 has 0,1 or two as a result?
Obviously nothing multiplied by 4 can have the uneven 1 as a last digit, so `A` can not be 0.
Having 0 as a last digit would only work if `D` was 5, as we do not allow `D` to be 0 if `A` was already that.
Having 2 as a last digit would only work if `D` was 3 or 8, as `3 * 4 = 12` and `8 * 4 = 32`.

We now know:

```
A is 0 or 2
D is 3 or 8 - if A is 2
  is 5      - if A is 0
```

Now lets concider one of the other digits. If the other digit is the largest possible digit, 9, then overflow of multiplying it with 4 is pretty limited: `4 * 9 = 36` - the immediate overflow is 3. Now there could be a further overflow from further right coming in on top of this, of course. Suppose `D` was 8, overflowing with 3, `C` would also be 9 - just forgive me - then the sum `36 + 3 = 39` would still only overflow 3, and so on. So given `A` in `{0,1,2}`, we know that `A * 4 <= 8` and `8 + overflow <= 11`.

We get two bits of information out of that:

The overflow from multiplying digit `B` must be 0 AND `A` must be 2. Why?
If `A` is 0, then `A * 4 + overflow = 0 + overflow <= 3` - but we needed it to be 5, as `A * 4 + overflow = xD = x5` (for any `x`).
So `A` can not be 0.

So `A = 2`.

We still want to show that the overflow is 0.

```
A * 4 + overflow = 8 + overflow <= 9
```

If overflow is 1, then `D = A * 4 + 1 = 9`. But `D` may only be 3 or 8 - so the overflow must be 0 and `D` must be 8.

We now know:

```
A = 2
D = 8
```

and

```
B * 4 + overflow(C) <= 9
```

We have not used the statement yet, that all digits must be different. Lets see how far we can continue without that.

So `B` must be 0,1 or 2.

Coming from the other side, we already know that

```
D * 4 = 8 * 4 = 32
```

so the overflow from `D` into `C` is 3.

Taking just the inner digts into account (we already know nothing overflows into `A` and 3 overflows from `D`), we now must figure out some `B` and `C` so that

``` 
"BC" * 4 + 3 = "CB"
```

and `B` is in `{0,1,2}`.

This where my reasoning stops - let's put this into a equation, out of lack of other useful thoughts (or do you have any?). 

```
4 * ( B * 10 + C ) + 3 = C * 10 + B
```

Lets bring all the `B`s on one side and the `C`s on the other:

```
39 * B + 3 = 6 * C
```

Oh yeah!

```
     13 * B + 1
C =  ----------
         2
```

We already see that for `C` to be a whole number, `13 * B + 1` must be devidable by `2` - so must be even. Shorter still, `13 * B` must be odd.
Of the three digits we are still concidering for `B` (one of `0`, `1` and `2`), that only works for

```
B = 1
```

And then we also have

```
C = 7
```

That leaves us with:

```
ABCD = 2173
```

Let's check:

```
2178 * 4 = 8712
```

So we now know that 8712 is a solution, and since we ruled out all other digits, it's the only solution!
  
