# Audit Log

## 2026-02-05 — Repository Gap Scan

**Analysis**
- Public link mismatch: `Moses_Mansfield_Mowery_1822-1904_Lineage_Confirmation.pdf` is linked from the site but stored in `pdf/internal/`, so public links are broken unless moved or updated.
- Naming guidance conflict: instructions specify kebab-case, but report filenames in `research/reports/` use snake_case.
- Overview drift: `OVERVIEW.md` counts/layout do not match current report inventory or homepage structure.
- Unreferenced assets: 16 non-original image files appear unused; many look like pre-conversion PNGs or potential future location panels.

**Next Steps**
1. Decide whether the Moses lineage PDF should be public, then move it to `pdf/` or remove/update links.
2. Decide the preferred naming convention going forward, then update guidance or plan a rename migration.
3. Confirm whether `OVERVIEW.md` should be updated to current counts and homepage structure.
4. Identify which unreferenced images should be kept, converted to JPG, or archived.
