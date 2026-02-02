# Bug Log

<!-- Format:
## YYYY-MM-DD - Brief Title

**Issue**: What went wrong
**Root Cause**: Why it happened
**Solution**: How it was fixed
**Prevention**: How to avoid it
-->

## 2026-02-01 - Markdown Tables Not Rendering

**Issue**: Migration timeline tables showed raw markdown (pipe characters) instead of HTML tables.

**Root Cause**: mistune 3.x requires explicit plugin enablement. Only `footnotes` was enabled, not `table`.

**Solution**: Added `'table'` to plugins list in convert_md.py:
```python
markdown = mistune.create_markdown(renderer=renderer, plugins=['footnotes', 'table'])
```

**Prevention**: When adding markdown features, check mistune plugin requirements.
