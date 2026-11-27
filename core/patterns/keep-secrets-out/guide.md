# Keep secrets out: guide

Keep the files that hold your secrets out of your agent's reach, using a rule rather than its good behaviour, and keep credentials out of what you type.

> **Detection is not available yet.** Dram cannot recognize this pattern in your sessions today, so finishing this guide will not show a recognition. The guide is still worth doing: a rule stops a read that a careful-sounding agent might still make.

**Throughout this guide, nobody opens a secret file.** You and your agent work with file names and locations only, never contents.

## 1. Pick a real repository with secrets

Think of a repository you work in regularly that has secret files: environment files, a secrets config, a credentials file.

- If none of your repositories has secret files, **stop here**. There is no exercise and nothing to recognize.

## 2. Find where the secrets actually live

Ask your agent, by names only:

> Without opening or printing any file, list the paths in this repository that are likely to hold secrets: environment files, secrets configs, credential or key files. Check the ignore files for hints. Names only.

Check the list against what you know. Secrets are often in more than one place: `.env` files **and** a config such as `config/secrets.yml`. A rule that covers only one of them leaves the other open.

## 3. Ask for deny rules that cover those locations

Ask your agent to inspect **its actual supported permission configuration** and propose deny rules for those paths. Ask it to explain:

- which settings file the rules go in (yours, the project's, or a shared team file) and **what takes precedence** over that file;
- whether the rule stops every route to the file, including shell commands, and in the modes you actually run it in.

Review the proposal before it is saved. Keep the values where they are; the rule only keeps the agent away from them.

## 4. Take the step: work in the repository with the rule in effect

Do your next real task in that repository.

**Done:** a session in that repository ran with your rule in effect, covering where its secrets really live. That is what this pattern recognizes once detection is available.

**Not done yet:** if you discussed rules but saved none, or the rule covers `.env` while the secrets sit somewhere else, or you have not had a session in that repository since, the pattern has not happened yet. That is fine. Nothing is recorded against you; finish the rule and use the repository on real work.

## Also: keep credentials out of prompts

If you need the agent to use a credential, point it at where the value is configured instead of pasting the value into your prompt.

## Later

Once several patterns happen on their own, rules for your usual secret locations can live in your user-level settings and cover every repository you open. That comes later; it does not replace checking where each repository keeps its secrets.
