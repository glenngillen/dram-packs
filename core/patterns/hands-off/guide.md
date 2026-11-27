# Hands off: guide

Take one of your own commands that you already trust, run it without watching, and use what it produces.

> **Detection is not available yet.** Dram cannot recognize this pattern in your sessions today, so finishing this guide will not show a recognition. The guide is still worth doing: a familiar workflow running on its own frees the time you spend watching it.

## 1. Check the safety prerequisite first

An unattended run needs **narrowly scoped permissions for unattended work** (see Scope permissions). If you have not yet run an unattended session with a scoped permission set, do that first. Never make a run unattended by switching permission checks off.

## 2. Pick a familiar command of your own

Choose a command or skill **you or your team wrote** (not a built-in or a plugin) that you have already run by hand at least three times, with results you used: for example a release-notes or triage command.

If you have no such command, or none you have run by hand three times, **stop here**. There is no exercise and nothing to recognize. Running it by hand on real work first is the right step.

## 3. Inspect what it needs

Ask your agent:

> Look at my command's definition and at this harness's actual supported way to run it headless. List the exact tools and commands it uses, and propose a narrowly scoped permission set for an unattended run. Do not run it.

Review the list. If anything is broader than the command needs, narrow it before going on.

## 4. Take the step: run it unattended on real work and use the output

Start the run yourself on real work in your project, either **headless** or interactively letting it work for **at least fifteen minutes** without prompting it. A shorter interactive run is not unattended. When it finishes, read the output and **use it**: publish the notes, apply the labels, merge or act on the result.

**Done:** your own command ran unattended (headless, or at least fifteen minutes of continued agent work without a prompt from you) and you used what it produced. That is this pattern.

**Not done yet:** if you only set up permissions, ran the command while watching it, ran it interactively for less than fifteen minutes without a qualifying headless or unprompted stretch, or the output was thrown away, the pattern has not happened yet. That is fine. Nothing is recorded against you; try again when the next real use for the command comes up.

## Later

Once several patterns happen on their own, a schedule or trigger you configure can run the command for you, with the same scoped permissions. That comes later, not as a shortcut.
