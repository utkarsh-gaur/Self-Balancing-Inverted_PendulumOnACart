# Self-Balancing Inverted Pendulum on a Cart

Small STM32-based project that balances an inverted pendulum on a cart using an MPU6050 IMU and two-directional DC motor control (TIM1 PWM outputs).

Key points
- MCU: STM32F446 and STM32 HAL (CubeMX-generated project + CMake)
- Sensors: MPU6050 (I2C)
- Motor: H-bridge driven by TIM1 PWM (channels PA8/PA9)
- Control: Complementary filter + PD controller (source: `Core/Src/main.c`)

Quick build (Windows)
1. Install prerequisites: `cmake`, `gcc-arm-none-eabi`, `make` (or `ninja`), and ST-Link/OpenOCD or vendor programmer.
2. From project root:

```powershell
mkdir build
cd build
cmake -DCMAKE_TOOLCHAIN_FILE=cmake/gcc-arm-none-eabi.cmake ..
cmake --build . --config Release
```

Flashing
- Use the included `flash.bat` (Windows) or your preferred tool (ST-Link, OpenOCD, etc.).

Files of interest
- `Core/Src/main.c` — main control loop, IMU read, PD controller
- `CMakeLists.txt` and `cmake/gcc-arm-none-eabi.cmake` — build configuration
- `flash.bat` — example flash script for Windows

Notes
- No license file included. Add a license if you want to publish this for reuse.
- Update pins and wiring to match your hardware before powering the system.

If you'd like, I can:
- Add a `LICENSE` (MIT) and enhance the README with wiring diagrams
- Add a basic GitHub Actions CI to build on push
