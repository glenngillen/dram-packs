# Learn From Production

## Overview

Source ID `learn-from-production`; Checking the work, rung 11. Turn actual production signals into agent fixes with a regression check. Detection requires model judgement.

## Requirements

- Applies to work on production services.
- Seen requires work started from an actual alert/error/log/SLO signal supplied to the agent and a fix including a check that would catch the problem next time.
- Exclude generic bug requests without the signal and fixes without a new preventive check.
- Cite the person request carrying the signal and the new check as completion.
- Continuous requires a person/team-configured alert/error trigger starting agent work automatically in the window, applied and holding.
- Coach on production fixes adding no regression check. The guide asks the person to use a real redacted production error and request a reproducing test before the fix.

## Acceptance Criteria

- [ ] Recognize “Here's the error from the alert … fix it and add a test that reproduces it” with the resulting check; reject “Fix the bug in payments” without a signal.
- [ ] Recognize an attributable error-tracker trigger starting a headless fix with a regression test; reject a fix with no new check.
- [ ] A guided explanation of an alert without supplying it and creating the preventive check is incomplete.
- [ ] No production credentials or real customer incident content are committed to fixtures or guide examples.

## Edge Cases

- A trigger can supply the intentional action through person/team configuration; an agent starting itself does not.
- The pack does not fetch production logs or connect to error services. It can use only evidence the CLI is already authorized to collect.

## Dependencies

- [Pattern evidence](pattern-evidence.md), [evaluation readiness](evaluation-readiness.md), [coaching content](coaching-content.md).
- Production-signal provenance, fix-to-check judgement and trigger/run evidence; unsupported detection remains disabled.
