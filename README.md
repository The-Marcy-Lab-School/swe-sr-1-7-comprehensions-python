# Reading a Traceback

Work out where an error came from, which is almost never where it appeared.

- [AI Use on This Assignment](#ai-use-on-this-assignment)
- [Setup](#setup)
- [Instructions](#instructions)
- [Submitting](#submitting)

## AI Use on This Assignment

These are your own words. Do not use AI to draft or rewrite your responses —
that holds in every mode, including implementer mode. You may use it to check
grammar and spelling on writing you have already done, and you may use it
before you start to quiz you on error types until you can name them without
notes. Paste this if you want that kind of help:

> You are acting as a tutor. Quiz me on Python error types and on how to read
> a traceback, until I can say what each part of one tells me without looking
> anything up. Do not read this particular traceback for me. Tell me when my
> reasoning is wrong or imprecise, and do not write or rewrite any part of my
> response.

Pasting a traceback into a model and copying what it says back out is the
fastest way to never learn this. Reading one takes about a minute once you
know the shape, and you will read thousands.

## Setup

Clone this repo into `development/mod-1` and `cd` into it. Make a draft branch
before you start.

```sh
git clone [your_repo]
cd [your_repo]
git checkout -b draft
```

There is nothing to install. Run the program with:

```sh
python3 main.py
```

## Instructions

Run the program first. Read the traceback it prints before you read any of the
source files, then answer the prompt in `short_response.md`.

Aim for a response with these qualities. Your instructor will give you
feedback on each one:

- [ ] Addresses all parts of the prompt
- [ ] Accurately uses relevant technical terminology
- [ ] Is free of grammar and spelling mistakes (double check with Grammarly!)
- [ ] Uses markdown to enhance readability (preview in VS Code with
      Command/Control + Shift + V)
- [ ] Is easy to comprehend

## Submitting

```sh
git add -A
git commit -m "your message"
git push
```

Open a pull request to your instructor for feedback.
