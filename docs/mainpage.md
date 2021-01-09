Main Page
---

This reference  documents the overall structure of the TAStm32 firmware source code. The Python client is not covered here.

## Building
The TAStm32 firmware can be built either directly with gcc/newlib or from within Atollic TRUEStudio.

### Linux
On Debian-alikes, install the following packages: `gcc-arm-none-eabi binutils-arm-none-eabi libnewlib-arm-none-eabi`, then simply run `make`.

On other distributions, simply substitute equivalent packages.

### Windows (TRUEStudio)
1. Right-click on the project > Build Configurations > Set Active > Release.
2. Project > Build Project and check that the console shows no errors. The last line before "build finished" should be "arm-atollic-eabi-objcopy -O ihex TAStm32.elf TAStm32.hex".



TODO: actually write a sane mainpage.
