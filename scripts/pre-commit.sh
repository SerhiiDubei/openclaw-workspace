#!/bin/bash
# 🛡️ Pre-commit hook — захист від ламання архітектури
# Встановити: ln -s ../../scripts/pre-commit.sh .git/hooks/pre-commit

set -e

REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "$REPO_ROOT"

ERRORS=0

echo "🔍 Перевірка архітектури..."

# 1. Перевірка: нові папки в корені (крім дозволених)
ALLOWED_DIRS="_system scripts tmp"
NEW_DIRS=$(git diff --cached --name-status | grep "^A" | cut -f2 | grep "^[^/]*/" | cut -d'/' -f1 | sort -u | grep -v "^\." || true)

ILLEGAL_DIRS=""
if [ -n "$NEW_DIRS" ]; then
    for dir in $NEW_DIRS; do
        if ! echo "$ALLOWED_DIRS" | grep -qw "$dir"; then
            ILLEGAL_DIRS="$ILLEGAL_DIRS $dir"
        fi
    done
fi

if [ -n "$ILLEGAL_DIRS" ]; then
    echo "❌ ЗАБОРОНЕНО: створення папок в корені:"
    for dir in $ILLEGAL_DIRS; do
        echo "   - $dir/"
    done
    echo ""
    echo "📋 Правильні місця:"
    echo "   - projects/{project-name}/"
    echo "   - skills/{skill-name}/"
    echo "   - memory/users/{username}/"
    echo ""
    ERRORS=$((ERRORS + 1))
fi

# 2. Перевірка: системні файли тільки в корені
SYSTEM_FILES="AGENTS.md BOOTSTRAP.md HEARTBEAT.md IDENTITY.md INSTRUCTION.md MEMORY.md SOUL.md TOOLS.md USER.md"
STAGED_FILES=$(git diff --cached --name-only)

for file in $STAGED_FILES; do
    basename=$(basename "$file")
    # Якщо файл з назвою системного — але не в корені
    if echo "$SYSTEM_FILES" | grep -qw "$basename"; then
        if [ "$(dirname "$file")" != "." ]; then
            echo "❌ Системний файл '$basename' має бути в корені, а не в '$file'"
            ERRORS=$((ERRORS + 1))
        fi
    fi
done

# 3. Перевірка: кавички (curly quotes)
STAGED_MD=$(git diff --cached --name-only | grep "\.md$" || true)
if [ -n "$STAGED_MD" ]; then
    CURLY=$(echo "$STAGED_MD" | xargs grep -l $'[\u2018\u2019\u201c\u201d]' 2>/dev/null || true)
    if [ -n "$CURLY" ]; then
        echo "⚠️  Знайдено фігурні кавички (curly quotes) в:"
        echo "$CURLY" | while read f; do
            echo "   - $f"
        done
        echo "💡 Рекомендація: замінити на прямі кавички ' \" "
        echo ""
        # Це warning, не error
    fi
fi

# Результат
if [ $ERRORS -gt 0 ]; then
    echo ""
    echo "🚫 COMMIT ВІДХИЛЕНО: виправи помилки вище"
    exit 1
fi

echo "✅ Архітектура OK — commit дозволено"
exit 0
