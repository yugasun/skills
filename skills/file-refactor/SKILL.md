---
name: file-refactor
description: Automatically optimize and split large files that exceed 600 lines. Use when a file is too large (over 600 lines), when you need to decouple a monolithic module, when a .tsx/.ts or .py file has mixed concerns (types, utils, hooks/components, CLI handlers, formatters), or when splitting a screen component or service module into smaller files. Applies to React/TypeScript frontends and Python backend modules.
---

# File Refactor Skill

This skill optimizes file sizes by extracting types, utilities, hooks/components, formatters, and constants into separate focused modules. Default target: **keep files under 600 lines** unless the repo documents a different limit.

## When to Trigger

- File exceeds 600 lines (or the repo's documented limit)
- Module has mixed concerns (types, utils, handlers, rendering, constants in one file)
- Screen/component has inline sub-components that could be extracted
- Python service has long pure helpers, dataclasses, or CLI subcommands mixed with orchestration
- File has long utility functions that could be separated
- You need to decouple a monolithic file

## Language Routing

| Stack | Typical targets |
| --- | --- |
| TypeScript / React | `types.ts`, `utils.ts`, `hooks/`, `components/`, `constants.ts` |
| Python | `models.py`, `*_format.py`, `*_sections.py`, `utils.py`, `constants.py`, thin `__init__.py` re-exports |

Pick the stack that matches the file you are refactoring. Do not invent a new layout if the surrounding package already has a pattern — mirror neighbors first.

---

## TypeScript / React Splitting Strategy

### 1. Types First

Extract all TypeScript interfaces, types, and enums to `types.ts`:

```typescript
// types.ts
export interface MyProps { ... }
export type MyType = "a" | "b";
export const MY_CONSTANT = ...;
```

### 2. Pure Utility Functions

Extract formatting, grouping, and data transformation functions to `utils.ts`:

```typescript
// utils.ts
export function formatDate(date: Date): string { ... }
export function groupItems(items: Item[]): GroupedItems { ... }
```

### 3. Complex State Logic → Hooks

Extract complex `useState`/`useCallback` logic to `hooks/useXxx.ts`:

```typescript
// hooks/useMyFeature.ts
export function useMyFeature() {
  const [state, setState] = useState(...);
  // ... complex logic
  return { state, actions };
}
```

### 4. Sub-Components → components/

Extract UI sub-components to `components/SubComponent.tsx`:

```typescript
// components/SubComponent.tsx
interface SubComponentProps { ... }
export function SubComponent({ ... }: SubComponentProps) { ... }
```

### 5. Inline Constants/Config

Extract hardcoded arrays and config objects to `constants.ts`:

```typescript
// constants.ts
export const OPTIONS = [
  { value: "a", label: "A" },
  { value: "b", label: "B" },
];
```

---

## Python Splitting Strategy

### 1. Data Models / Types → `models.py`

Extract `@dataclass`, `TypedDict`, `Protocol`, `Literal` aliases, and small immutable value objects:

```python
# models.py
from __future__ import annotations

from dataclasses import dataclass

@dataclass(frozen=True)
class Order:
    id: str
    total: float
```

Keep orchestration and I/O out of `models.py`.

### 2. Pure Helpers → sibling module

Extract formatting, parsing, grouping, and transformation with no side effects:

- Flat package: `utils.py` or domain-specific `*_format.py`
- Large renderer: split `report.py` → `report_format.py` + `report_sections.py`

```python
# report_format.py
def format_pct(value: float | None) -> str:
    ...
```

Import types from `models.py`; avoid circular imports (extract shared types upward if needed).

### 3. Orchestration Stays Thin

The original file should remain the coordinator — CLI entry, service facade, or pipeline driver. Move branches into focused modules:

```
myapp/reports/
├── __init__.py          # public re-exports only
├── models.py            # data types
├── loader.py            # file I/O
├── runner.py            # orchestration
├── report.py            # top-level render entry
├── report_format.py     # string/format helpers
└── report_sections.py   # section builders
```

### 4. CLI / Command Groups

When a CLI module grows, extract subcommand handlers to dedicated modules and keep `main` wiring thin:

```
myapp/cli/
├── main.py              # argparse / click wiring only
├── repl.py              # REPL loop
├── repl_session.py      # session state/helpers extracted from repl
└── stream.py            # streaming path extracted from chat handler
```

### 5. Constants / Prompts / Config

Extract module-level string templates, frozensets, and default dicts:

```python
# constants.py
DEFAULT_TIMEOUT = 30
ALLOWED_COMMANDS = frozenset({"read", "write", "list"})
```

Or keep prompts near the orchestrator if only one consumer exists — do not over-split one-liners.

### 6. Preserve Public API

- Re-export stable names from `__init__.py` when callers import the package root.
- Prefer the project's existing import style (absolute vs relative).
- Respect module boundaries and layering rules defined in the repo (architecture docs, lint rules, import tests).

### 7. Python Conventions

- Start new modules with `from __future__ import annotations` when the repo already does.
- Match existing naming: `snake_case` files/functions, `PascalCase` classes.
- Lazy imports inside functions are fine to break cycles.
- Update or add the smallest targeted test when behavior moves across modules.

---

## Step-by-Step Process

### Step 1: Analyze the File

Read the target file and identify:

1. **Types** — `type`/`interface`/`enum` (TS) or dataclasses / TypedDict / Protocol (Python)
2. **Pure Functions** — no component state, no IPC, no DB/network side effects
3. **Stateful UI logic** — React hooks (TS) or long async orchestration blocks (Python)
4. **Sub-units** — JSX sub-components (TS) or CLI subcommands / report sections / handlers (Python)
5. **Constants** — inline arrays, objects, prompts, config

### Step 2: Create Supporting Files

Mirror the package's existing layout. Create only directories/files you actually need.

```bash
# TypeScript screen module
mkdir -p components/ hooks/

# Python package (flat split — prefer this unless subpackage already exists)
# touch models.py utils.py   # only when warranted
```

### Step 3: Extract and Create

Move code in dependency order: types/models → pure helpers → sections/hooks → orchestrator trim.

### Step 4: Update Original File

1. Add imports for extracted modules
2. Remove extracted code from the original file
3. Keep exports stable for existing callers (`__init__.py` / barrel files / tests)

### Step 5: Verify

**TypeScript / React**

1. Run the repo's typecheck command (e.g. `npm run typecheck`, `tsc --noEmit`)
2. Verify imports/exports and UI behavior

**Python**

1. Run targeted tests for the affected area
2. Run any import-boundary or architecture guard tests the repo provides
3. Confirm public imports still resolve from package roots

---

## Example Layouts

### TypeScript screen module

```
MyScreen/
├── MyScreen.tsx
├── MyScreen.css
├── types.ts
├── utils.ts
├── hooks/
│   └── useMyFeature.ts
└── components/
    └── SubPanel.tsx
```

### Python service package

```
myapp/billing/
├── __init__.py
├── models.py
├── calculator.py
├── invoice.py
├── invoice_format.py
└── invoice_sections.py
```

---

## Output Checklist

After refactoring, verify:

- [ ] Types/models extracted to dedicated module
- [ ] Pure utilities/formatters extracted
- [ ] Hooks/components (TS) or sections/handlers (Python) extracted
- [ ] Constants/prompts extracted when reused or noisy
- [ ] Original file reduced below 600 lines (or repo limit)
- [ ] Typecheck / lint passes
- [ ] Targeted tests pass; module boundaries respected
- [ ] Public exports preserved for downstream imports and tests
- [ ] Functionality preserved

---

## Example Extraction

### TypeScript — 1000-line `MyScreen.tsx`

```typescript
// BEFORE: mixed concerns
interface Props { ... }
const CONSTANT = [...];
function formatData() { ... }
function useMyHook() { useState... }
function SubComponent() { ... }
export function MyScreen() { ... }
```

```typescript
// types.ts — utils.ts — hooks/useMyHook.ts — components/SubComponent.tsx
// MyScreen.tsx (now ~300 lines) imports the above
```

### Python — 900-line `invoice.py`

```python
# BEFORE: mixed concerns
@dataclass
class LineItem: ...

def format_currency(x): ...
def summary_section(data): ...
def render_invoice(data): ...
```

```python
# models.py — invoice_format.py — invoice_sections.py
# invoice.py keeps render_invoice() and wires sections together
```

---

## Key Principles

1. **Single Responsibility** — Each file does one thing well
2. **Cohesion** — Related code stays together
3. **Importability** — Extracted modules can be imported independently
4. **Testability** — Smaller units are easier to test
5. **Preserve Exports** — Don't break existing imports from other files
6. **Mirror the neighborhood** — Follow patterns already used in the same package
