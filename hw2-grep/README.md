# HW2. Grep

HW1 with grep feature

## Usage

Use `interpreter.py` to run CLI

Supported commands:
* `cat`
* `echo`
* `exit`
* `pwd`
* `wc`
* `grep`

Also supports pipes and variables assignment

## Grep

The following flags are available:
*    `-i`, `--ignore-case`
              Ignore case distinctions in  both  the  PATTERN  and  the  input
              files.
*    `-w`, `--word-regexp`
              Select only those  lines  containing  matches  that  form  whole
              words.
*    `-A NUM`, `--after-context=NUM`
              Print NUM  lines  of  trailing  context  after  matching  lines.
              Places   a  line  containing  a  group  separator  (--)  between
              contiguous groups of matches.

## Example

```
> grep plugin build.gradle
apply plugin: 'java'
apply plugin: 'idea'
> cat build.gradle | grep plugin
apply plugin: 'java'
apply plugin: 'idea'
> grep -A 2 plugin build.gradle
apply plugin: 'java'
apply plugin: 'idea'
group = 'ru.example'
version = '1.0'
```

## Про выбор библиотеки для разбора аргументов

Я использовала argparse, ~~потому что он нагуглился первым~~, потому что он лучше всего подошёл для этой задачи.
Вообще, из популярных там есть примерно три библиотеки: argparse, getopt и docopt. Есть ещё какой-нибудь click, но [тут](http://xion.io/post/programming/python-dont-use-click.html) просят его не использовать)

getopt какой-то древний, там нужно писать побольше кода, а ещё там убогие двоеточия

docopt, вроде, норм (и идея с генерацией по документации топ), но он не делает сам классные сообщения об ошибке как argparse, а ещё не чекает типы


