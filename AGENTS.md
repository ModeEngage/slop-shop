# Repository guidance

This repository contains skills intended to work with `workslop`. Support Codex,
Cursor, and Claude Code from one shared plugin directory. Keep `README.md` brief.
Edit this file for repository guidance; `CLAUDE.md` is a relative symlink to it.

## Shared layout

Each plugin lives in `plugins/<plugin-name>/`. Its skills live in
`skills/<skill-name>/SKILL.md` inside that plugin. Keep one copy of each skill.
Put supporting references, scripts, and assets inside the plugin so they remain
available when the plugin is installed separately from this repository.

Keep the plugin folder name and manifest `name` equal. Keep `name`, `version`,
`description`, and `author` consistent across all four manifests.

| Format | Manifest inside the plugin | Catalog at the repository root |
| --- | --- | --- |
| Portable Agent Plugins | `plugin.json` | Uses the host's catalog |
| Codex compatibility | `.codex-plugin/plugin.json` | `.agents/plugins/marketplace.json` |
| Cursor | `.cursor-plugin/plugin.json` | `.cursor-plugin/marketplace.json` |
| Claude Code | `.claude-plugin/plugin.json` | `.claude-plugin/marketplace.json` |

## Codex

The root `plugin.json` declares the Agent Plugins schema through `$schema`:
`https://agent-plugins.org/schemas/1.0.0/plugin.schema.json`. Portable packages
discover skills in `skills/` without a manifest `skills` field.

This repository also keeps `.codex-plugin/plugin.json` for compatibility. It
declares `skills: "./skills/"` and stores presentation metadata in `interface`.
OpenAI-specific settings can instead use `extensions.com.openai` in the portable
manifest. If that object is present, it replaces the compatibility overlay;
the two are not merged.

The Codex catalog uses an object for each entry's source:
`{"source": "local", "path": "./plugins/<plugin-name>"}`. The path is relative
to the repository root. Preserve each entry's `policy.installation`,
`policy.authentication`, and `category` fields.

See the [OpenAI plugin format](https://developers.openai.com/plugins/build/plugins).

## Cursor

Cursor supports portable Agent Plugins and its own `.cursor-plugin/plugin.json`
format. This repository keeps both manifests. The Cursor manifest declares
`skills: "./skills/"`, relative to the plugin root.

The Cursor catalog has `name`, `owner`, and `plugins` fields. Each plugin entry
uses a string source such as `"./plugins/funnel"`, relative to the repository
root. Keep the catalog entry name equal to the plugin manifest name.

See the [Cursor plugin reference](https://prod.cursor.com/docs/reference/plugins)
and [official examples](https://github.com/cursor/plugins).

## Claude Code

Claude Code reads `.claude-plugin/plugin.json` for plugin identity and discovers
skills in the plugin's root `skills/` directory. Put only the manifest inside
`.claude-plugin/`; skill content belongs outside that directory.

The Claude Code catalog has `name`, `owner`, and `plugins` fields. Each entry in
this repository uses a string source such as `"./plugins/funnel"`, relative to
the repository root. Plugin skills use namespaced commands, such as
`/funnel:write-issues`.

See the [Claude Code plugin format](https://code.claude.com/docs/en/plugins).

## Changes and validation

- When adding or removing a plugin, update all three catalogs. Adding a skill
  to an existing plugin does not require a new catalog entry.
- Use lowercase letters, digits, and hyphens for skill names. Match the folder
  name to frontmatter `name`. Use an unquoted, single-line `description` to match
  the repository validator's supported metadata format.
- Keep shared instructions independent of host-specific tool names and variables.
  Check current host documentation before adding hooks or MCP configuration;
  those formats can differ between hosts.
- Update each changed skill's `CHANGELOG.md` with **What**, **Why**, **Evidence**,
  **Impact**, and **Reference** fields. Keep skill release metadata there, and
  consolidate changes into one release entry per merge request.
- Use ASD-STE100 simplified technical English for documentation and necessary
  code comments. Do not include issue or deliverable identifiers in documentation.

Run `python3 scripts/validate.py` after changes. GitLab CI runs the same command
from `.gitlab-ci.yml`. It checks repository metadata and structure; it does not
prove that a host can load or execute a skill. Do not add unit tests for metadata.
