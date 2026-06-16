# Legacy carousel redraw and replace pattern

Use this when the user points to an existing Refrimix carousel folder and says it looks amateur, junior, or should be remade from scratch.

## Trigger

- Existing folder under `/home/will/Imagens/carroceis/<slug>` already contains PNGs and `caption.txt`.
- User explicitly says not to keep legacy images or wants a modern/premium refactor.
- Goal is a finished posting bundle, not a long strategy document.

## Fast workflow

1. Audit the legacy folder first.
   - Count files.
   - Record image dimensions and file names.
   - Identify whether there are editable source files or only raster exports.
   - Look for duplicated names, repeated concepts, weak CTA, clutter, poor typography, and stock/template feel.

2. Create a short ephemeral PRD if `/plan-enfemero` is invoked.
   - Keep it outside the final delivery folder, e.g. `/tmp/hermes-plan-enfemero/<slug>/PRD.md`.
   - Use it to define acceptance criteria: 5 PNGs, correct dimensions, caption, backup, no legacy images.

3. Rebuild the creative system from zero.
   - Do not reuse old PNGs as backgrounds, overlays, crops, or hidden assets when the user says not to keep legacy images.
   - Preserve only strategic learning from the audit: what was weak and what must improve.
   - Use a modern typography system: one strong sans family, bold display titles, thin subtitles, large negative space, strict grid, subtle technical lines.

4. Replace safely.
   - Move the old folder to `/home/will/Imagens/carroceis/_archive/<slug>_legacy_<date>` before writing the new package.
   - Recreate the original target folder cleanly.
   - Final folder should contain only the approved 5 PNGs and `caption.txt` unless the user requests notes/prompts.

5. Validate before final response.
   - Exactly 5 PNG files.
   - Each PNG has target dimensions, usually 1080x1350 or the workflow’s requested format.
   - `caption.txt` exists.
   - No legacy file names remain in the final folder.
   - No extra notes, PRDs, scripts, contact sheets, or workbench files remain in the final folder.
   - If you create a contact sheet for visual QA, keep it in the workbench and delete it before final delivery unless the user asks to keep it.

## Copy structure for PMOC hospitalar

Use the Refrimix 5-page arc:

1. Hook: PMOC hospitalar is not routine/checklist.
2. Belief shift: air is part of clinical infrastructure.
3. Consequences: loss of control raises operational risk.
4. Technical solution: engineering, data, scheduled inspections, automation.
5. Premium CTA: elevate the PMOC standard with Refrimix.

## Visual direction

- Premium editorial, technical, hospital-grade.
- Cold palette: deep graphite/navy, ice white, petroleum blue, cyan/green hospital accent.
- Big typographic hierarchy: display title first, subtitle second, microcopy last.
- Avoid cheap installer-stock aesthetics, generic gradients, fake hospital renders, excessive warning colors, and microtext.

## Reporting

Final response should be short and operational:

- Final folder path.
- Files created.
- Backup path for legacy package.
- Smoke results.
- Any remaining durable workbench artifact, if intentionally kept.
