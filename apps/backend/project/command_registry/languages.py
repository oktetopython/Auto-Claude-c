"""
Language Commands Module
========================

Programming language-specific commands including interpreters,
compilers, and language-specific tooling.
"""


# =============================================================================
# LANGUAGE-SPECIFIC COMMANDS
# =============================================================================

LANGUAGE_COMMANDS: dict[str, set[str]] = {
    "python": {
        "python",
        "python3",
        "pip",
        "pip3",
        "pipx",
        "ipython",
        "jupyter",
        "notebook",
        "pdb",
        "pudb",  # debuggers
    },
    "javascript": {
        "node",
        "npm",
        "npx",
    },
    "typescript": {
        "tsc",
        "ts-node",
        "tsx",
    },
    "rust": {
        # Core toolchain
        "cargo",
        "rustc",
        "rustup",
        "rustfmt",
        "rust-analyzer",
        # Cargo subcommand binaries
        "cargo-clippy",
        "cargo-fmt",
        "cargo-miri",
        # Common dev tools
        "cargo-watch",
        "cargo-nextest",
        "cargo-llvm-cov",
        "cargo-tarpaulin",
        # Dependency management
        "cargo-audit",
        "cargo-deny",
        "cargo-outdated",
        "cargo-edit",
        "cargo-update",
        # Build & release
        "cargo-release",
        "cargo-dist",
        "cargo-make",
        "cargo-xtask",
        # Cross-compilation & WASM
        "cross",
        "wasm-pack",
        "wasm-bindgen",
        "trunk",
        # Documentation & publishing
        "cargo-doc",
        "mdbook",
    },
    "go": {
        "go",
        "gofmt",
        "golint",
        "gopls",
        "go-outline",
        "gocode",
        "gotests",
    },
    "ruby": {
        "ruby",
        "gem",
        "irb",
        "erb",
    },
    "php": {
        "php",
        "composer",
    },
    "java": {
        "java",
        "javac",
        "jar",
        "mvn",
        "maven",
        "gradle",
        "gradlew",
        "ant",
    },
    "kotlin": {
        "kotlin",
        "kotlinc",
    },
    "scala": {
        "scala",
        "scalac",
        "sbt",
    },
    "csharp": {
        "dotnet",
        "nuget",
        "msbuild",
    },
    "c": {
        # Compilers
        "gcc",
        "g++",
        "clang",
        "clang++",
        # Build systems
        "make",
        "cmake",
        "ninja",
        "meson",
        # Linker and binary tools
        "ld",
        "ar",
        "nm",
        "objdump",
        "strip",
        "readelf",
        "size",
        "strings",
        # Static analysis
        "cppcheck",
        "clang-tidy",
        "clang-format",
        "include-what-you-use",
        "iwyu",
        "scan-build",
        "lizard",
        # Dynamic analysis
        "valgrind",
        "gdb",
        "lldb",
        "strace",
        "ltrace",
        # Profiling
        "gprof",
        "perf",
        "gcov",
        "lcov",
        "genhtml",
    },
    "cpp": {
        # Compilers
        "gcc",
        "g++",
        "clang",
        "clang++",
        # Build systems
        "make",
        "cmake",
        "ninja",
        "meson",
        # Linker and binary tools
        "ld",
        "ar",
        "nm",
        "objdump",
        "strip",
        "readelf",
        "size",
        "strings",
        # Static analysis
        "cppcheck",
        "clang-tidy",
        "clang-format",
        "include-what-you-use",
        "iwyu",
        "scan-build",
        "lizard",
        # Dynamic analysis
        "valgrind",
        "gdb",
        "lldb",
        "strace",
        "ltrace",
        # Profiling
        "gprof",
        "perf",
        "gcov",
        "lcov",
        "genhtml",
    },
    "cuda": {
        # NVIDIA CUDA Toolkit
        "nvcc",
        "cuda-gdb",
        "cuda-memcheck",
        "compute-sanitizer",
        "nvprof",
        "nsys",
        "ncu",
        "nsight",
        "nsight-sys",
        "nsight-compute",
        "cuobjdump",
        "nvdisasm",
        "ptxas",
        # Also include C++ tools for CUDA projects
        "gcc",
        "g++",
        "clang",
        "clang++",
        "make",
        "cmake",
        "ninja",
        "cppcheck",
        "clang-tidy",
        "clang-format",
        "valgrind",
        "gdb",
        "lldb",
    },
    "elixir": {
        "elixir",
        "mix",
        "iex",
    },
    "haskell": {
        "ghc",
        "ghci",
        "cabal",
        "stack",
    },
    "lua": {
        "lua",
        "luac",
        "luarocks",
    },
    "perl": {
        "perl",
        "cpan",
        "cpanm",
    },
    "swift": {
        "swift",
        "swiftc",
        "xcodebuild",
    },
    "zig": {
        "zig",
    },
    "dart": {
        "dart",
        "dart2js",
        "dartanalyzer",
        "dartdoc",
        "dartfmt",
        "pub",
    },
}


__all__ = ["LANGUAGE_COMMANDS"]
