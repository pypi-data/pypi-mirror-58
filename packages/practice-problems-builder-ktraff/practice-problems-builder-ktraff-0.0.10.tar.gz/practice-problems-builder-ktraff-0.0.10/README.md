CLI tool for building practice programming problems
==============================

What Is This?
-------------
This is a simple CLI tool that can be used to build and manage a repository of programming problems and solutions.

The proposed feature set should be able to do the following:

- Creates a skeleton for a new programming problem, for any number of programming languages you like.  This should include linking any shared data structures, algorithms, argument parsing, Makefile, performance profiling, and setting up a test harness
- Shared data structures can also be packaged (using Cargo, for Rust, or as a pip module in Python).  There should be an easy way to edit these data structures from within the repo and then package and send them to PyPI or crates.io with a single command)
- There should be a way to search for these problems within your repository by keyword using the CLI.
- Programming problems can exist in any directory, or in multiple directories, but the directory for a single problem should look like:

```
- problem_name
  - config.yaml
  - README.md (generated)
  - golang
  - rust
  - python
    - Makefile
    - main.py
    - tests
      - shared
      - 1_naive 
    - src
      - shared
      - 1_naive
      - 2_optimized
```

Programming problems should be configured with either YAML or TOML that can be used to configure the programming solution, including generating documentation around the solution:

- Title
- Description (links to markdown READMEs can be optionally included)
- Difficulty (1-10)
- Tags
- Additional Resources

To start, Python, Rust and Go are supported languages.
