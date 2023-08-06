# prg2xex

Convert [KickAssembler](http://theweb.dk/KickAssembler/Main.html#frontpage) `.prg` object code to Atari 8 Bit .`xex` file.

It does this by prepending `0xff 0xff` to the beginning of the file and then inserting the end address of the code after the start address.

On a Mac you can then double click on the resulting file to open it in the [Atari800MacX](https://www.atarimac.com/atari800macx.php) emulator. 

## Dependencies

* [Python 3](https://www.python.org/download/releases/3.0/)

## Installation

`pip3 install prg2xex`

## Usage

`prg2xex < object.prg > object.xex`

Where `object` is the name of your object code.

## Testing

Run unit tests with:

`pytest`
