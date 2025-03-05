pytest tests/ -m "only" \
  -s \
  -vv \
  --cov=. \
  --cov-branch \
  --disable-warnings \
  -o junit_family=xunit1 \
  --junitxml=tests/junit_xml/xunit-result-00.xml \
  --cov-report=term \
  --cov-report=xml:tests/cov_xml/coverage.xml \
  --cov-report=html:tests/cov_html \
  --cov-config=tests/.coveragerc \
  --ignore=tests/test_empty.py \
  --cov-fail-under=85

