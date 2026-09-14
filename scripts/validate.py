import json
from pathlib import Path
import re
import sys


def require(condition, message):
    if not condition:
        raise ValueError(message)


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def validate(root):
    root = Path(root).resolve()
    plugins = {path.name: path for path in (root / "plugins").iterdir() if path.is_dir()}
    require(plugins, "No plugins found")
    for name, plugin in plugins.items():
        require(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name), f"Invalid plugin name: {name}")
        base = read_json(plugin / "plugin.json")
        require(base.get("name") == name, f"Plugin identity differs: {plugin}")
        require(base.get("$schema") == "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json", "Missing portable schema")
        for host in ("codex", "cursor", "claude"):
            manifest = read_json(plugin / f".{host}-plugin/plugin.json")
            for key in ("name", "version", "description", "author"):
                require(manifest.get(key) == base.get(key), f"Plugin identity differs: {host} {key}")
            if host in ("codex", "cursor"):
                require(manifest.get("skills") == "./skills/", f"Invalid skills path: {host}")
        skills = [path for path in (plugin / "skills").iterdir() if path.is_dir()]
        require(skills, f"No skills found: {plugin}")
        for skill in skills:
            content = (skill / "SKILL.md").read_text(encoding="utf-8")
            frontmatter = re.match(r"\A---\n(.*?)\n---\n(.+)", content, re.DOTALL)
            require(frontmatter, f"Missing skill frontmatter or body: {skill}")
            fields = dict(re.findall(r"^([a-z-]+): (.+)$", frontmatter[1], re.MULTILINE))
            if fields.get("description") in (">", ">-", ">+"):
                description = re.search(
                    r"^description: >[-+]?\n((?:[ \t]+[^\n]*(?:\n|$)|\n)*)",
                    frontmatter[1],
                    re.MULTILINE,
                )
                fields["description"] = " ".join(description[1].split()) if description else ""
            require(fields.get("name") == skill.name, f"Invalid skill name: {skill}")
            require(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", skill.name) and len(skill.name) <= 64, f"Invalid skill name: {skill}")
            require(fields.get("description", "").strip(), f"Missing skill description: {skill}")
            changelog = (skill / "CHANGELOG.md").read_text(encoding="utf-8")
            for field in ("What", "Why", "Evidence", "Impact", "Reference"):
                require(f"**{field}**:" in changelog, f"Missing changelog field: {skill} {field}")
    for location in (".agents/plugins", ".claude-plugin", ".cursor-plugin"):
        catalog = read_json(root / location / "marketplace.json")
        require(catalog.get("name") == "slop-shop", f"Invalid catalog name: {location}")
        entries = catalog["plugins"]
        require(len(entries) == len(plugins) and {entry["name"] for entry in entries} == set(plugins), f"Catalog coverage differs: {location}")
        for entry in entries:
            source = entry["source"]
            if location == ".agents/plugins":
                require(source.get("source") == "local", "Expected local source")
                source = source["path"]
                require(entry.get("policy") == {"installation": "AVAILABLE", "authentication": "ON_INSTALL"}, "Invalid Codex policy")
                require(entry.get("category"), "Missing Codex category")
            require(source == f"./plugins/{entry['name']}", f"Invalid catalog source: {location}")
            require((root / source).resolve() == plugins[entry["name"]], f"Invalid catalog source: {source}")


if __name__ == "__main__":
    try:
        validate(Path(__file__).resolve().parents[1])
    except (ValueError, OSError, KeyError, TypeError) as error:
        print(f"Validation failed: {error}", file=sys.stderr)
        sys.exit(1)
    print("Plugin manifests, catalogs, and skill structure are valid.")
