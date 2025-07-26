# Contributing to Project Template

1. Fork the repository and create a feature branch from `develop`.
2. Follow the setup instructions in `README.md`.
3. Ensure all pre-commit hooks pass: `pre-commit run --all-files`.
4. Write tests for new features in `tests/`.
5. Update documentation in `docs/`.
6. Submit a pull request to `develop` with a clear description.

## Code Quality

- Use type annotations for all functions, including `pytest` fixtures (e.g., `capsys: "pytest.CaptureFixture[str]"`, `-> None`).
- Run `pre-commit run --all-files` to ensure compliance with `mypy`, `pylint`, `black`, and `flake8`.

- Use LF line endings (set `git config core.autocrlf false` and `core.eol lf`).
- `pylint` skips `C0114`, `F0401`, `E0611`, `C0327`.
- Run `pre-commit run --all-files` to ensure compliance.
