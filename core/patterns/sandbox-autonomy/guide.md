# Sandbox autonomy: guide

When a run goes unattended, give it a box to run in: a devcontainer or sandbox with its own checkout and none of your credentials.

> **Detection is not available yet.** Dram cannot recognize this pattern in your sessions today, so finishing this guide will not show a recognition. The guide is still worth doing: a mistake made inside a container stays inside it.

**Broad permissions are not part of this guide.** You can run in a container under the same scoped permissions you use now. Do not turn approvals off to try it.

## 1. Pick a real unattended task

Think of a real task you want to let run without watching: a dependency bump, a test backfill, a nightly tidy-up in your own project.

- If you have no task you would run unattended, **stop here**. There is no exercise and nothing to recognize.
- Before running work unattended, scoped permissions (Scope permissions), guards for destructive commands (Guard destructive commands) and secret files kept out of reach (Keep secrets out) come first.

## 2. Ask for a contained environment

Ask your agent to check **what this machine actually supports** (a devcontainer, a container runtime, a remote sandbox) and propose an environment for this repository:

> Propose a devcontainer or sandbox for unattended runs of this repository. It should have its own checkout, should not mount my cloud configuration, SSH keys or other credentials, and should not run privileged. Tell me what it can still reach over the network. Show me the configuration before writing it.

Review it. A container that mounts your credentials, or runs privileged, gives back most of what it was meant to keep out. A separate worktree on your own machine is useful for other reasons, but it is not a sandbox.

## 3. Take the step: run the real task inside it

Start your unattended task inside that environment.

**Done:** the unattended run happened inside the container, devcontainer, VM or remote sandbox, started by you. That is what this pattern recognizes once detection is available.

**Not done yet:** if you wrote the configuration but ran the task on your own machine, or have not run anything in it yet, the pattern has not happened yet. That is fine. Nothing is recorded against you; run your next unattended task inside it.

## Other ways to reduce the risk

Running as a separate user account, or on a machine that holds no credentials, also keeps a run away from what matters, although a separate user still shares the network and anything readable system-wide. These are valid choices. Dram cannot recognize them yet, so they are neither counted for nor against you.

## Later

Once several patterns happen on their own, a launch script or devcontainer setup you own can make the contained environment the default for every unattended run. That comes later.
