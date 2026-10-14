# Short Responses

For this short response assignment, aim to write a response with the following
qualities (your instructor will give you feedback on these areas):

- [ ] Addresses all parts of the prompt
- [ ] Accurately uses relevant technical terminology
- [ ] Is free of grammar and spelling mistakes (double check with Grammarly!)
- [ ] Uses markdown to enhance readability (preview in VS Code with
      Command/Control + Shift + V)
- [ ] Is easy to comprehend

Write your response in the space provided. Make sure to preview your markdown
to check how it is rendered before submitting.

## Question 1

Running `python3 main.py` prints one correct answer and then this:

```
Traceback (most recent call last):
  File "main.py", line 4, in <module>
    print(checkout(100, "guest"))
          ~~~~~~~~^^^^^^^^^^^^^^
  File "app/store.py", line 14, in checkout
    return apply_discount(total, percent)
  File "app/store.py", line 9, in apply_discount
    return total - (total * percent_off / 100)
                    ~~~~~~^~~~~~~~~~~~~
TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
```

### Prompt 1

Explain this traceback to somebody who has never read one.

Cover all five:

- **Where to start reading, and why.** Say which line you read first and what
  it tells you, then work back through the rest in the order you actually use
  them.
- **What each of the three `File` lines is doing there.** They are not three
  errors. Say what the list as a whole represents.
- **The error in plain language.** What did Python refuse to do, and what was
  the value it refused to do it with?
- **Where the bad value came from.** The error appears on line 9 of
  `app/store.py`. That is not where the problem started. Name the line that
  produced the value, and say what in the program made it come out that way.
- **Which line the fix belongs on, and why.** There is more than one place you
  *could* change to stop the crash. Say which one you would change and what is
  wrong with the others.

That fourth and fifth part are the whole exercise. A traceback points at the
line that could not cope, which is usually downstream of the line that is
actually wrong. Learning to read past the arrow is what separates somebody who
can fix a bug from somebody who can make an error message go away.

### Response 1

Your response here...
