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

A teammate has rewritten four functions as one-liners, and opened a pull
request titled "tidy up loops".

```py
# 1. find the first user who has not paid
unpaid = [u for u in users if not u["paid"]][0]

# 2. print a greeting for everyone
[print(f"Hi {u['name']}") for u in users]

# 3. count how many users live in Chicago
in_chicago = len([u for u in users if u["city"] == "Chicago"])

# 4. the three highest scores
top = sorted(scores)[-3:]
```

You are reviewing it.

### Prompt 1

Write the review. For **each** of the four:

- Say whether a comprehension is the right tool here, and why.
- If it is wrong, say what it should be instead and what it costs as written.
  "It is less readable" is not an answer on its own. Say what breaks, what it
  does extra, or what a reader would get wrong.
- If it is right, say so plainly and move on. Not every line in a pull request
  needs changing.

Then finish with one paragraph: **what question do you ask yourself to decide
between a loop and a comprehension?** One sentence that would actually settle
it, not a list of considerations.

Number 4 is an interesting one! Try recreating an unsorted `scores` list and
then run the code. Does it produce the right order? Is it a bug or a feature?

### Response 1

Your response here...
