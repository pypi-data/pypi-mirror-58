## v0.7.1(2019-12-20)

- Wrap code block with 'highlight' container in codehilite mode.

## v0.7.0(2019-12-11)

- Deprecate the extension name with `Extension` suffix, e.g. `FootnoteExtension` -> `Footnote`.
  And the old names will be removed by `v1.0.0`.
- Store extra info after the language text in fenced code:
  ````
  ```python myscript.py    <-- myscript.py is stored in element
  print('hello world')
  ```
  ````
- Built-in code highlight extension using pygments.

## v0.6.0(2019-7-26)

- Reverse the extension order.
- Add a new extension attribute `elements`.
- Improve the CLI, add more options.

## v0.5.1(2019-7-20)

- Add type hints for all primary functions.

## v0.5.0(2019-7-19)

- Update to comply commonmark spec 0.29.
- Change the extension system.

## v0.4.3(2018-9-11)

- Fix TOC rendering when heading level exceeds the max depth.

## v0.4.2(2018-8-16)

- Fix CJK regexp for pangu extension.

## v0.4.0(2018-8-24)

- Support Python 2.7.

## v0.3.4(2018-8-20)

- Fix bugs about extensions.

## v0.3.1(2018-8-20)

- Pangu extension.

## v0.3.0(2018-8-20)

- Change the entry function to a class, add TOC and footnotes extensions.

## v0.2.0(2018-8-17)

- Github flavored markdown and docs.

## v0.1.0(2018-8-16)

- Commonmark spec tests.
