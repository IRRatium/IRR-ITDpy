import os
import shutil

ROOT = os.path.dirname(os.path.abspath(__file__))

# 1. Переименовать папку itdpy -> itdirr
old_dir = os.path.join(ROOT, "itdpy")
new_dir = os.path.join(ROOT, "itdirr")

if os.path.exists(old_dir):
    shutil.copytree(old_dir, new_dir)
    shutil.rmtree(old_dir)
    print("✅ Папка itdpy -> itdirr")
else:
    print("⚠ Папка itdpy не найдена, пропускаем")

# 2. Заменить импорты во всех .py и .md файлах
REPLACEMENTS = [
    ("from itdirr import", "from itdirr import"),
    ("from itdirr.", "from itdirr."),
    ("import itdirr", "import itdirr"),
    ("itdirr/", "itdirr/"),
]

EXTENSIONS = (".py", ".md", ".toml", ".yml", ".yaml", ".txt")

SKIP_DIRS = {".git", "__pycache__", ".venv", "venv", "site"}

updated_files = []

for dirpath, dirnames, filenames in os.walk(ROOT):
    # Пропускаем служебные папки
    dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]

    for filename in filenames:
        if not filename.endswith(EXTENSIONS):
            continue

        filepath = os.path.join(dirpath, filename)

        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()

        new_content = content
        for old, new in REPLACEMENTS:
            new_content = new_content.replace(old, new)

        if new_content != content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
            rel = os.path.relpath(filepath, ROOT)
            updated_files.append(rel)
            print(f"✅ Обновлён: {rel}")

print(f"\nГотово! Обновлено файлов: {len(updated_files)}")
print("\nТеперь выполни команды для пуша:")
print("  git add .")
print('  git commit -m "refactor: rename package itdpy -> itdirr"')
print("  git push origin main")