
<h1 align="center">
  Python Concur
</h1>

<p align="center">
   <img src="https://raw.githubusercontent.com/ajnsit/purescript-concur/master/docs/logo.png" height="100">
</p>

[**Documentation**](https://potocpav.github.io/python-concur/)

[**Examples**](https://github.com/potocpav/python-concur/tree/master/examples)

<!-- Start docs -->

Concur is a Python UI framework based on synchronous generators.

It is a port of [Concur for Haskell](https://github.com/ajnsit/concur) and [Concur for Purescript](https://github.com/ajnsit/purescript-concur).

Concur can be thought of as a layer on top of [PyImGui](https://github.com/swistakm/pyimgui), which is a set of bindings to the [Dear ImGui](https://github.com/ocornut/imgui) UI library. It helps you to get rid of unprincipled code with mutable state, and lets you build structured and composable abstractions.

A discussion of Concur concepts can also be found in the [Documentation for the Haskell/Purescript versions](https://github.com/ajnsit/concur-documentation/blob/master/README.md). This obviously uses Haskell/Purescript syntax and semantics, but many of the concepts will apply to the Python version.

Being an abstraction over ImGui, Concur is best used for debugging, prototyping and data analysis, rather than user-facing applications.

<p align="center">
<img src="https://raw.githubusercontent.com/potocpav/python-concur/master/screenshot.png">
</p>

<!-- End docs -->

## Installation

Concur [is available on PyPI](https://pypi.org/project/concur/) and can be installed using pip:

```sh
pip install concur
```

This Python code should now produce a very simple UI:

```python
import concur as c
c.integrations.main("Hello World", c.button("Close"), 500, 500)
```

Use any of the [examples](https://github.com/potocpav/python-concur/tree/master/examples) as a starting point for your app.

Optionally, replace PyImGui with a [forked version](https://github.com/potocpav/pyimgui). It contains several functions that are missing from upstream. Without those, some more experimental functionality in Concur may be missing and/or buggy (graph plotting).

```sh
pip install git+https://github.com/potocpav/pyimgui.git
```

For Concur development, clone the repo and install it using pip:

```sh
git clone https://github.com/potocpav/python-concur.git
cd python-concur
pip install -e.

examples/all.py # Run the examples to verify installation
```

To build documentation, install [pdoc3](https://pdoc3.github.io/pdoc/) (`pip install pdoc3`) and run the script `./mkdocs.sh`.
