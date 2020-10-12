# Computer Architecture

## Project

* [Implement the LS-8 Emulator](ls8/)

## Task List: add this to the first comment of your Pull Request

### Day 1: Get `print8.ls8` running

- [x] Inventory what is here
- [x] Implement the `CPU` constructor
- [x] Add RAM functions `ram_read()` and `ram_write()`
- [x] Implement the core of `run()`
- [x] Implement the `HLT` instruction handler
- [x] Add the `LDI` instruction
- [x] Add the `PRN` instruction

### Day 2: Add the ability to load files dynamically, get `mult.ls8` running

- [x] Un-hardcode the machine code
- [x] Implement the `load()` function to load an `.ls8` file given the filename
      passed in as an argument
- [x] Implement a Multiply instruction (run `mult.ls8`)

### Day 3: Stack

- [x] Implement the System Stack and be able to run the `stack.ls8` program

### Day 4: Get `call.ls8` running

- [x] Implement the CALL and RET instructions
- [x] Implement Subroutine Calls and be able to run the `call.ls8` program

### Stretch

- [ ] Add the timer interrupt to the LS-8 emulator
- [ ] Add the keyboard interrupt to the LS-8 emulator
- [ ] Write an LS-8 assembly program to draw a curved histogram on the screen

## SPRINT CHALLENGE: Minimum Viable Product

Your finished project must include all of the following requirements:

- [x] Add the `CMP` instruction and `equal` flag to your LS-8.

- [x] Add the `JMP` instruction.

- [x] Add the `JEQ` and `JNE` instructions.

[See the LS-8 spec for details](https://github.com/LambdaSchool/Computer-Architecture/blob/master/LS8-spec.md)

In your solution, it is essential that you follow best practices and produce
clean and professional results. Schedule time to review, refine, and assess your
work and perform basic professional polishing including spell-checking and
grammar-checking on your work. It is better to submit a challenge that meets MVP
than one that attempts too much and does not.

Validate your work through testing and ensure that your code operates as designed.

[Here is some code](./ls8/examples/sctest.ls8) that exercises the above instructions. It should
print:

```
1
4
5
```

```
# Code to test the Sprint Challenge
#
# Expected output:
# 1
# 4
# 5