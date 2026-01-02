"""
Code Quality Commands Module
============================

Commands for linters, formatters, security scanners, and code analysis tools.
"""


# =============================================================================
# CODE QUALITY COMMANDS
# =============================================================================

CODE_QUALITY_COMMANDS: dict[str, set[str]] = {
    "shellcheck": {"shellcheck"},
    "hadolint": {"hadolint"},
    "actionlint": {"actionlint"},
    "yamllint": {"yamllint"},
    "jsonlint": {"jsonlint"},
    "markdownlint": {"markdownlint", "markdownlint-cli"},
    "vale": {"vale"},
    "cspell": {"cspell"},
    "codespell": {"codespell"},
    "cloc": {"cloc"},
    "scc": {"scc"},
    "tokei": {"tokei"},
    "git-secrets": {"git-secrets"},
    "gitleaks": {"gitleaks"},
    "trufflehog": {"trufflehog"},
    "detect-secrets": {"detect-secrets"},
    "semgrep": {"semgrep"},
    "snyk": {"snyk"},
    "trivy": {"trivy"},
    "grype": {"grype"},
    "syft": {"syft"},
    "dockle": {"dockle"},
    # C/C++ static analysis tools
    "cppcheck": {"cppcheck"},
    "clang-tidy": {"clang-tidy", "run-clang-tidy"},
    "clang-format": {"clang-format"},
    "iwyu": {"include-what-you-use", "iwyu"},
    "scan-build": {"scan-build"},
    # Code complexity analysis
    "lizard": {"lizard"},
    "complexity": {"complexity"},
    "radon": {"radon"},
    # Memory and runtime analysis
    "valgrind": {"valgrind", "memcheck", "cachegrind", "callgrind", "helgrind", "drd"},
    "asan": {"asan"},
    "msan": {"msan"},
    "tsan": {"tsan"},
    "ubsan": {"ubsan"},
    # CUDA/GPU analysis tools
    "cuda-tools": {
        "cuda-memcheck",
        "compute-sanitizer",
        "nvprof",
        "nsys",
        "ncu",
        "nsight",
        "nsight-sys",
        "nsight-compute",
    },
}


__all__ = ["CODE_QUALITY_COMMANDS"]
