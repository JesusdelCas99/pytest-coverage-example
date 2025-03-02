pytest test \
  -vv \
  --cov=. \
  --disable-warnings \
  -o junit_family=xunit1 \
  --junitxml=test/junit_xml/xunit-result-00.xml \
  --cov-report=term \
  --cov-report=xml:test/cov_xml/coverage.xml \
  --cov-report=html:test/cov_html \
  --cov-config=test/.coveragerc \
  --ignore=test/test_empty.py \
  --cov-fail-under=95

