---
name: design-slides-grouped-sub-page
description: Protocol for grouping multiple presentation slides into a single parent slide with fragments (sub-pages) to ensure absolute visual persistence and effortless cross-fade transitions. Use when the user requests to 'group slides together' or when a block diagram must remain stationary while text layers evolve.
---

# Design Slides: Grouped Sub-Page Protocol

This skill enforces a structural pattern for grouping related content into "sub-pages" within a single Reveal.js slide, ensuring that shared visual elements (like diagrams or 3D backgrounds) remain perfectly stationary while specific content layers fade in/out.

## Core Pattern: Vertical Slide Nesting

Instead of separate horizontal sections, related slides are nested within a parent `<section>` to create "vertical slides" (sub-pages). This allows Reveal.js to treat them as a single logical unit while keeping the URL indexing consistent (e.g., `#/6/0/0`, `#/6/0/1`).

### Implementation Template

```html
<!-- Parent Slide (The Group) -->
<section data-auto-animate data-waypoint="SHARED_WAYPOINT">
    
    <!-- Sub-Page 1 -->
    <section data-auto-animate data-transition="fade" class="fade-slide">
        <h2>Sub-Page 1 Title</h2>
        <div class="content-box">
            <p>Initial content...</p>
        </div>
        <!-- Shared Persistent Element -->
        <div data-id="persistent-graphic">
            <!-- SVG or Image -->
        </div>
    </section>

    <!-- Sub-Page 2 -->
    <section data-auto-animate data-transition="fade" class="fade-slide">
        <h2>Sub-Page 2 Title</h2>
        <div class="content-box">
            <p>Evolved content...</p>
        </div>
        <!-- Shared Persistent Element (Stays stationary via data-id) -->
        <div data-id="persistent-graphic">
            <!-- Same SVG/Image with optional additions -->
        </div>
    </section>

</section>
```

## Mandatory Rules

1. **Stationary Anchor**: Always assign the same `data-waypoint` to the parent and all children to lock the background camera.
2. **Motion Suppression**: Apply `data-transition="fade"` and the `.fade-slide` class to every child section to override the global 3D transition.
3. **Identity Syncing**: Use `data-id` on containers that must stay stationary (like diagrams). Reveal.js will smoothly transition the *content* inside them but will not move the *container* itself.
4. **URL Navigation**: Grouped pages will be indexed as `#/H/V/F` (Horizontal/Vertical/Fragment).

## When to Use

- When the user says "Group these pages together."
- When a complex block diagram must "grow" (add blocks) without the diagram itself moving or resetting.
- When transitioning between "Approach", "Reliability", and "Architecture" where the logic is additive.
