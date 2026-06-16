# ChatGPT Plus Image2 iterative loop for premium carousels

Session-derived pattern:

## Target
Reach a luxury-house editorial level for Refrimix carousels using ChatGPT Plus Images, with imported reference imagery and slow, image-by-image approval.

## Proven workflow
1. Open a ChatGPT Project for the campaign.
2. Import the strongest reference image/screenshot into the Project.
3. On the home screen, click `Create an image` to switch the composer into image mode before prompting.
4. Ask for the visual direction first if needed; do not jump straight into a batch of slides.
5. Generate slide 1 only.
6. Review slide 1 before requesting slide 2.
7. If the result misses the target, change only one variable at a time:
   - camera angle
   - daylight softness
   - negative space
   - ceiling / diffuser integration
   - material palette
   - realism level
   - furniture reduction
8. Continue only after approval.
9. Repeat the same direction for up to 10 attempts when the target is hard to hit.
10. Save the best prompt pack, reference board, and failure notes locally.

## UI behavior observed
- ChatGPT image mode changes the composer hint to `Describe or edit an image`.
- A successful first render may take ~50s or more.
- The generated result can still read generic even when the prompt is premium; the first fix to try is composition, not batch regeneration.
- If the image includes commentary-like overlay text, explicitly forbid any UI-style overlays, labels, or captions in the prompt.

## What the target should feel like
- architecture magazine photo
- real premium interior, not a template
- HVAC integrated into the architecture
- luxury without excess
- specific enough that it clearly belongs to Refrimix

## What failed in the first version
- looked like a premium dark template
- relied on decorative framing instead of scene realism
- talked about luxury instead of showing it
- felt too generic before the image loop was tightened

## What improved in the second version
- the image moved toward a corridor / dining-area composition with stronger architectural framing
- it still read as somewhat generic and not yet unmistakably authored
- the next best lever is more spatial specificity, less room-decor language, and a stronger signature ceiling / wall / opening geometry
