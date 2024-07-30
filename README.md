# KeePass Conflict Fixer
[![pdm-managed](https://img.shields.io/endpoint?url=https%3A%2F%2Fcdn.jsdelivr.net%2Fgh%2Fpdm-project%2F.github%2Fbadge.json)](https://pdm-project.org)

Using Syncthing to keep your password database available on all your devices? Updated it without syncing beforehand? Ended up with `*sync-conflict*.kdbx` all over the place? Don't worry, this will fix it :)

## How it works
There are two possible cases,
1. Entry is *not* present, just add it
2. Entry is present in two *different* files, prioritize the one with the most *recent* date (i.e. changed the password and didn't sync)

## Notes
The main purpose of this project is to handle the tedious task of fixing the various sync conflicts, however, I also started this to learn the following
- Using some sort of dependency manager
- Writing **good** *conventional* commits
- Testing, both unit and integration
- Project structure
- Doc generation
- Logging, **configurable** *and* **meaningful**
- Test-driven development
- CI/CD, maybe also releases