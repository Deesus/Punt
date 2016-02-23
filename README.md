# Punt - A Python Task Runner
###### The Python version of GruntJS

Automate your web development work -- the Python way. A work-in-progress.

# BUG:
NOTE: `minify` parser is bugged when it encounters child elements -- e.g.
`.foobar ul` or `#main .subsection` or `#foo .bar ul` etc.

### API:
- minify files:
`$ python minify.py INPUT_PATH OUTPUT_PATH`:
```shell
python minify.py ./src/styles.css ./src/output.css 
```

### Requirements:
- Python 3.x

### TODO:
+ [ ] Add JS support
+ [ ] Add prettify function
+ [ ] Translate gruntfiles (to add more tasks)
+ [ ] Add ability to run automation via scripts
+ [ ] Add error handling
+ [ ] Add cli
+ [ ] Add travis tests

### License:
Copyright 2016 Dee Reddy. Apache 2 License.
