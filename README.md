# Punt: "Python Grunt" - A Python Task Runner
###### The Python version of GruntJS

Automate your web development work -- the Python way. A work-in-progress.

### API:
- Minify files:
`$ python minify.py INPUT_PATH OUTPUT_PATH`:
```bash
python minify.py ./src/styles.css ./src/output.css 
```

- Prettify files:
`$ python prettify.py INPUT_PATH OUTPUT_PATH [TAB_LENGTH]`:
```bash
python prettify.py ./src/styles.css ./src/output.css 2
```

### Requirements:
- Python 3.x

### Issues:
- See ISSUES.md

### TODO:
- Refactor:
+ [ ] Need a more robust parsing system to handle complexity of code syntax
+ [ ] C.f. `ISSUES.md`
+ [ ] Simplify/refactor regexes
+ [ ] `prettify` can't handle comments well (esp. with nested braces)
+ [ ] Add prettify options (amount of tab spacing or tab-character)
+ [ ] Add ability to parse JS in prettify/minify
+ [ ] Currently doesn't handle files w/ errors (e.g. dangling braces)

- Future:
+ [ ] Add tokenizer/scanner
+ [ ] Translate gruntfiles (to add more tasks)
+ [ ] Add ability to run automation via scripts
+ [ ] Add error handling (point to location of syntax error)
+ [ ] Add cli
+ [ ] Add travis tests
+ [ ] Test for Python 2.x compatibility

### License:
Copyright 2016 Dee Reddy. Apache 2 License.
