# environment

This repository contains code for setting up an environment
for testing cooperative multi-agent control algorithms.

## Introduction

This environment simulates a human and an agent interacting
inside a kitchen. We call the human and the agent collectively
as actors. In this environment, each actor can hold one item
at a time. The environment also contains objects that these
actors can interact with.

To represent the state with numerical vectors, each entities
would be given an unique ID. The following is an exhaustive
list of all possible entities:

- human facing up (1)
- human facing down (2)
- human facing left (3)
- human facing right (4)
- agent facing up (5)
- agent facing down (6)
- agent facing left (7)
- agent facing right (8)
- apple (9)
- orange (10)
- cup with nothing (11)
- cup with apple juice (12)
- cup with orange juice (13)
- juicer with nothing (14)
- juicer with apple (15)
- juicer with orange (16)
- juicer with apple juice (17)
- juicer with orange juice (18)
- apple storage - closed (19)
- apple storage - opened (20)
- apple storage button (21)
- orange storage - closed (22)
- orange storage - opened (23)
- orange storage button (24)

A state is represented by (1) a grid of entities ID, and (2) a
numerical value for each actor that indicates what it is holding. 

This environment also supports the following actions:

- do nothing (0)
- move up (1)
- move down (2)
- move left (3)
- move right (4)
- take item (5)
- drop item (6)
- interact item (7)
