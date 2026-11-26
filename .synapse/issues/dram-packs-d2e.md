---
id: dram-packs-d2e
title: Build initial dram packs
status: open
type: feature
priority: 2
created_at: 2026-11-26T12:44:00Z
updated_at: 2026-11-26T12:44:06Z
closed_at: ~
close_reason: ~
external_ref: gh-glenngillen/dram-packs#1
worker: ai
persona: software-engineer
---
Building a new CLI. The initial early-stage development of it is in ../dram. I will share the spec later as a link.

Within that spec, there is the concept of rule packs, which is a way of defining a bunch of assessments or recommendations and things that should be generated based on historical agent usage. There are also, I think, 8 or 9 different patterns and then 40+ different rules or assessments within those patterns. They are designed to help us build out a standard framework for assessing people's usage of AI (if they're using it efficiently) and coaching them to do better.

I want you to go through and implement all those patterns and rule packs based on the current example: rule packs that our engineer has already built.  example dram packs: https://github.com/owenrumney/dram-packs, original spec: https://claude.ai/artifact/7Kivvnz4VxYDVCB3tVbv8H?sk=oc_o-Fb9JsCMK_MU5os4Pw#spec (you may need to be authd to access it)