# Script It

## Overview

Source ID `script-it`; Guides, rung 5. Use deterministic tooling for mechanical edits instead of repeating manual agent edits. Detection combines judgement with execution/configuration evidence.

## Requirements

- Applies to mechanical changes across many files, such as renames, migrations and boilerplate.
- Seen requires a person-requested script/codemod/tool that actually makes the change, or a person-configured language/MCP tool subsequently used by the agent.
- Exclude unprompted throwaway scripts and scripts written but never run.
- Cite the request/configuration and the tool execution making the change as completion.
- Continuous requires a repository-saved script or command wrapper reused in the window, with applicable holding evidence.
- Coach when the same mechanical edit is made manually across at least ten files. The guide asks for a script on the next real rename/migration and encourages review of the script.

## Acceptance Criteria

- [ ] Recognize “Write a codemod for the API rename and run it on src/” followed by its execution; reject forty files edited individually.
- [ ] Recognize “Use the scaffold script to add the new endpoint” with execution; reject a script never run.
- [ ] A configured code-intelligence tool must actually be used; agent discovery alone does not establish person configuration.
- [ ] Guided script discussion without the person's requested execution cannot complete the pattern.

## Edge Cases

- Ten files is the source's coach trigger, not a new universal recognition threshold for “many”.
- A script's existence does not establish deterministic behavior, correct changes or reuse.

## Dependencies

- [Pattern evidence](pattern-evidence.md), [coaching content](coaching-content.md), [evaluation readiness](evaluation-readiness.md).
- Mechanical-task judgement, tool provenance, edit linkage and repeat execution evidence; retain disabled detection until these can be verified.

