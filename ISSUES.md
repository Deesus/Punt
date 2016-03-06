+ [ ] Spacing removed in multi-element CSS:
    `minify` has problem when parsing CSS properties that have multiple space-separated elements. E.g. `box-shadow: 0 0 5px rgba(20,20,20,0.5)`
    becomes `box-shadow:005pxrgba(20,20,20,0.5)` -- which is incorrect and causes error in CSS. This is cause by regex, which currently removes
    all space chars inside `{ }`.
