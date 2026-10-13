import fs from "node:fs";
import path from "node:path";

const root = process.cwd();
const skillsRoot = path.join(root, "skills");
const errors = [];

if (!fs.existsSync(skillsRoot)) {
  errors.push("Missing skills directory.");
}

const skillFolders = fs.existsSync(skillsRoot)
  ? fs
      .readdirSync(skillsRoot, { withFileTypes: true })
      .filter((entry) => entry.isDirectory())
      .map((entry) => entry.name)
      .sort()
  : [];

const declaredNames = new Map();

for (const folder of skillFolders) {
  const skillPath = path.join(skillsRoot, folder, "SKILL.md");
  if (!fs.existsSync(skillPath)) {
    errors.push(`${folder}: missing SKILL.md`);
    continue;
  }

  const source = fs.readFileSync(skillPath, "utf8");
  const frontmatter = source.match(/^---\s*\r?\n([\s\S]*?)\r?\n---\s*\r?\n/);
  if (!frontmatter) {
    errors.push(`${folder}: missing YAML frontmatter`);
    continue;
  }

  const nameMatch = frontmatter[1].match(/^name:\s*(.+?)\s*$/m);
  const descriptionMatch = frontmatter[1].match(/^description:\s*(.+?)\s*$/m);
  const name = nameMatch?.[1]?.replace(/^['"]|['"]$/g, "");

  if (!name) {
    errors.push(`${folder}: missing frontmatter name`);
  } else if (name !== folder) {
    errors.push(`${folder}: frontmatter name is ${name}`);
  } else if (declaredNames.has(name)) {
    errors.push(`${folder}: duplicate name also used by ${declaredNames.get(name)}`);
  } else {
    declaredNames.set(name, folder);
  }

  if (!descriptionMatch?.[1]?.trim()) {
    errors.push(`${folder}: missing frontmatter description`);
  }
}

if (skillFolders.length === 0) {
  errors.push("No skill folders found.");
}

if (errors.length > 0) {
  console.error("Skills package validation failed:");
  for (const error of errors) console.error(`- ${error}`);
  process.exit(1);
}

console.log(`Validated ${skillFolders.length} skills for Skills CLI discovery.`);
