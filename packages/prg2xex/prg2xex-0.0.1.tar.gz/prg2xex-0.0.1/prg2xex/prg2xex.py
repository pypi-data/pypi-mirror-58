"""
Convert KickAssembler .prg object code to Atari 8 Bit .xex format
"""
import sys

def process(source):
    """Convert bytearray in .prg format to .xex format"""
    xex = bytearray(b'\xff\xff')
    xex.append(source[0])
    xex.append(source[1])
    xex_end = (source[1] * 255) + source[0] + (len(source) - 2)
    xex.append(int(xex_end % 255))
    xex.append(int(xex_end / 255))
    return xex + source[2:]

def convert():
    """Convert stdin .prg to stdout .xex"""
    try:
        data = sys.stdin.buffer.read()
    except AttributeError:
        sys.exit('error reading from stdin')
    output = process(data)
    sys.stdout.buffer.write(output)

if __name__ == '__main__':

    convert()
