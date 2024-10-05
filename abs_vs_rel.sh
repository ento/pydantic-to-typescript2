#!/usr/bin/env bash

echo "### Relative import"
set -x
git checkout 972fc5e7e311a43ab14a97e1bfb6e40ca3c39d3d 2>/dev/null
pydantic2ts --module tests/expected_results/enums/v1/input.py --output output.ts --json2ts ./node_modules/.bin/json2ts
grep -E 'Foo.? ' output.ts
set +x
echo ""
echo "### Absolute import"
set -x
git checkout f828b0393d123fbf82b3f45489d61cf81257471d 2>/dev/null
PYTHONPATH=$(pwd)/tests/expected_results/enums/v1 pydantic2ts --module /home/ento/workspace/pydantic-to-typescript2/tests/expected_results/enums/v1/input.py --output output.ts --json2ts ./node_modules/.bin/json2ts
grep -E 'Foo.? ' output.ts
