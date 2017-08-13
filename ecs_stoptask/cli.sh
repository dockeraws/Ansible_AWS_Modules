#!/bin/bash
aws ecs start-task --cluster test-automation --task-definition test_task --container-instances 2c3f3f0d-76db-42b2-8fdd-9edf1595e62e
