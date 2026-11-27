# Scope permissions: guide

Fewer approval prompts without handing your agent everything: approve the specific commands your real work needs.

> **Detection is not available yet.** Dram cannot recognize this pattern in your sessions today, so finishing this guide will not show a recognition. The guide is still worth doing: a short allow list removes most prompts while keeping one wrong command away from everything else.

## 1. Pick a real repository you work in

Choose a repository where you regularly approve the same commands, or where you have been tempted to turn approvals off altogether.

- If you have no current work with an agent in any repository, **stop here**. There is no exercise and nothing to recognize.

## 2. Find the commands you actually approve

Ask your agent:

> Which commands and tools have I approved most often in this repository? List them, and say which are read-only, which run tests or builds, and which change anything outside this working copy.

Keep the ones the work really needs: running the tests, the build, read-only git commands. Leave out anything that deploys, deletes, or reaches production.

## 3. Ask for a narrow allow list

Ask your agent to inspect **its actual supported permission configuration** and propose an allow list for just those commands. Ask it to tell you:

- which settings file the list belongs in, and **whether any other setting (yours, the project's or a local one) would override it** with something broader;
- that no entry approves every command (a wildcard over the whole shell is not scoped).

Review the proposal before it is saved. Do not turn approvals off to save time: if you want fully hands-off runs, contain them in a sandbox instead (Sandbox autonomy).

## 4. Take the step: do real work under the list

Run your next real task in that repository in the normal approval mode.

**Done:** a session ran under your scoped allow list, without approvals turned off. If the task ran unattended, that also shows scoped permissions for unattended work, which Hands off needs before it is suggested.

**Not done yet:** if you edited the permissions but have not run a session under them, or a broader setting still overrides your list, or the session ran with approvals bypassed, the pattern has not happened yet. That is fine. Nothing is recorded against you; run your next real task under the scoped list.

## Later

Once several patterns happen on their own, a user-level or team allow list can cover every project, unattended runs included. That comes later, and it still never means approving everything.
