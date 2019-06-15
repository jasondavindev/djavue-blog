#!/bin/bash
docker-compose -f docker/compose/test.yml run djavue-blog unittests.sh
exitcode=$?
docker-compose -f docker/compose/test.yml down
exit $exitcode
