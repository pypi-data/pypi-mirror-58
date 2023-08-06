# bver - the Bible version parser

bver is a simple tool to parse Bible translations. It is mostly made for programs that need to specify what translation a user entered.

This is a part of the Heb12 project. See more about us at https://code.theres.life/heb12

## Installation

```
$ git clone https://code.theres.life/heb12/bver
$ cd bver
$ pip install .
```

Soon it will be published on PyPi. Then you will be able to simply run `pip install bver`.

## Usage

Here is an example of basic usage:
```
import bver

print(bver.parse("KJV")["name"])
```

This prints out the full name of the KJV ("King James Version").

Here is an example of the information for a translation:
```
{
	"abbr": "KJV",
	"name": "King James Version",
	"aliases": [
		"Authorised Version", "Authorised King James Version", "Authorised (King James) Version",
		"Authorized Version", "Authorized King James Version", "Authorized (King James) Version",
		"King James Bible", "AV", "AKJV", "KJB"
	]
}
```

## Contributing

Ideas for contributing include:
- Improving the parser to handle more errors and adding new features
- Adding more information about translations
- Adding more translations

## License

Copyright 2020 MotS <https://mtiger.xyz> (read Hebrews 4:12)

You may use this software under the terms of the MIT/Expat license as described in the LICENSE file.

The `bible-translations.json` file is derived from [danday74's work](https://github.com/MasterOfTheTiger/bible-translation-lookup/blob/master/LICENSE.md).
