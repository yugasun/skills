# Slide Layouts

## 1. Standard Content (Card Grid)
Best for 3-4 key points.
```html
<div class="slide-container" id="slideX">
    <h2 class="animate-in">Slide Title</h2>
    <div class="content-area">
        <div class="grid-tiled">
            <div class="card animate-in delay-1">
                <h3>Point 1</h3>
                <p>Brief description</p>
            </div>
            <div class="card animate-in delay-2">
                <h3>Point 2</h3>
                <p>Brief description</p>
            </div>
            <div class="card animate-in delay-3">
                <h3>Point 3</h3>
                <p>Brief description</p>
            </div>
        </div>
    </div>
</div>
```

## 2. Scrollable Content
Best for code blocks, long tables, or detailed logs.
```html
<div class="slide-container compact" id="slideX">
    <h2 class="animate-in">Detailed Content</h2>
    <div class="content-area scrollable">
        <pre class="code-block">
<!-- Long code content here -->
        </pre>
    </div>
</div>
```

## 3. Checklist
Best for requirements or step completions.
```html
<div class="slide-container" id="slideX">
    <h2 class="animate-in">Checklist</h2>
    <div class="content-area">
        <ul class="checklist">
            <li><span class="check-icon">✓</span> Item 1</li>
            <li><span class="check-icon">✓</span> Item 2</li>
            <li><span class="check-icon">✓</span> Item 3</li>
        </ul>
    </div>
</div>
```

## 4. Compact Grid
Best for 6-8 smaller items.
```html
<div class="slide-container compact" id="slideX">
    <h2 class="animate-in">Many Items</h2>
    <div class="content-area">
        <div class="grid-compact">
            <div class="card animate-in delay-1">Content 1</div>
            <div class="card animate-in delay-1">Content 2</div>
            <!-- More cards -->
        </div>
    </div>
</div>
```

## 5. Split Content (Text + Visual)
Best for explaining a concept with an image or graphic.
```html
<div class="slide-container" id="slideX">
    <h2 class="animate-in">Concept Title</h2>
    <div class="content-area">
        <div class="grid-2">
            <div class="animate-in delay-1">
                <h3>Key Concept</h3>
                <p>Explanation of the concept.</p>
                <ul>
                    <li>Detail 1</li>
                    <li>Detail 2</li>
                </ul>
            </div>
            <div class="animate-in delay-2">
                <!-- Image or Code -->
            </div>
        </div>
    </div>
</div>
```

## 6. Q&A (Final Slide)
Mandatory final slide.
```html
<div class="slide-container" id="slide[LAST]">
    <div class="content-area" style="align-items: center; justify-content: center; text-align: center;">
        <h2 class="animate-in" style="font-size: 52px; margin-bottom: 16px;">Q & A</h2>
        <p class="subtitle animate-in delay-1">Thank you for your attention.</p>
        
        <div class="animate-in delay-2" style="margin-top: 40px; display: flex; gap: 16px;">
            <a href="mailto:your@email.com" class="pill">Contact</a>
        </div>
    </div>
</div>
```
